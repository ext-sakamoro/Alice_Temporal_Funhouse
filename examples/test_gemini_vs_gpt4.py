#!/usr/bin/env python3
"""
Example: Run RETRO protocol with AI players

This demonstrates how to test the extreme protocols with different AI implementations.

Usage (with LLM APIs - optional):
    # Install LLM libraries
    pip install google-generativeai openai

    # Set your API keys
    export GEMINI_API_KEY="your-key-here"
    export OPENAI_API_KEY="your-key-here"

    # Run the test
    python test_gemini_vs_gpt4.py

Usage (without APIs - runs locally):
    # Just run with Simple AI
    python test_gemini_vs_gpt4.py
"""

import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from simple_ai_players import GreedyAI, CornerAI, LLMAIBase
from protocol_demo import run_retro_demo

# Try to import LLM libraries (optional)
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class GeminiPlayer(LLMAIBase):
    """AI player using Google Gemini"""

    def __init__(self, color: str, api_key: str, model: str = "gemini-pro"):
        super().__init__(color, model)
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model)

    def _call_llm_api(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text


class OpenAIPlayer(LLMAIBase):
    """AI player using OpenAI GPT-4"""

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


if __name__ == "__main__":
    # Get API keys from environment (optional)
    gemini_key = os.getenv('GEMINI_API_KEY')
    openai_key = os.getenv('OPENAI_API_KEY')

    # Determine which players to use
    use_llm = False
    if gemini_key and openai_key and GEMINI_AVAILABLE and OPENAI_AVAILABLE:
        # Use LLM players if keys and libraries are available
        player_black = GeminiPlayer(color='B', api_key=gemini_key)
        player_white = OpenAIPlayer(color='W', api_key=openai_key)
        battle_name = "Gemini vs GPT-4"
        use_llm = True
    else:
        # Fallback to Simple AI (no API required)
        player_black = GreedyAI(color='B')
        player_white = CornerAI(color='W')
        battle_name = "GreedyAI vs CornerAI"

        print("\n" + "="*60)
        print("  ℹ️  Running in LOCAL MODE (no API required)")
        print("="*60)
        if not GEMINI_AVAILABLE or not OPENAI_AVAILABLE:
            print("\n💡 LLM libraries not installed.")
            print("   To use LLM mode, run:")
            print("   pip install google-generativeai openai")
        elif not gemini_key or not openai_key:
            print("\n💡 API keys not set.")
            print("   To use LLM mode, set environment variables:")
            print("   export GEMINI_API_KEY='your-key-here'")
            print("   export OPENAI_API_KEY='your-key-here'")
        print("\n   Using Simple AI instead (GreedyAI vs CornerAI)")
        print("="*60)

    # Run the battle
    print("\n" + "="*60)
    print(f"  AI Battle: {battle_name}")
    print("="*60)

    print(f"\nBlack: {player_black.player_name}")
    print(f"White: {player_white.player_name}")

    # Run RETRO protocol
    print("\nRunning RETRO Protocol (Time Paradoxes)...")
    if use_llm:
        print("This may take several minutes due to API calls.\n")
    else:
        print("This should complete quickly with local AI.\n")

    results = run_retro_demo(player_black, player_white)

    # Display results
    print("\n" + "="*60)
    print("  Final Results")
    print("="*60)
    print(f"\n{player_black.player_name}: {results['black_score']} stones")
    print(f"{player_white.player_name}: {results['white_score']} stones")
    print(f"\nTotal turns: {results['turns']}")

    winner = player_black.player_name if results['black_score'] > results['white_score'] else player_white.player_name
    print(f"\n🏆 Winner: {winner}")
    print("\n" + "="*60 + "\n")
