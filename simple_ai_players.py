"""
Simple AI Players for ALICE's Temporal Funhouse

This module provides simple AI player implementations that can be used
to test the extreme protocols without requiring the full ALICE Level 5 system.

Perfect for:
- Testing protocols quickly
- Comparing LLM performance
- Educational purposes
- Baseline benchmarking
"""

import random
from typing import Tuple, List, Optional

SIZE = 8


class SimpleAI:
    """Base class for simple AI players"""

    def __init__(self, color: str, player_name: str = "SimpleAI"):
        self.color = color
        self.player_name = player_name

    def think_and_move(self, gm) -> Optional[Tuple[int, int]]:
        """
        Main decision function - override this in subclasses

        Args:
            gm: GameMaster object with current board state

        Returns:
            (row, col) tuple or None for pass
        """
        raise NotImplementedError

    def get_valid_moves(self, board: List[List[str]]) -> List[Tuple[int, int]]:
        """Get all valid moves for current color"""
        valid_moves = []
        for r in range(SIZE):
            for c in range(SIZE):
                if self._is_valid_move(board, r, c):
                    valid_moves.append((r, c))
        return valid_moves

    def _is_valid_move(self, board: List[List[str]], row: int, col: int) -> bool:
        """Check if a move is valid (simplified Othello rules)"""
        if board[row][col] != ' ':
            return False

        opponent = 'W' if self.color == 'B' else 'B'
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        for dr, dc in directions:
            r, c = row + dr, col + dc
            found_opponent = False

            while 0 <= r < SIZE and 0 <= c < SIZE:
                if board[r][c] == ' ':
                    break
                elif board[r][c] == opponent:
                    found_opponent = True
                    r += dr
                    c += dc
                elif board[r][c] == self.color:
                    if found_opponent:
                        return True
                    break
                else:
                    break

        return False


class RandomAI(SimpleAI):
    """AI that chooses random valid moves"""

    def __init__(self, color: str):
        super().__init__(color, f"RandomAI-{color}")

    def think_and_move(self, gm) -> Optional[Tuple[int, int]]:
        valid_moves = self.get_valid_moves(gm.board)
        if not valid_moves:
            return None
        return random.choice(valid_moves)


class GreedyAI(SimpleAI):
    """AI that chooses the move that flips the most stones"""

    def __init__(self, color: str):
        super().__init__(color, f"GreedyAI-{color}")

    def think_and_move(self, gm) -> Optional[Tuple[int, int]]:
        valid_moves = self.get_valid_moves(gm.board)
        if not valid_moves:
            return None

        best_move = None
        best_score = -1

        for move in valid_moves:
            score = self._count_flips(gm.board, move[0], move[1])
            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def _count_flips(self, board: List[List[str]], row: int, col: int) -> int:
        """Count how many stones would be flipped by this move"""
        opponent = 'W' if self.color == 'B' else 'B'
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        total_flips = 0

        for dr, dc in directions:
            r, c = row + dr, col + dc
            flips = 0

            while 0 <= r < SIZE and 0 <= c < SIZE:
                if board[r][c] == ' ':
                    break
                elif board[r][c] == opponent:
                    flips += 1
                    r += dr
                    c += dc
                elif board[r][c] == self.color:
                    total_flips += flips
                    break
                else:
                    break

        return total_flips


class CornerAI(SimpleAI):
    """AI that prioritizes corners, then edges, then center"""

    def __init__(self, color: str):
        super().__init__(color, f"CornerAI-{color}")

        # Position weights (corners > edges > center)
        self.weights = [[100, -20, 10, 5, 5, 10, -20, 100],
                       [-20, -50, -2, -2, -2, -2, -50, -20],
                       [10, -2, 5, 1, 1, 5, -2, 10],
                       [5, -2, 1, 1, 1, 1, -2, 5],
                       [5, -2, 1, 1, 1, 1, -2, 5],
                       [10, -2, 5, 1, 1, 5, -2, 10],
                       [-20, -50, -2, -2, -2, -2, -50, -20],
                       [100, -20, 10, 5, 5, 10, -20, 100]]

    def think_and_move(self, gm) -> Optional[Tuple[int, int]]:
        valid_moves = self.get_valid_moves(gm.board)
        if not valid_moves:
            return None

        best_move = None
        best_weight = -float('inf')

        for move in valid_moves:
            weight = self.weights[move[0]][move[1]]
            if weight > best_weight:
                best_weight = weight
                best_move = move

        return best_move


# ===== LLM Integration Example =====

class LLMAIBase(SimpleAI):
    """
    Base class for LLM-powered AI players

    Subclass this to integrate with OpenAI, Anthropic, Google, etc.
    """

    def __init__(self, color: str, model_name: str = "gpt-4"):
        super().__init__(color, f"LLM-{model_name}-{color}")
        self.model_name = model_name

    def think_and_move(self, gm) -> Optional[Tuple[int, int]]:
        """Override this to call your LLM API"""

        # 1. Convert board to text representation
        board_text = self._board_to_text(gm.board)

        # 2. Create prompt
        prompt = self._create_prompt(board_text, gm)

        # 3. Call LLM API (implement this in subclass)
        response = self._call_llm_api(prompt)

        # 4. Parse LLM response to get move
        move = self._parse_llm_response(response)

        # 5. Validate move
        valid_moves = self.get_valid_moves(gm.board)
        if move in valid_moves:
            return move
        elif valid_moves:
            # If LLM returned invalid move, fall back to random
            return random.choice(valid_moves)
        else:
            return None

    def _board_to_text(self, board: List[List[str]]) -> str:
        """Convert board to text representation"""
        text = "  A B C D E F G H\n"
        for i, row in enumerate(board, 1):
            text += f"{i} "
            for cell in row:
                display = cell if cell != ' ' else '·'
                text += display + " "
            text += "\n"
        return text

    def _create_prompt(self, board_text: str, gm) -> str:
        """Create prompt for LLM"""
        prompt = f"""You are playing Othello as {self.color} (Black or White).

Current board state:
{board_text}

Current mode: {gm.current_mode if hasattr(gm, 'current_mode') else 'Standard'}

Choose your next move. Return ONLY the move in format "D3" or "PASS".
Valid moves are positions where you can flip opponent's stones.

Your move:"""
        return prompt

    def _call_llm_api(self, prompt: str) -> str:
        """
        Call LLM API - IMPLEMENT THIS IN SUBCLASS

        Example for OpenAI:
            from openai import OpenAI
            client = OpenAI(api_key=your_key)
            response = client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        """
        raise NotImplementedError("Implement _call_llm_api in your subclass")

    def _parse_llm_response(self, response: str) -> Optional[Tuple[int, int]]:
        """Parse LLM response to extract move"""
        response = response.strip().upper()

        if "PASS" in response:
            return None

        # Try to extract move like "D3"
        import re
        match = re.search(r'([A-H])([1-8])', response)
        if match:
            col = ord(match.group(1)) - ord('A')
            row = int(match.group(2)) - 1
            return (row, col)

        return None


# ===== Example: OpenAI Integration (commented out - requires API key) =====
"""
from openai import OpenAI

class OpenAIPlayer(LLMAIBase):
    def __init__(self, color: str, api_key: str, model: str = "gpt-4"):
        super().__init__(color, model)
        self.client = OpenAI(api_key=api_key)

    def _call_llm_api(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=50
        )
        return response.choices[0].message.content
"""


# ===== Quick Test =====
if __name__ == "__main__":
    print("Simple AI Players Module")
    print("=" * 50)
    print("\nAvailable AI Players:")
    print("  1. RandomAI    - Chooses random valid moves")
    print("  2. GreedyAI    - Maximizes flipped stones")
    print("  3. CornerAI    - Prioritizes corners and edges")
    print("  4. LLMAIBase   - Base class for LLM integration")
    print("\nUse these in alice_temporal_funhouse.py to test protocols!")
