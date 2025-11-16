# 「ランキング設計からはじめるスポーツデータ分析 ―― MATLABであなたも予測できる」をMATLABではなくてpythonを使って学ぶ試み

このプロジェクトは、MATLABで書かれた書籍「ランキング設計からはじめるスポーツデータ分析 ―― MATLABであなたも予測できる」をPythonで実装・学習するためのリポジトリです。

## プロジェクト概要

「ランキング設計からはじめるスポーツデータ分析 ―― MATLABであなたも予測できる」の内容を確認して、ランキング設計や予測モデルの構築をPythonで実装します。

## セットアップ

### 必要な環境

- Python 3.11以上
- uv（パッケージマネージャー）

### インストール

```bash
# 依存関係のインストール
uv sync
```

### 主な依存パッケージ

- `pandas`: データ分析
- `matplotlib`: 可視化
- `openpyxl`: Excelファイルの読み書き
- `japanize-matplotlib`: 日本語フォント対応

## プロジェクト構造

```
rank-sports-data-project/
├── data/                    # データファイル
│   ├── archive/            # 国際サッカー結果データ（Kaggle）
│   ├── FisherIris/         # Fisher's Irisデータセット
│   └── *.xlsx, *.csv       # 各種スポーツデータ（NBA、NFL、Jリーグなど）
├── figure/                  # 生成されたグラフ・図
├── main.py                  # メインエントリーポイント
├── nba_results.py          # NBAデータの読み込み・表示
├── smallDataExample.py     # 小規模データの分析例（勝敗集計・可視化）
└── pyproject.toml          # プロジェクト設定・依存関係
```

## データについて

### データファイル

- **NBA**: `NBAResults*.xlsx`（2000-2019シーズン）
- **NFL**: `NFLResults20232024.xlsx`
- **Jリーグ**: `JLeagueResults.xlsx`
- **UEFA CL**: `UEFACL202425.xlsx`
- **その他**: 各種サッカー・スポーツデータ

## 今後の予定

書籍の内容に沿って、以下のような分析を実装予定：

- ランキングシステムの実装
- 予測モデルの構築
- 各種統計手法の適用
