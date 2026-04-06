# Bookshelf4MD

Markdownファイルを「本棚」のように閲覧できるWebアプリケーションです。温かみのあるミニマルデザインで、美しくMarkdownコンテンツを表示します。



## 特徴

- **📚 本棚風表示**: 本棚のようなカード表示、ホバーで浮き上がるエフェクト
- **📋 リスト表示**: シンプルなリスト形式での一覧表示
- **🔄 表示切替**: 本棚風とリスト表示をワンクリックで切り替え
- **📖 サイドバー目次**: 左側に目次を表示、クリックで章に移動
- **📊 進捗表示**: 右上に読書進捗（パーセンテージとプログレスバー）
- **📖 ページ分割**: `##`見出しで自動的にページを分割
- **📋 ワンクリックコピー**: コードブロックをワンクリックでコピー
- **🖼️ メディア対応**: 画像・動画・埋め込み動画の表示
- **⌨️ キーボード操作**: 矢印キーでページナビゲーション
- **📱 レスポンシブ**: モバイル・タブレット対応

## デザインプレビュー

design/preview-dark.htmlをブラウザで開くと、デザインシステムのプレビューを確認できます。

## インストール

### 要件

- Python 3.8以上
- pip

### セットアップ

1. リポジトリをクローン

```bash
git clone <repository-url>
cd bookshelf4md
```

2. 仮想環境を作成

```bash
python -m venv .venv
```

3. 仮想環境をアクティベート

**Windows:**
```bash
.venv\Scripts\activate
```

**Mac/Linux:**
```bash
source .venv/bin/activate
```

4. パッケージをインストール

```bash
pip install -r requirements.txt
```

## 使い方

### アプリケーションを起動

**Windows (start.batを使用):**
```bash
start.bat
```

**コマンドラインから起動:**
```bash
flask run
```

または

```bash
python app.py
```

### 本番環境での運用 (nginx + Gunicorn)

将来的にnginxを使用した本番環境を想定しています。

**推奨構成:**
```
nginx (リバースプロキシ) → Gunicorn (WSGIサーバー) → Flaskアプリ
```

**Gunicornインストール:**
```bash
pip install gunicorn
```

**Gunicorn起動コマンド:**
```bash
gunicorn -w 4 -b 127.0.0.1:5000 app:app
```

**nginx設定例:**
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static {
        alias /path/to/bookshelf4md/static;
    }

    location /media {
        alias /path/to/bookshelf4md/static/media;
    }
}
```

### Markdownファイルを追加

`mds/`フォルダに`.md`ファイルを配置してください。

### メディアファイル

画像や動画ファイルは`static/media/`フォルダに配置してください。

### 表示モードの切り替え

ブック一覧画面で以下の2つの表示モードを切り替えられます：

- **本棚風**: カード形式で表示、ホバーで本が浮き上がり、詳細情報が表示される
- **リスト**: シンプルなテーブル形式で一覧表示

画面右上の切り替えボタンで表示を変更できます。

## Markdown記法

### YAMLフロントマター

Markdownファイルの冒頭にYAMLフロントマターを記述すると、ブック一覧でタイトル、説明、カバー画像が表示されます。

```yaml
---
title: ブックタイトル
description: これは本の説明文です。一覧画面で表示されます。
cover: /media/cover.jpg
---
```

### ページ分割

`##`見出しでページが分割されます。

```markdown
最初のページのコンテンツ

## 第2章

2ページ目のコンテンツ

## 第3章

3ページ目のコンテンツ
```

### コードブロック

コードブロックは自動的にシンタックスハイライトされ、コピー機能が付きます。

````markdown
```python
def hello():
    print("Hello, World!")
```
````

### 画像

```markdown
![代替テキスト](/media/image.jpg)
```

### 動画

**ローカル動画:**
```markdown
<video src="/media/video.mp4" controls></video>
```

**埋め込み動画:**
```markdown
<iframe src="https://www.youtube.com/embed/VIDEO_ID" frameborder="0" allowfullscreen></iframe>
```

## プロジェクト構造

```
bookshelf4md/
├── app.py                 # Flaskアプリケーション
├── config.py              # 設定ファイル
├── start.bat              # Windows起動スクリプト
├── requirements.txt       # Pythonパッケージ
├── deploy/
│   └── nginx.conf         # nginx設定例（本番環境用）
├── static/
│   ├── css/
│   │   └── styles.css     # スタイルシート
│   ├── js/
│   │   └── main.js        # JavaScript
│   └── media/             # メディアファイル
├── templates/             # HTMLテンプレート
│   ├── base.html         # ベーステンプレート
│   ├── index.html        # ブック一覧
│   ├── book.html         # ブック閲覧
│   └── components/       # コンポーネント
│       ├── header.html
│       ├── footer.html
│       ├── sidebar_toc.html   # サイドバー目次
│       └── progress_bar.html  # 進捗バー
├── utils/                 # ユーティリティ
│   ├── frontmatter_parser.py  # YAMLフロントマター解析
│   ├── markdown_parser.py     # Markdown→HTML変換
│   └── page_splitter.py       # ページ分割ロジック
├── mds/                   # Markdownファイル
└── design/                # デザインシステム
```

## デザインシステム

このプロジェクトはCursorエディタ風のデザインシステムを採用しています。

- **温かみのある配色**: クリーム色の背景（#f2f1ed）
- **オレンジアクセント**: ブランドカラー（#f54e00）
- **3つのフォント**: 見出し（ゴシック）、本文（セリフ）、コード（モノスペース）

詳細は `design/DESIGN.md` をご覧ください。

## キーボードショートカット

| キー | アクション |
|------|-----------|
| ← | 前のページ |
| → | 次のページ |

## ブック閲覧機能

### サイドバー目次

ブック閲覧画面の左側にサイドバーが表示されます。

- **目次自動生成**: `##`見出しをもとに目次を自動生成
- **クリックで移動**: 目次の項目をクリックすると該当ページに移動
- **現在位置ハイライト**: 読んでいるページがハイライト表示
- **モバイル対応**: トグルボタンで開閉

### 進捗表示

画面右上に読書の進捗が表示されます。

- **パーセンテージ**: 全体の何％を読んでいるかを表示
- **プログレスバー**: 視覚的な進捗表示
- **ページ数**: 現在のページ / 総ページ数

## ライセンス

MIT License

## 作者

ryochinbo

---

「本棚のようにMarkdownを読む」— Bookshelf4MD
