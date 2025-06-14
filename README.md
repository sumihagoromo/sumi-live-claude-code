# 🎵 Miku VTuber Landing Page 🎵

> **Claude Code で作成された VTuber ランディングページの実装サンプル**

[![Python](https://img.shields.io/badge/Python-3.12.4-blue.svg)](https://www.python.org/)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Powered-purple.svg)](https://claude.ai/code)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🎯 プロジェクトの目的

このプロジェクトは **Claude Code** を活用して構築された VTuber（バーチャルYouTuber）のランディングページです。主な目的は以下の通りです：

### 主要目標
- **Claude Code の実践活用**: AI アシスタントによる効率的な開発プロセスの実現
- **Web開発スキルの向上**: HTML/CSS/Pythonを組み合わせたフルスタック開発の学習
- **VTuberブランディング**: 魅力的なランディングページによるファン獲得
- **技術実験**: 最新のAI支援開発ツールの検証と評価

## 🚀 Claude Code について

### Claude Code とは
[Claude Code](https://claude.ai/code) は Anthropic が提供する AI アシスタント開発ツールです。

### 基本コマンド
```bash
# Claude Code 起動
claude

# ヘルプ表示
/help

# メモリ機能の活用
/memory

# モデル設定
/model
```

### 活用メリット
- **コード生成支援**: 高品質なコードの自動生成
- **デバッグサポート**: エラーの迅速な特定と修正
- **学習促進**: ベストプラクティスの提案と説明
- **効率化**: 開発時間の大幅な短縮

## 🎮 クイックスタート

### 1. サーバー起動
```bash
python vtuber_server.py
```

### 2. ブラウザでアクセス
```
http://localhost:8000
```

### 3. 機能一覧
- ランディングページの表示
- レスポンシブデザイン
- インタラクティブな要素
- VTuberプロフィール表示

### トラブルシューティング
```bash
# ポート使用状況確認
lsof -i :8000
kill <プロセスID>

# サーバー再起動
python vtuber_server.py
```

## 📁 プロジェクト構成

```
sumi-live-claude-code/
├── README.md              # プロジェクト説明書（このファイル）
├── CLAUDE.md              # Claude Code 向け指示書
├── vtuber_server.py       # Python HTTP サーバー
├── static/                # 静的ファイル
│   ├── index.html         # メイン HTML ファイル
│   └── style.css          # CSS スタイルシート
└── claude-env/            # Python 仮想環境
```

### ファイル詳細

#### `vtuber_server.py`
- Python 標準ライブラリを使用した軽量 HTTP サーバー
- ポート 8000 でファイルサーバーを提供
- 静的ファイルの配信に特化

#### `static/index.html`
- VTuber のランディングページ本体
- レスポンシブデザイン対応
- モダンな UI コンポーネント

#### `static/style.css`
- 美しいビジュアルデザイン
- アニメーション効果
- CSS Grid/Flexbox 活用

#### `CLAUDE.md`
- Claude Code 向けの開発指示
- プロジェクト環境の説明
- 開発ワークフロー

## 🛠 開発ガイド

### UI/UX 改善点
- **ビジュアル強化**: アニメーション効果の追加
- **ユーザビリティ**: ナビゲーションの改善
- **パフォーマンス**: 読み込み速度の最適化
- **アクセシビリティ**: CSS でのインクルーシブデザイン

### コンテンツ拡張
- **プロフィール詳細**: VTuber の詳細情報
- **メディアギャラリー**: 画像・動画ギャラリー
- **SNS 連携**: YouTube、Twitter、Discord など
- **ファン機能**: コメント機能・投げ銭など

## 🔧 技術スタック

| 技術 | 用途 | バージョン |
|------|------|------------|
| ![Python](https://img.shields.io/badge/Python-FFD43B?style=flat&logo=python&logoColor=blue) | サーバーサイド | 3.12.4 |
| ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white) | マークアップ | HTML5 |
| ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white) | スタイリング | CSS3 |
| ![Claude](https://img.shields.io/badge/Claude%20Code-8A2BE2?style=flat&logo=anthropic&logoColor=white) | 開発支援 | Latest |

## 🎓 学習効果

このプロジェクトから得られる学習効果：

### Claude Code 活用
- AI アシスタントとの効果的な協働
- プロンプトエンジニアリング
- コード生成とレビュー

### Web 開発
- Python HTTP サーバーの構築
- レスポンシブデザインの実装
- CSS アニメーションの活用

### プロジェクト管理
- ファイル構成の設計
- ドキュメンテーション
- バージョン管理

## 🚧 開発手順

### 開発フロー
1. **企画**: VTuber ランディングページの要件定義
2. **設計**: ファイル構成と技術選定
3. **UI作成**: HTML/CSS によるビジュアル構築
4. **サーバー実装**: Python による HTTP サーバー
5. **統合テスト**: 全体動作の確認
6. **ドキュメント作成**: README.md の整備

### 開発時の注意点
- **ポート競合**: `OSError: [Errno 48] Address already in use`
  - **解決法**: `lsof -i :8000` で確認後 `kill` で終了

## 🎉 今後の発展可能性

このプロジェクトは以下の方向性で発展可能です：

### 短期目標
- ユーザーインタラクションの追加
- パフォーマンスとUXの向上

### 長期目標
- データベース連携
- リアルタイム配信機能の統合

### 技術的成長
1. このプロジェクトでの実験
2. 開発スキルの向上
3. Claude Code による効率化
4. 最新技術トレンドの習得

## 📄 ライセンス

MIT License - 詳細は [LICENSE](LICENSE) ファイルを参照してください。

## 📞 サポート・お問い合わせ

質問やフィードバックがありましたら：

- **Issue**: GitHub Issues で報告
- **Email**: プロジェクト管理者まで
- **Claude Code**: `/help` コマンドでサポート

---

<div align="center">

**🎵 Made with ❤️ using Claude Code 🎵**

[![Claude Code](https://img.shields.io/badge/Powered%20by-Claude%20Code-purple?style=for-the-badge&logo=anthropic)](https://claude.ai/code)

</div>