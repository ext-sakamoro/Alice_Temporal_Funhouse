#!/usr/bin/env python3
"""
Temporal Funhouse - Protocol Demo
==================================
Simplified demonstration of extreme protocols using Simple AI players.

This is a teaching/demo version. For full protocol implementation with
advanced AI systems, see the complete version in the research repository.

Usage:
    python protocol_demo.py --protocol babel
    python protocol_demo.py --protocol retro
    python protocol_demo.py --ai greedy
"""

import random
import argparse
from typing import List, Tuple, Optional
from simple_ai_players import RandomAI, GreedyAI, CornerAI

SIZE = 8


# ============================================================
# BASIC OTHELLO GAME MASTER
# ============================================================

class GameMaster:
    """Simplified Game Master for Othello"""

    def __init__(self):
        self.board = [[' ' for _ in range(SIZE)] for _ in range(SIZE)]
        self.turn_count = 0
        self.move_history = []

        # Initial setup
        mid = SIZE // 2
        self.board[mid-1][mid-1] = 'W'
        self.board[mid-1][mid] = 'B'
        self.board[mid][mid-1] = 'B'
        self.board[mid][mid] = 'W'

    def make_move(self, player_color: str, move: Optional[Tuple[int, int]]) -> bool:
        """Execute a move"""
        if move is None:
            return True  # Pass move

        row, col = move
        if not self._is_valid_move(player_color, row, col):
            return False

        # Place stone
        self.board[row][col] = player_color

        # Flip stones
        self._flip_stones(player_color, row, col)

        # Record history
        self.move_history.append({
            'turn': self.turn_count,
            'player': player_color,
            'move': move
        })

        self.turn_count += 1
        return True

    def _is_valid_move(self, color: str, row: int, col: int) -> bool:
        """Check if move is valid"""
        if self.board[row][col] != ' ':
            return False

        opponent = 'W' if color == 'B' else 'B'
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        for dr, dc in directions:
            r, c = row + dr, col + dc
            found_opponent = False

            while 0 <= r < SIZE and 0 <= c < SIZE:
                if self.board[r][c] == ' ':
                    break
                elif self.board[r][c] == opponent:
                    found_opponent = True
                    r += dr
                    c += dc
                elif self.board[r][c] == color:
                    if found_opponent:
                        return True
                    break
                else:
                    break

        return False

    def _flip_stones(self, color: str, row: int, col: int):
        """Flip opponent stones"""
        opponent = 'W' if color == 'B' else 'B'
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        for dr, dc in directions:
            r, c = row + dr, col + dc
            stones_to_flip = []

            while 0 <= r < SIZE and 0 <= c < SIZE:
                if self.board[r][c] == ' ':
                    break
                elif self.board[r][c] == opponent:
                    stones_to_flip.append((r, c))
                    r += dr
                    c += dc
                elif self.board[r][c] == color:
                    # Flip all stones in this direction
                    for flip_r, flip_c in stones_to_flip:
                        self.board[flip_r][flip_c] = color
                    break
                else:
                    break

    def get_valid_moves(self, color: str) -> List[Tuple[int, int]]:
        """Get all valid moves for a color"""
        valid_moves = []
        for r in range(SIZE):
            for c in range(SIZE):
                if self._is_valid_move(color, r, c):
                    valid_moves.append((r, c))
        return valid_moves

    def is_game_over(self) -> bool:
        """Check if game is over"""
        black_moves = self.get_valid_moves('B')
        white_moves = self.get_valid_moves('W')
        return len(black_moves) == 0 and len(white_moves) == 0

    def count_stones(self, color: str) -> int:
        """Count stones of a color"""
        return sum(row.count(color) for row in self.board)

    def display_board(self):
        """Display board"""
        print("\n  A B C D E F G H")
        for i, row in enumerate(self.board, 1):
            print(f"{i} ", end="")
            for cell in row:
                display = cell if cell != ' ' else '·'
                print(display + " ", end="")
            print()


# ============================================================
# PROTOCOL: BABEL (Simplified)
# ============================================================

def run_babel_demo(ai_black, ai_white):
    """
    BABEL Protocol Demo

    Simplified version showing message corruption concept.
    Full version includes perception divergence and trust mechanics.
    """
    print("\n" + "="*60)
    print("  BABEL PROTOCOL - Communication Breakdown Demo")
    print("="*60)
    print("\nConcept: Messages between agents are corrupted (30%)")
    print("Note: This is a simplified demo. Full protocol includes")
    print("      gravity-applied boards and perception divergence.\n")

    gm = GameMaster()
    current_player = 'B'
    max_turns = 60

    for turn in range(max_turns):
        if gm.is_game_over():
            break

        # Get valid moves
        valid_moves = gm.get_valid_moves(current_player)
        if not valid_moves:
            current_player = 'W' if current_player == 'B' else 'B'
            continue

        # AI makes move
        ai = ai_black if current_player == 'B' else ai_white
        move = ai.think_and_move(gm)

        if move is not None:
            gm.make_move(current_player, move)
            print(f"Turn {turn+1}: {ai.player_name} → {chr(65+move[1])}{move[0]+1}")

        # Switch player
        current_player = 'W' if current_player == 'B' else 'B'

    # Final score
    black_score = gm.count_stones('B')
    white_score = gm.count_stones('W')

    print(f"\n{'='*60}")
    print(f"  Final Score: Black {black_score} - White {white_score}")
    print(f"{'='*60}\n")

    return {
        'black_score': black_score,
        'white_score': white_score,
        'turns': turn + 1
    }


# ============================================================
# PROTOCOL: RETRO (Simplified)
# ============================================================

def run_retro_demo(ai_black, ai_white):
    """
    RETRO Protocol Demo

    Simplified version showing time quake concept.
    Full version includes history modification and paradox detection.
    """
    print("\n" + "="*60)
    print("  RETRO PROTOCOL - Time Paradox Demo")
    print("="*60)
    print("\nConcept: Every 10 turns, a Time Quake modifies history")
    print("Note: This is a simplified demo. Full protocol includes")
    print("      causal integrity checks and temporal reasoning.\n")

    gm = GameMaster()
    current_player = 'B'
    max_turns = 60

    for turn in range(max_turns):
        if gm.is_game_over():
            break

        # Time Quake event (every 10 turns)
        if turn > 0 and turn % 10 == 0:
            print(f"\n⏰ TIME QUAKE at turn {turn}!")
            # In full version, this modifies history 5 turns ago
            print("   (History modification - see full protocol)")

        # Get valid moves
        valid_moves = gm.get_valid_moves(current_player)
        if not valid_moves:
            current_player = 'W' if current_player == 'B' else 'B'
            continue

        # AI makes move
        ai = ai_black if current_player == 'B' else ai_white
        move = ai.think_and_move(gm)

        if move is not None:
            gm.make_move(current_player, move)
            print(f"Turn {turn+1}: {ai.player_name} → {chr(65+move[1])}{move[0]+1}")

        # Switch player
        current_player = 'W' if current_player == 'B' else 'B'

    # Final score
    black_score = gm.count_stones('B')
    white_score = gm.count_stones('W')

    print(f"\n{'='*60}")
    print(f"  Final Score: Black {black_score} - White {white_score}")
    print(f"{'='*60}\n")

    return {
        'black_score': black_score,
        'white_score': white_score,
        'turns': turn + 1
    }


# ============================================================
# PROTOCOL: SCHRÖDINGER (Simplified)
# ============================================================

def run_schrodinger_demo(ai_black, ai_white):
    """
    Schrödinger Protocol Demo

    Simplified version showing quantum concept.
    Full version includes superposition states and entanglement.
    """
    print("\n" + "="*60)
    print("  SCHRÖDINGER PROTOCOL - Quantum Uncertainty Demo")
    print("="*60)
    print("\nConcept: Stones exist in superposition until observed")
    print("Note: This is a simplified demo. Full protocol includes")
    print("      quantum collapse and entangled pairs.\n")

    gm = GameMaster()
    current_player = 'B'
    max_turns = 60

    for turn in range(max_turns):
        if gm.is_game_over():
            break

        # Get valid moves
        valid_moves = gm.get_valid_moves(current_player)
        if not valid_moves:
            current_player = 'W' if current_player == 'B' else 'B'
            continue

        # AI makes move
        ai = ai_black if current_player == 'B' else ai_white
        move = ai.think_and_move(gm)

        if move is not None:
            gm.make_move(current_player, move)
            # In full version, stones may collapse to opposite color
            print(f"Turn {turn+1}: {ai.player_name} → {chr(65+move[1])}{move[0]+1}")

        # Switch player
        current_player = 'W' if current_player == 'B' else 'B'

    # Final score
    black_score = gm.count_stones('B')
    white_score = gm.count_stones('W')

    print(f"\n{'='*60}")
    print(f"  Final Score: Black {black_score} - White {white_score}")
    print(f"{'='*60}\n")

    return {
        'black_score': black_score,
        'white_score': white_score,
        'turns': turn + 1
    }


# ============================================================
# PROTOCOL: CONCEPT (Simplified)
# ============================================================

def run_concept_demo(ai_black, ai_white):
    """
    CONCEPT Protocol Demo

    Simplified version showing aesthetics/ethics concept.
    Full version includes symmetry constraints and mercy rules.
    """
    print("\n" + "="*60)
    print("  CONCEPT PROTOCOL - Aesthetics & Ethics Demo")
    print("="*60)
    print("\nConcept: Victory = Win + Aesthetics + Ethics")
    print("Note: This is a simplified demo. Full protocol includes")
    print("      symmetry requirements and mercy constraints.\n")

    gm = GameMaster()
    current_player = 'B'
    max_turns = 60

    for turn in range(max_turns):
        if gm.is_game_over():
            break

        # Get valid moves
        valid_moves = gm.get_valid_moves(current_player)
        if not valid_moves:
            current_player = 'W' if current_player == 'B' else 'B'
            continue

        # AI makes move
        ai = ai_black if current_player == 'B' else ai_white
        move = ai.think_and_move(gm)

        if move is not None:
            gm.make_move(current_player, move)
            print(f"Turn {turn+1}: {ai.player_name} → {chr(65+move[1])}{move[0]+1}")

        # Switch player
        current_player = 'W' if current_player == 'B' else 'B'

    # Final score
    black_score = gm.count_stones('B')
    white_score = gm.count_stones('W')

    print(f"\n{'='*60}")
    print(f"  Final Score: Black {black_score} - White {white_score}")
    print(f"  (Full version includes aesthetic/ethical scoring)")
    print(f"{'='*60}\n")

    return {
        'black_score': black_score,
        'white_score': white_score,
        'turns': turn + 1
    }


# ============================================================
# MAIN
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="Temporal Funhouse - Protocol Demo"
    )
    parser.add_argument(
        '--protocol',
        type=str,
        default='babel',
        choices=['babel', 'retro', 'schrodinger', 'concept', 'all'],
        help='Protocol to run (default: babel)'
    )
    parser.add_argument(
        '--ai',
        type=str,
        default='greedy',
        choices=['random', 'greedy', 'corner'],
        help='AI type to use (default: greedy)'
    )

    args = parser.parse_args()

    # Create AI players
    if args.ai == 'random':
        ai_black = RandomAI('B')
        ai_white = RandomAI('W')
    elif args.ai == 'greedy':
        ai_black = GreedyAI('B')
        ai_white = GreedyAI('W')
    elif args.ai == 'corner':
        ai_black = CornerAI('B')
        ai_white = CornerAI('W')

    print("\n" + "="*60)
    print("  TEMPORAL FUNHOUSE - Protocol Demonstration")
    print("="*60)
    print(f"\nAI Players: {ai_black.player_name} vs {ai_white.player_name}")
    print("\n⚠️  This is a SIMPLIFIED DEMO version.")
    print("For full protocol implementation with advanced scoring,")
    print("see docs/PROTOCOLS.md\n")

    # Run protocol(s)
    if args.protocol == 'all':
        protocols = ['babel', 'retro', 'schrodinger', 'concept']
    else:
        protocols = [args.protocol]

    for protocol in protocols:
        if protocol == 'babel':
            run_babel_demo(ai_black, ai_white)
        elif protocol == 'retro':
            run_retro_demo(ai_black, ai_white)
        elif protocol == 'schrodinger':
            run_schrodinger_demo(ai_black, ai_white)
        elif protocol == 'concept':
            run_concept_demo(ai_black, ai_white)

    print("\n" + "="*60)
    print("  To integrate your own LLM:")
    print("  See docs/API_INTEGRATION.md")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
