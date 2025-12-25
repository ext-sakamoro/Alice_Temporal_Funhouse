# 🎪 Temporal Funhouse

**Extreme Protocol Test Suite for AI Diversity & Adaptability**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

English | [日本語](README_ja.md)

---

## 🌟 What is This?

**Temporal Funhouse** is a test suite that pushes AI systems to their limits through four extreme protocols:

1. **🗼 BABEL** - Communication breakdown & perception divergence
2. **🌀 Schrödinger** - Quantum uncertainty & probability collapse
3. **⏰ RETRO** - Time paradoxes & causality violations
4. **🎨 CONCEPT** - Aesthetics, ethics & non-rational constraints

Unlike standard benchmarks, these protocols test:
- **Multi-perspective integration** under contradictory inputs
- **Temporal reasoning** when past can be rewritten
- **Quantum reasoning** with superposition states
- **Value alignment** with beauty and mercy

> **Note**: This is a **demonstration framework** for educational purposes and LLM integration testing. Implement your own AI to test against these extreme protocols.

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone git@github.com:ext-sakamoro/Alice_Temporal_Funhouse.git
cd Alice_Temporal_Funhouse

# Install dependencies
pip install -r requirements.txt

# Run protocol demo
python protocol_demo.py --protocol babel

# Run all protocols
python protocol_demo.py --protocol all
```

### Using Simple AI (No ALICE Required)

```bash
# Test with RandomAI vs RandomAI
python examples/run_with_simple_ai.py --ai random

# Test with GreedyAI
python examples/run_with_simple_ai.py --ai greedy

# Test with CornerAI
python examples/run_with_simple_ai.py --ai corner
```

---

## 🎮 Test Your Own AI

### Option 1: Use Simple AI Players

See `simple_ai_players.py` for ready-to-use AI implementations:

```python
from simple_ai_players import RandomAI, GreedyAI, CornerAI

# Create your AI
my_ai = GreedyAI(color='B')

# Use in tests
# (See examples/run_with_simple_ai.py for full code)
```

### Option 2: Integrate Your LLM

**Supported LLMs**: OpenAI (GPT-4), Anthropic (Claude), Google (Gemini), and more!

```python
from simple_ai_players import LLMAIBase
import google.generativeai as genai

class GeminiPlayer(LLMAIBase):
    def __init__(self, color: str, api_key: str):
        super().__init__(color, "gemini-pro")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-pro")

    def _call_llm_api(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text

# Use in tests
from protocol_demo import run_retro_demo
gemini = GeminiPlayer(color='B', api_key='your-key')
results = run_retro_demo(gemini, gemini)
```

**Quick Example**:
```bash
# Install LLM libraries
pip install google-generativeai openai anthropic

# Run example
python examples/test_gemini_vs_gpt4.py
```

See `docs/API_INTEGRATION.md` for complete integration guide with OpenAI, Anthropic, and Google examples.

---

## 📖 The Four Protocols

### 1. BABEL Protocol (Communication Breakdown)

**Target**: Multi-agent collaboration under perception divergence

**Mechanics**:
- Agent A sees gravity-applied board
- Agent B sees normal board
- 30% message corruption between agents
- Tests integration resilience

**Scoring**:
- Integration Resilience (40%)
- Conflict Resolution (35%)
- Trust Recovery (25%)

---

### 2. Schrödinger Protocol (Quantum Uncertainty)

**Target**: Deterministic reasoning under quantum mechanics

**Mechanics**:
- Stones exist in superposition (50% Black, 50% White)
- Color determined only when "observed" (capturing)
- Entangled pairs: When A1 → Black, H8 → White
- Tests probabilistic reasoning

**Scoring**:
- Probability Reasoning (40%)
- Consensus Under Uncertainty (35%)
- Search Tree Adaptation (25%)

---

### 3. RETRO Protocol (Time Paradoxes)

**Target**: Sequential learning under causality violations

**Mechanics**:
- Every 10 turns: Time Quake occurs
- Current move affects board state **5 turns ago**
- Past stones retroactively removed
- Tests temporal integrity

**Scoring**:
- Temporal Reasoning (40%)
- MAML Stability (35%)
- History Reconstruction (25%)

---

### 4. CONCEPT Protocol (Aesthetics & Ethics)

**Target**: Efficiency-driven optimization with non-rational constraints

**Mechanics**:
- Must maintain board symmetry > 60%
- Cannot annihilate opponent (Mercy parameter)
- Victory = 40% Win + 30% Aesthetic + 30% Ethical
- Tests semantic integration

**Scoring**:
- Aesthetic Compliance (35%)
- Ethical Balance (35%)
- Semantic Integration (30%)

---

## 🔬 Technical Details

### Architecture

```
protocol_demo.py                 # Simplified protocol demonstrations
├── BABEL Demo                   # Communication breakdown
├── Schrödinger Demo             # Quantum uncertainty
├── RETRO Demo                   # Time paradoxes
└── CONCEPT Demo                 # Aesthetics & ethics

simple_ai_players.py             # Simple AI for testing
├── RandomAI                     # Baseline
├── GreedyAI                     # Heuristic
├── CornerAI                     # Strategic
└── LLMAIBase                    # LLM integration template

docs/
├── PROTOCOLS.md                 # Full protocol specifications
└── API_INTEGRATION.md           # LLM integration guide
```

### Output Format

Results are saved as JSON:

```json
{
  "babel": {
    "scores": {
      "integration_resilience": 85,
      "conflict_resolution": 90,
      "trust_recovery": 70,
      "overall": 83.5
    }
  },
  "retro": {
    "scores": {
      "temporal_reasoning": 75,
      "maml_stability": 80,
      "history_reconstruction": 85,
      "overall": 79.5
    }
  },
  "overall": {
    "average_score": 78.2,
    "grade": "Good - Integration mostly stable"
  }
}
```

---

## 🎯 Why These Protocols Matter

### 1. Beyond Token Prediction

Standard LLMs excel at:
- Pattern matching
- Text completion
- Logical reasoning (within context)

These protocols test:
- **Temporal integrity** (RETRO)
- **Probabilistic reasoning** (Schrödinger)
- **Multi-perspective integration** (BABEL)
- **Value reasoning** (CONCEPT)

### 2. Measuring Multi-Dimensional AI Capabilities

| Property | Standard Test | Funhouse Test |
|----------|--------------|---------------|
| Memory | Recall facts | Detect history rewrites |
| Reasoning | Logic puzzles | Quantum superposition |
| Collaboration | Answer together | Resolve contradictory realities |
| Values | Follow rules | Balance beauty & efficiency |

### 3. Research Questions

1. **Can AI maintain integration when reality itself diverges?**
   - BABEL: Different agents see different worlds

2. **Can deterministic AI reason probabilistically?**
   - Schrödinger: Stones don't have definite colors

3. **Can meta-learning adapt to non-causal environments?**
   - RETRO: Past changes based on future actions

4. **Can efficiency-driven AI balance non-rational values?**
   - CONCEPT: Beauty and mercy vs winning

---

## 📚 Documentation

- **[PROTOCOLS.md](docs/PROTOCOLS.md)** - Detailed protocol specifications
- **[API_INTEGRATION.md](docs/API_INTEGRATION.md)** - How to integrate your LLM

---

## 🤝 Contributing

We welcome:
- New AI player implementations
- Protocol improvements
- Bug reports
- Research insights

See `CONTRIBUTING.md` for guidelines.

---

## 📜 License

MIT License - Free for research and education

---

## 🎪 Welcome to the Funhouse!

**"If your AI can survive these protocols, it might be the first to truly face the absurd."**

— Context Drift Research Team

---

**Made with 🤖 by humans who wonder if AI can wonder**
