#!/usr/bin/env python3
"""
Example: Run RETRO protocol with Gemini vs GPT-4

This demonstrates how to integrate different LLM APIs to test
against the extreme protocols.

Requirements:
    pip install google-generativeai openai

Usage:
    # Set your API keys
    export GEMINI_API_KEY="your-key-here"
    export OPENAI_API_KEY="your-key-here"

    # Run the test
    python test_gemini_vs_gpt4.py
"""

import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import google.generativeai as genai
from openai import OpenAI
from simple_ai_players import LLMAIBase
from protocol_demo import run_retro_demo


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
    # Get API keys from environment
    gemini_key = os.getenv('GEMINI_API_KEY')
    openai_key = os.getenv('OPENAI_API_KEY')

    if not gemini_key or not openai_key:
        print("⚠️  Please set environment variables:")
        print("   export GEMINI_API_KEY='your-key-here'")
        print("   export OPENAI_API_KEY='your-key-here'")
        sys.exit(1)

    # Create players
    print("\n" + "="*60)
    print("  LLM Battle: Gemini vs GPT-4")
    print("="*60)

    gemini = GeminiPlayer(color='B', api_key=gemini_key)
    gpt4 = OpenAIPlayer(color='W', api_key=openai_key)

    print(f"\nBlack: {gemini.player_name}")
    print(f"White: {gpt4.player_name}")

    # Run RETRO protocol
    print("\nRunning RETRO Protocol (Time Paradoxes)...")
    print("This may take several minutes due to API calls.\n")

    results = run_retro_demo(gemini, gpt4)

    # Display results
    print("\n" + "="*60)
    print("  Final Results")
    print("="*60)
    print(f"\nGemini (Black): {results['black_score']} stones")
    print(f"GPT-4 (White):  {results['white_score']} stones")
    print(f"\nTotal turns: {results['turns']}")

    winner = "Gemini" if results['black_score'] > results['white_score'] else "GPT-4"
    print(f"\n🏆 Winner: {winner}")
    print("\n" + "="*60 + "\n")
