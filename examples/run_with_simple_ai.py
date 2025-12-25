#!/usr/bin/env python3
"""
Example: Run Extreme Protocols with Simple AI Players

This demonstrates how to test the protocols without the full ALICE system.
Perfect for:
- Quick testing
- Baseline comparisons
- Educational purposes
"""

import sys
import os
import argparse

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from simple_ai_players import RandomAI, GreedyAI, CornerAI


def run_simple_test(ai_type='random', protocol='all'):
    """Run protocols with simple AI players"""

    print(f"\n{'='*60}")
    print(f"  Running {protocol.upper()} Protocol with {ai_type.upper()}AI")
    print(f"{'='*60}\n")

    # Create AI players based on type
    if ai_type == 'random':
        ai_black = RandomAI('B')
        ai_white = RandomAI('W')
    elif ai_type == 'greedy':
        ai_black = GreedyAI('B')
        ai_white = GreedyAI('W')
    elif ai_type == 'corner':
        ai_black = CornerAI('B')
        ai_white = CornerAI('W')
    else:
        print(f"Unknown AI type: {ai_type}")
        print("Available: random, greedy, corner")
        return

    print(f"Black: {ai_black.player_name}")
    print(f"White: {ai_white.player_name}")
    print()

    # Note: To actually run protocols, you would need to:
    # 1. Import the protocol runner from alice_temporal_funhouse.py
    # 2. Modify it to accept simple AI players
    # 3. Or create a simplified version for simple AI

    print("⚠️  Note: This is a template example.")
    print("To run actual protocols, you need to:")
    print("1. Modify alice_temporal_funhouse.py to accept SimpleAI")
    print("2. Or use the full ALICE system")
    print("\nFor now, this demonstrates AI player creation.")
    print(f"\n{ai_black.player_name} and {ai_white.player_name} are ready!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run Extreme Protocols with Simple AI"
    )
    parser.add_argument(
        '--ai',
        type=str,
        default='random',
        choices=['random', 'greedy', 'corner'],
        help='AI type to use (default: random)'
    )
    parser.add_argument(
        '--protocol',
        type=str,
        default='all',
        choices=['babel', 'schrodinger', 'retro', 'concept', 'all'],
        help='Protocol to run (default: all)'
    )

    args = parser.parse_args()
    run_simple_test(args.ai, args.protocol)
