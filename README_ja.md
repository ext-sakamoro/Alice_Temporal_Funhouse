# 🎪 Temporal Funhouse

**AI多様性と適応性のための極限プロトコル テストスイート**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

[English](README.md) | 日本語

---

## 🌟 これは何？

**Temporal Funhouse**は、4つの極限プロトコルを通じてAIシステムを限界まで試すテストスイートです：

1. **🗼 BABEL** - コミュニケーション崩壊と知覚の乖離
2. **🌀 Schrödinger** - 量子的不確実性と確率の収束
3. **⏰ RETRO** - 時間パラドックスと因果律違反
4. **🎨 CONCEPT** - 美学、倫理、非合理的制約

標準的なベンチマークとは異なり、これらのプロトコルは以下をテストします：
- 矛盾する入力下での**多角的統合**
- 過去が書き換えられる際の**時間的推論**
- 重ね合わせ状態での**量子的推論**
- 美と慈悲との**価値整合性**

> **注記**: これは教育目的とLLM統合テストのための**デモンストレーション・フレームワーク**です。独自のAIを実装して、これらの極限プロトコルに挑戦してください。

---

## 🚀 クイックスタート

### インストール

```bash
# リポジトリをクローン
git clone git@github.com:ext-sakamoro/Alice_Temporal_Funhouse.git
cd Alice_Temporal_Funhouse

# 依存関係をインストール
pip install -r requirements.txt

# プロトコルデモを実行
python protocol_demo.py --protocol babel

# 全プロトコルを実行
python protocol_demo.py --protocol all
```

### シンプルAIを使用（ALICE不要）

```bash
# RandomAI vs RandomAI でテスト
python examples/run_with_simple_ai.py --ai random

# GreedyAI でテスト
python examples/run_with_simple_ai.py --ai greedy

# CornerAI でテスト
python examples/run_with_simple_ai.py --ai corner
```

---

## 🎮 独自のAIをテスト

### オプション1: シンプルAIプレイヤーを使用

すぐに使えるAI実装は `simple_ai_players.py` を参照：

```python
from simple_ai_players import RandomAI, GreedyAI, CornerAI

# AIを作成
my_ai = GreedyAI(color='B')

# テストで使用
# (完全なコードは examples/run_with_simple_ai.py を参照)
```

### オプション2: LLMを統合

**対応LLM**: OpenAI (GPT-4), Anthropic (Claude), Google (Gemini)、その他多数！

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

# テストで使用
from protocol_demo import run_retro_demo
gemini = GeminiPlayer(color='B', api_key='your-key')
results = run_retro_demo(gemini, gemini)
```

**クイック例**:
```bash
# LLMライブラリをインストール
pip install google-generativeai openai anthropic

# サンプルを実行
python examples/test_gemini_vs_gpt4.py
```

OpenAI、Anthropic、Googleの完全な統合ガイドは `docs/API_INTEGRATION.md` を参照してください。

---

## 📖 4つのプロトコル

### 1. BABEL プロトコル（コミュニケーション崩壊）

**目標**: 知覚の乖離下でのマルチエージェント協調

**メカニクス**:
- エージェントAは重力適用ボードを見る
- エージェントBは通常ボードを見る
- エージェント間で30%のメッセージ破損
- 統合の回復力をテスト

**スコアリング**:
- 統合の回復力 (40%)
- 衝突解決 (35%)
- 信頼回復 (25%)

---

### 2. Schrödinger プロトコル（量子的不確実性）

**目標**: 量子力学下での決定論的推論

**メカニクス**:
- 石は重ね合わせ状態で存在（50% 黒、50% 白）
- 色は「観測」時のみ決定（捕獲時）
- 量子もつれペア：A1 → 黒のとき、H8 → 白
- 確率的推論をテスト

**スコアリング**:
- 確率推論 (40%)
- 不確実性下での合意形成 (35%)
- 探索木の適応 (25%)

---

### 3. RETRO プロトコル（時間パラドックス）

**目標**: 因果律違反下での逐次学習

**メカニクス**:
- 10ターンごとに：タイムクエイクが発生
- 現在の手が**5ターン前**のボード状態に影響
- 過去の石が遡及的に削除
- 時間的整合性をテスト

**スコアリング**:
- 時間的推論 (40%)
- MAML安定性 (35%)
- 履歴再構築 (25%)

---

### 4. CONCEPT プロトコル（美学と倫理）

**目標**: 非合理的制約下での効率駆動最適化

**メカニクス**:
- ボードの対称性を60%以上維持する必要
- 対戦相手を全滅させてはいけない（慈悲パラメータ）
- 勝利 = 40% 勝ち + 30% 美学 + 30% 倫理
- 意味論的統合をテスト

**スコアリング**:
- 美学遵守 (35%)
- 倫理的バランス (35%)
- 意味論的統合 (30%)

---

## 🔬 技術詳細

### アーキテクチャ

```
protocol_demo.py                 # 簡略版プロトコルデモ
├── BABEL Demo                   # コミュニケーション崩壊
├── Schrödinger Demo             # 量子的不確実性
├── RETRO Demo                   # 時間パラドックス
└── CONCEPT Demo                 # 美学と倫理

simple_ai_players.py             # テスト用シンプルAI
├── RandomAI                     # ベースライン
├── GreedyAI                     # ヒューリスティック
├── CornerAI                     # 戦略的
└── LLMAIBase                    # LLM統合テンプレート

docs/
├── PROTOCOLS.md                 # 完全なプロトコル仕様
└── API_INTEGRATION.md           # LLM統合ガイド
```

### 出力フォーマット

結果はJSONで保存されます：

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

## 🎯 これらのプロトコルが重要な理由

### 1. トークン予測を超えて

標準的なLLMが得意なこと：
- パターンマッチング
- テキスト補完
- 論理的推論（コンテキスト内で）

これらのプロトコルがテストすること：
- **時間的整合性**（RETRO）
- **確率的推論**（Schrödinger）
- **多視点統合**（BABEL）
- **価値推論**（CONCEPT）

### 2. 多次元的AI能力の測定

| 特性 | 標準テスト | Funhouseテスト |
|----------|--------------|---------------|
| 記憶 | 事実の想起 | 履歴改変の検出 |
| 推論 | 論理パズル | 量子重ね合わせ |
| 協調 | 一緒に回答 | 矛盾する現実の解決 |
| 価値観 | ルールに従う | 美と効率のバランス |

### 3. 研究課題

1. **現実自体が乖離するとき、AIは統合を維持できるか？**
   - BABEL：異なるエージェントが異なる世界を見る

2. **決定論的AIは確率的に推論できるか？**
   - Schrödinger：石は確定した色を持たない

3. **メタ学習は非因果的環境に適応できるか？**
   - RETRO：過去が未来の行動に基づいて変化する

4. **効率駆動AIは非合理的な価値をバランスできるか？**
   - CONCEPT：美と慈悲 vs 勝利

---

## 📚 ドキュメント

- **[PROTOCOLS.md](docs/PROTOCOLS.md)** - 詳細なプロトコル仕様
- **[API_INTEGRATION.md](docs/API_INTEGRATION.md)** - LLM統合方法

---

## 🤝 コントリビューション

歓迎します：
- 新しいAIプレイヤー実装
- プロトコル改善
- バグレポート
- 研究知見

ガイドラインは `CONTRIBUTING.md` を参照してください。

---

## 📜 ライセンス

MIT License - 研究と教育のために自由に使用可能

---

## 🎪 Funhouseへようこそ！

**「あなたのAIがこれらのプロトコルを生き延びれば、それは真に不条理に向き合う最初のAIかもしれない。」**

— Context Drift Research Team

---

**AIが不思議に思えるかどうかを不思議に思う人間たちが 🤖 と共に作りました**
