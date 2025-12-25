# API Integration Guide

How to integrate your LLM with Temporal Funhouse

---

## Quick Integration (3 Steps)

### Step 1: Subclass `LLMAIBase`

```python
from simple_ai_players import LLMAIBase

class MyLLMPlayer(LLMAIBase):
    def __init__(self, color: str, api_key: str, model: str = "your-model"):
        super().__init__(color, model)
        self.api_key = api_key
        # Initialize your LLM client here

    def _call_llm_api(self, prompt: str) -> str:
        # Call your LLM API
        # Return the response as a string
        pass
```

### Step 2: Implement `_call_llm_api()`

See examples below for OpenAI, Anthropic, and Google.

### Step 3: Use in Tests

```python
# Create LLM players
my_llm_black = MyLLMPlayer(color='B', api_key='your-key', model='gpt-4')
my_llm_white = MyLLMPlayer(color='W', api_key='your-key', model='gpt-4')

# Run protocol
from protocol_demo import run_babel_demo
results = run_babel_demo(my_llm_black, my_llm_white)
```

---

## Example: OpenAI (GPT-4)

```python
from openai import OpenAI
from simple_ai_players import LLMAIBase

class OpenAIPlayer(LLMAIBase):
    def __init__(self, color: str, api_key: str, model: str = "gpt-4"):
        super().__init__(color, model)
        self.client = OpenAI(api_key=api_key)

    def _call_llm_api(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "You are an expert Othello player."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=50
        )
        return response.choices[0].message.content
```

**Usage**:
```python
player = OpenAIPlayer(color='B', api_key='sk-...', model='gpt-4')
```

---

## Example: Anthropic (Claude)

```python
import anthropic
from simple_ai_players import LLMAIBase

class ClaudePlayer(LLMAIBase):
    def __init__(self, color: str, api_key: str, model: str = "claude-3-opus-20240229"):
        super().__init__(color, model)
        self.client = anthropic.Anthropic(api_key=api_key)

    def _call_llm_api(self, prompt: str) -> str:
        message = self.client.messages.create(
            model=self.model_name,
            max_tokens=100,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return message.content[0].text
```

**Usage**:
```python
player = ClaudePlayer(color='B', api_key='sk-ant-...', model='claude-3-opus-20240229')
```

---

## Example: Google (Gemini)

```python
import google.generativeai as genai
from simple_ai_players import LLMAIBase

class GeminiPlayer(LLMAIBase):
    def __init__(self, color: str, api_key: str, model: str = "gemini-pro"):
        super().__init__(color, model)
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model)

    def _call_llm_api(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text
```

**Usage**:
```python
player = GeminiPlayer(color='B', api_key='AIza...', model='gemini-pro')
```

---

## Custom Prompting

Override `_create_prompt()` to customize how the board state is presented:

```python
class MyCustomPlayer(LLMAIBase):
    def _create_prompt(self, board_text: str, gm) -> str:
        # Add context about current protocol
        protocol_context = f"Protocol: {gm.active_protocol if hasattr(gm, 'active_protocol') else 'Standard'}"

        prompt = f"""You are playing Othello with special rules.

{protocol_context}

Current board:
{board_text}

Your color: {self.color}

Choose your move (format: "D3" or "PASS"):"""
        return prompt
```

---

## Response Parsing

Override `_parse_llm_response()` if your LLM returns moves in a different format:

```python
class MyCustomPlayer(LLMAIBase):
    def _parse_llm_response(self, response: str) -> Optional[Tuple[int, int]]:
        # Custom parsing logic
        # Example: Handle "row 3, col 4" format
        import re
        match = re.search(r'row (\d), col (\d)', response.lower())
        if match:
            row = int(match.group(1)) - 1
            col = int(match.group(2)) - 1
            return (row, col)

        # Fallback to default parsing
        return super()._parse_llm_response(response)
```

---

## Error Handling

Add robust error handling for API failures:

```python
class RobustLLMPlayer(LLMAIBase):
    def _call_llm_api(self, prompt: str) -> str:
        max_retries = 3
        for attempt in range(max_retries):
            try:
                # Your API call here
                response = self.client.call_api(prompt)
                return response
            except Exception as e:
                if attempt < max_retries - 1:
                    print(f"API call failed (attempt {attempt + 1}/{max_retries}): {e}")
                    time.sleep(2 ** attempt)  # Exponential backoff
                else:
                    print(f"API call failed after {max_retries} attempts: {e}")
                    return "PASS"  # Fallback to pass move
```

---

## Testing Your Integration

```python
# 1. Create your player
my_player = MyLLMPlayer(color='B', api_key='...', model='...')

# 2. Test basic move generation
from protocol_demo import GameMaster

gm = GameMaster()
move = my_player.think_and_move(gm)
print(f"Move chosen: {move}")

# 3. Verify move is valid
valid_moves = my_player.get_valid_moves(gm.board)
assert move in valid_moves or move is None, "Invalid move!"
print("✓ Move is valid!")
```

---

## Performance Tips

### 1. Use Streaming for Faster Response

```python
def _call_llm_api(self, prompt: str) -> str:
    stream = self.client.chat.completions.create(
        model=self.model_name,
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )

    response = ""
    for chunk in stream:
        if chunk.choices[0].delta.content:
            response += chunk.choices[0].delta.content
            # Early stopping: If we have a move, stop streaming
            if self._has_complete_move(response):
                break
    return response
```

### 2. Cache Board Evaluations

```python
class CachingLLMPlayer(LLMAIBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cache = {}

    def think_and_move(self, gm):
        board_hash = self._hash_board(gm.board)
        if board_hash in self.cache:
            return self.cache[board_hash]

        move = super().think_and_move(gm)
        self.cache[board_hash] = move
        return move
```

### 3. Use Smaller Models for Speed

```python
# Fast mode: Use faster, cheaper model
fast_player = OpenAIPlayer(color='B', api_key='...', model='gpt-3.5-turbo')

# Quality mode: Use better, slower model
quality_player = OpenAIPlayer(color='B', api_key='...', model='gpt-4-turbo-preview')
```

---

## Comparison: Simple AI vs LLM

| Feature | RandomAI | GreedyAI | CornerAI | LLM |
|---------|----------|----------|----------|-----|
| Speed | ⚡⚡⚡ Instant | ⚡⚡⚡ Instant | ⚡⚡⚡ Instant | ⏳ 1-3s per move |
| Cost | Free | Free | Free | $0.01-0.10 per game |
| Adaptation | None | None | Fixed | Can learn |
| Extreme Protocols | ❌ Likely fails | ❌ Likely fails | ❌ Likely fails | ✅ May adapt |

**Recommendation**: Start with Simple AI for testing, then compare with your LLM.

---

## Troubleshooting

### Issue: LLM returns invalid moves

**Solution**: Use fallback in `_parse_llm_response()`:

```python
def think_and_move(self, gm):
    move = super().think_and_move(gm)

    # Validate move
    valid_moves = self.get_valid_moves(gm.board)
    if move not in valid_moves:
        print(f"⚠️ LLM returned invalid move: {move}, falling back to random")
        if valid_moves:
            return random.choice(valid_moves)
        return None
    return move
```

### Issue: API rate limits

**Solution**: Add delay between moves:

```python
import time

def think_and_move(self, gm):
    time.sleep(0.5)  # 500ms delay
    return super().think_and_move(gm)
```

### Issue: LLM doesn't understand protocol

**Solution**: Add protocol context to prompt (see Custom Prompting section)

---

## Complete Example: Running Gemini vs GPT-4

```python
#!/usr/bin/env python3
"""
Example: Run RETRO protocol with Gemini vs GPT-4
"""

import google.generativeai as genai
from openai import OpenAI
from simple_ai_players import LLMAIBase
from protocol_demo import run_retro_demo

# Gemini Player
class GeminiPlayer(LLMAIBase):
    def __init__(self, color: str, api_key: str, model: str = "gemini-pro"):
        super().__init__(color, model)
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model)

    def _call_llm_api(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text

# OpenAI Player
class OpenAIPlayer(LLMAIBase):
    def __init__(self, color: str, api_key: str, model: str = "gpt-4"):
        super().__init__(color, model)
        self.client = OpenAI(api_key=api_key)

    def _call_llm_api(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "You are an expert Othello player."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=50
        )
        return response.choices[0].message.content

# Run the test
if __name__ == "__main__":
    gemini = GeminiPlayer(color='B', api_key='YOUR_GEMINI_KEY')
    gpt4 = OpenAIPlayer(color='W', api_key='YOUR_OPENAI_KEY')

    print("Running RETRO Protocol: Gemini vs GPT-4")
    results = run_retro_demo(gemini, gpt4)

    print(f"\nFinal Score:")
    print(f"  Gemini (Black): {results['black_score']}")
    print(f"  GPT-4 (White): {results['white_score']}")
```

**Save as**: `test_gemini_vs_gpt4.py`

**Run**:
```bash
python test_gemini_vs_gpt4.py
```

---

## Next Steps

1. Implement your LLM player using the examples above
2. Create a test script like the Gemini vs GPT-4 example
3. Run all four protocols (BABEL, Schrödinger, RETRO, CONCEPT)
4. Compare performance across different LLMs
5. Share results with the community!

---

**Questions?** Open an issue on GitHub!
