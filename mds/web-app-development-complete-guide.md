---
title: Webアプリケーション開発完全ガイド
description: Bookshelf4MDのコード完全解説
cover: /media_mds/media_web-app-development-complete-guide/image.png
---

# Webアプリケーション開発完全ガイド

Webアプリケーションをゼロから作るために必要な知識を学びます。

## 本教材で学べること

- Pythonを使ったバックエンド開発
- FlaskフレームワークによるWebアプリケーション構築
- HTML/CSS/JavaScriptによるフロントエンド開発
- 実際の動くアプリケーションのコードリーディング
- 自分でアプリケーションを作るための基礎知識

## Webアプリケーションの仕組み

### クライアントとサーバー

Webアプリケーションは、大きく分けて2つの部分で構成されています。

**クライアント（フロントエンド）**
- ユーザーが見ている画面
- ブラウザ（Chrome、Firefoxなど）で動作
- HTML/CSS/JavaScriptで構成

**サーバー（バックエンド）**
- データを処理する部分
- サーバー上で動作
- Python/Java/Rubyなどで構成

```
ユーザー
  ↓ (リクエスト)
Webサーバー (Nginx)
  ↓
バックエンド (Flask/Python)
  ↓ (レスポンス)
フロントエンド (HTML/CSS/JS)
  ↓
ユーザーの画面に表示
```

### バックエンドの役割

- データの処理・保存・取得
- ユーザー認証
- ビジネスロジックの実行
- APIの提供

### フロントエンドの役割

- 画面の表示
- ユーザー操作の受け付け
- データの表示
- アニメーション・視覚効果

## 本教材で使う技術

| 技術 | 用途 | 説明 |
|------|------|------|
| Python | バックエンド言語 | 学びやすく実用的 |
| Flask | Webフレームワーク | 最小限のコードでWebアプリ構築 |
| HTML | 構造 | 画面の骨組み |
| CSS | デザイン | 見た目の装飾 |
| JavaScript | インタラクション | 動きのある機能 |
| Markdown | ドキュメント | 技術書の記述 |

## 学習の進め方

1. 各章を順番に読む
2. コード例を実際に書いてみる
3. 動作を確認する
4. 演習問題に挑戦する
5. 理解できない箇所は実際にコードを変更して実験する

---

## 開発環境のセットアップ

プログラミングを始める前に、開発環境を整えます。

### Pythonのインストール

**Windowsの場合**

1. [Python公式サイト](https://www.python.org/downloads/)にアクセス
2. 「Download Python」ボタンをクリック
3. インストーラーを起動し、「Add Python to PATH」にチェックを入れる
4. 「Install Now」をクリック

**インストール確認**

コマンドプロンプトまたはPowerShellを開き、以下を実行：

```bash
python --version
```

`Python 3.x.x` と表示されれば成功です。

### 仮想環境の作成

Pythonプロジェクトごとに独立した環境を作ります。

**仮想環境を作成**

プロジェクトフォルダで以下を実行：

```bash
python -m venv .venv
```

**仮想環境のアクティベート**

**Windows (PowerShell):**
```bash
.venv\Scripts\Activate.ps1
```

**Windows (コマンドプロンプト):**
```bash
.venv\Scripts\activate.bat
```

プロンプトの先頭に `(.venv)` が表示されれば成功です。

**仮想環境の終了**

```bash
deactivate
```

### 必要なパッケージのインストール

**requirements.txt の使い方**

プロジェクトで必要なパッケージを一括管理するファイルです。

```txt
Flask==3.0.0
markdown==3.5.1
Pygments==2.17.2
PyYAML==6.0.1
```

**インストール方法**

```bash
pip install -r requirements.txt
```

**インストール済みパッケージの確認**

```bash
pip list
```

### コードエディタの選択

**推奨エディタ**

| エディタ | 特徴 |
|----------|------|
| VS Code | 無料、拡張機能豊富、シンタックスハイライト |
| PyCharm | Python開発に特化、有料版あり |
| Notepad++ | 軽量、Windowsに最適 |

**VS Codeの推奨拡張機能**

- Python
- Python Docstring Generator
- Pylance
- Live Server

### プロジェクトのフォルダ構造

```
bookshelf4md/
├── .venv/              # 仮想環境
├── app.py              # メインアプリケーション
├── config.py           # 設定ファイル
├── requirements.txt    # パッケージリスト
├── static/             # 静的ファイル（CSS/JS）
├── templates/          # HTMLテンプレート
├── utils/              # ユーティリティモジュール
└── mds/                # Markdownファイル
```

### Gitの基本

**Gitのインストール**

[Git公式サイト](https://git-scm.com/)からダウンロード・インストール

**基本コマンド**

```bash
git init              # リポジトリの初期化
git add .              # 変更をステージング
git commit -m "メッセージ"  # コミット
git status             # 状態確認
```

---

## Pythonの基礎

プログラミングの基本を学びます。

### 変数とデータ型

**変数の定義**

```python
# 変数に値を代入
message = "Hello, World!"
count = 42
price = 19.99
is_active = True

# 確認
print(message)  # Hello, World!
print(count)     # 42
```

**主なデータ型**

| 型 | 説明 | 例 |
|----|------|------|
| `str` | 文字列 | `"hello"` |
| `int` | 整数 | `42` |
| `float` | 浮動小数点 | `3.14` |
| `bool` | 真偽値 | `True`, `False` |
| `list` | リスト | `[1, 2, 3]` |
| `dict` | 辞書 | `{"key": "value"}` |
| `None` | 何もない | `None` |

**文字列の操作**

```python
# 文字列結合
name = "太郎"
greeting = "こんにちは、" + name + "さん"
print(greeting)  # こんにちは、太郎さん

# 文字列のフォーマット
name = "花子"
age = 25
message = f"{name}さんは{age}歳です"
print(message)  # 花子さんは25歳です
```

**リストの操作**

```python
# リストの作成
fruits = ["りんご", "バナナ", "オレンジ"]

# 要素の取得
print(fruits[0])  # りんご

# 要素の追加
fruits.append("ぶどう")

# 要素数
print(len(fruits))  # 4

# 繰り返し
for fruit in fruits:
    print(f"私は{fruit}が好きです")
```

**辞書の操作**

```python
# 辞書の作成
person = {
    "name": "一郎",
    "age": 30,
    "city": "東京"
}

# 値の取得
print(person["name"])  # 一郎
print(person.get("age"))  # 30

# キーと値の追加
person["job"] = "エンジニア"
```

### 制御構文

**if文**

```python
score = 75

if score >= 80:
    print("素晴らしい！")
elif score >= 60:
    print("合格です")
else:
    print("もう少し頑張りましょう")
```

**for文**

```python
# 0から4まで繰り返す
for i in range(5):
    print(f"現在の数字: {i}")

# リストの要素を処理
names = ["太郎", "花子", "次郎"]
for name in names:
    print(f"{name}さん、こんにちは！")
```

**while文**

```python
count = 0
while count < 5:
    print(f"カウント: {count}")
    count += 1
```

### 関数

**関数の定義**

```python
def greet(name):
    """挨拶を返す関数"""
    return f"こんにちは、{name}さん！"

# 呼び出し
message = greet("太郎")
print(message)  # こんにちは、太郎さん！
```

**複数の戻り値**

```python
def divide(a, b):
    """割り算を行う関数"""
    if b == 0:
        return None, "0で割ることはできません"
    return a / b, "成功"

result, message = divide(10, 2)
print(f"結果: {result}, メッセージ: {message}")
```

**デフォルト引数**

```python
def introduce(name, age=20):
    """自己紹介をする関数"""
    return f"{name}さん、{age}歳です"

print(introduce("太郎"))           # 太郎さん、20歳です
print(introduce("花子", 25))       # 花子さん、25歳です
```

### クラス

**クラスの定義**

```python
class Person:
    def __init__(self, name, age):
        """初期化メソッド"""
        self.name = name
        self.age = age

    def greet(self):
        """挨拶メソッド"""
        return f"{self.name}です、{self.age}歳です"

    def have_birthday(self):
        """年齢を増やすメソッド"""
        self.age += 1

# インスタンス作成
person = Person("太郎", 30)
print(person.greet())  # 太郎です、30歳です
person.have_birthday()
print(person.age)  # 31
```

### ファイル操作

**ファイルの読み込み**

```python
# ファイルを開いて読み込み
with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

**ファイルへの書き込み**

```python
# ファイルに書き込み
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!\n")
```

### 例外処理

```python
try:
    # 0で割る処理
    result = 10 / 0
except ZeroDivisionError:
    print("0で割ることはできません")
finally:
    print("処理を終了します")
```

---

## Flaskでバックエンド開発

Flaskフレームワークを使って、Webアプリケーションのバックエンドを作ります。

### Flaskとは

FlaskはPythonのWebフレームワークです。最小限のコードでWebアプリケーションを作成できます。

**Flaskの特徴**

- 軽量でシンプル
- 拡張性が高い
- ドキュメントが豊富
- 大規模なプロダクションでも使用可能

### app.py 完全解説

**インポート文**

```python
import os  # OSモジュール：ファイルパス操作などに使用
from pathlib import Path  # パス操作：オブジェクト指向でパスを扱う
from flask import Flask, render_template, send_from_directory, jsonify, request
# Flask: Webフレームワーク
# render_template: HTMLテンプレートをレンダリング
# send_from_directory: 静的ファイルを配信
# jsonify: JSONレスポンスを返す
# request: クライアントからのリクエスト情報を取得
from werkzeug.middleware.proxy_fix import ProxyFix  # nginx対応：プロキシ経由のアクセスを正しく処理
import config  # 設定ファイル：定数を一元管理
```

**Flaskアプリケーションの初期化**

```python
app = Flask(__name__,
            static_folder=str(config.STATIC_FOLDER),  # 静的ファイルのフォルダパス
            template_folder=str(config.TEMPLATE_FOLDER))  # テンプレートのフォルダパス

# __name__: 現在のモジュール名を指定（Flaskがリソースを見つけるために必要）
# static_folder: CSS/JSファイルの場所
# template_folder: HTMLテンプレートの場所
```

**nginx対応（ProxyFix）**

```python
# nginx対応：ProxyFixミドルウェア
app.wsgi_app = ProxyFix(
    app.wsgi_app,  # FlaskのWSGIアプリケーション
    x_for=config.PROXY_FIX_COUNT,  # X-Forwarded-Forヘッダーの処理回数
    x_proto=config.PROXY_FIX_COUNT,  # X-Forwarded-Protoヘッダーの処理回数
    x_host=config.PROXY_FIX_COUNT,  # X-Forwarded-Hostヘッダーの処理回数
    x_prefix=config.PROXY_FIX_COUNT  # X-Forwarded-Prefixヘッダーの処理回数
)

# nginxをリバースプロキシとして使う場合、クライアントの本来のIPアドレスなどを
# 正しく取得するために必要
```

**設定の読み込み**

```python
app.config.from_object(config)
# configモジュールから設定を読み込み
# SECRET_KEY, DEBUGなどの設定値が適用される
```

**ディレクトリの作成**

```python
# ディレクトリが存在しない場合は作成
config.MARKDOWN_DIR.mkdir(exist_ok=True)  # Markdownファイル用ディレクトリ
config.MEDIA_DIR.mkdir(parents=True, exist_ok=True)  # メディアファイル用ディレクトリ

# exist_ok=True: 既に存在する場合でもエラーにしない
# parents=True: 親ディレクトリも同時に作成
```

**ユーティリティの初期化**

```python
# ユーティリティをインポート
from utils.frontmatter_parser import FrontmatterParser  # YAMLフロントマター解析
from utils.page_splitter import PageSplitter  # ページ分割処理
from utils.markdown_parser import MarkdownParser  # Markdown→HTML変換

# 各クラスのインスタンスを作成
frontmatter_parser = FrontmatterParser()  # パーサーインスタンス
page_splitter = PageSplitter()  # スプリッターインスタンス
markdown_parser = MarkdownParser()  # パーサーインスタンス
```

### ルーティングの仕組み

**ルーティングとは**

URLと関数を紐付ける仕組みです。

```python
@app.route('/')  # ルート定義：ルートとURLパターン
def index():  # ビュー関数：リクエストがあったときに実行される関数
    """ブックシェフ一覧ページ"""
    view_mode = request.cookies.get('view_mode', 'shelf')  # クッキーから表示モードを取得
    books = get_markdown_files()  # ブック一覧を取得
    return render_template('index.html', books=books, view_mode=view_mode)
    # HTMLテンプレートをレンダリングして返す
```

**URLパラメータの受け取り**

```python
@app.route('/book/<filename>')  # パスパラメータ：filenameに何かが入る
@app.route('/book/<filename>/page/<int:page_num>')  # 複数のパラメータ：page_numは整数
def view_book(filename, page_num=1):  # パラメータを関数の引数で受け取る
    """ブック詳細ページ"""
    # filename: URLから取得したファイル名
    # page_num: ページ番号（デフォルト値は1）
```

**レスポンスの返し方**

| メソッド | 説明 | 使用例 |
|---------|------|--------|
| `render_template()` | HTMLを返す | ページ表示 |
| `jsonify()` | JSONを返す | APIレスポンス |
| `send_from_directory()` | ファイルを返す | 画像・CSS/JS配信 |

---

## ユーティリティモジュール詳解

コードを機能別に分割して、再利用しやすくします。

### config.py 完全解説

```python
import os
from pathlib import Path

# ベースディレクトリ：現在のファイルの場所を基準
BASE_DIR = Path(__file__).resolve().parent

# Flask設定
SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
# SECRET_KEY: セッション暗号化に使用（本番環境では環境変数で設定）
DEBUG = os.environ.get('FLASK_DEBUG', 'True') == 'True'
# DEBUG: デバッグモード（Trueならエラー詳細表示）

# ディレクトリ設定
MARKDOWN_DIR = BASE_DIR / 'mds'  # Markdownファイルの格納場所
MEDIA_DIR = BASE_DIR / 'static' / 'media'  # メディアファイルの格納場所
STATIC_FOLDER = BASE_DIR / 'static'  # 静的ファイルの場所
TEMPLATE_FOLDER = BASE_DIR / 'templates'  # テンプレートの場所

# URL設定
APPLICATION_ROOT = '/'  # アプリケーションのルートパス
PREFERRED_URL_SCHEME = 'http'  # 優先するURLスキーム

# セッション設定
SESSION_COOKIE_SECURE = False  # HTTPS時はTrueに
SESSION_COOKIE_HTTPONLY = True  # JavaScriptからのアクセスを禁止
SESSION_COOKIE_SAMESITE = 'Lax'  # クロスサイトリクエスト制御

# ファイルアップロード設定
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB：アップロード上限

# nginx対応（ProxyFix用）
PROXY_FIX_COUNT = 1  # nginxのプロキシ階層数に合わせて調整
```

### utils/frontmatter_parser.py 完全解説

```python
import re
import yaml

class FrontmatterParser:
    """YAMLフロントマターを解析するクラス"""

    def __init__(self):
        # ---で囲まれた部分をマッチする正規表現
        # re.DOTALL: .が改行にもマッチする
        self.pattern = re.compile(r'^---\s*\n(.*?)\n---\s*\n(.*)$', re.DOTALL)

    def parse(self, content):
        """
        Markdownコンテンツからフロントマターを解析

        Args:
            content: Markdownファイルの内容

        Returns:
            dict: {'frontmatter': dict, 'content': str}
        """
        match = self.pattern.match(content)  # パターンにマッチさせる

        if match:  # マッチした場合
            yaml_text, markdown_content = match.groups()  # キャプチャグループを取得
            try:
                frontmatter = yaml.safe_load(yaml_text) or {}  # YAMLをパース
            except yaml.YAMLError:
                frontmatter = {}  # パース失敗時は空辞書
            return {
                'frontmatter': frontmatter,  # フロントマターの辞書
                'content': markdown_content.strip(),  # Markdown本体
                'has_frontmatter': True  # フロントマターあり
            }

        # マッチしない場合（フロントマターなし）
        return {
            'frontmatter': {},
            'content': content.strip(),
            'has_frontmatter': False
        }

    def get_title(self, parsed_data, default=None):
        """フロントマターからタイトルを取得"""
        return parsed_data['frontmatter'].get('title', default)

    def get_description(self, parsed_data, default=''):
        """フロントマターから説明を取得"""
        return parsed_data['frontmatter'].get('description', default)

    def get_cover(self, parsed_data, default=None):
        """フロントマターからカバー画像を取得"""
        return parsed_data['frontmatter'].get('cover', default)
```

### utils/page_splitter.py 完全解説

```python
import re
from .frontmatter_parser import FrontmatterParser

class PageSplitter:
    """Markdownを##見出しでページ分割するクラス"""

    def __init__(self):
        # ##で始まる見出しをマッチする正規表現
        # ^: 行頭、$: 行末、\s+: 空白文字
        self.heading_pattern = re.compile(r'^##\s+(.+)$', re.MULTILINE)
        self.frontmatter_parser = FrontmatterParser()

    def split(self, content):
        """
        Markdownコンテンツを##見出しで分割

        Returns:
            dict: {'pages': list, 'toc': list, 'total_pages': int}
        """
        # フロントマターを解析
        parsed = self.frontmatter_parser.parse(content)
        markdown_content = parsed['content']
        frontmatter = parsed['frontmatter']

        # ##見出しで分割
        parts = self.heading_pattern.split(markdown_content)

        pages = []
        toc = []

        if len(parts) > 1:  # ##見出しがある場合
            # 最初の##以前のコンテンツ
            first_content = parts[0].strip()
            if first_content:
                pages.append({
                    'title': 'はじめに',
                    'content': first_content,
                    'index': 0
                })
                toc.append({
                    'title': 'はじめに',
                    'page': 0
                })

            # ##以降のセクション
            for i in range(1, len(parts) - 1, 2):
                title = parts[i].strip()  # 見出しのタイトル
                section_content = parts[i + 1].strip()  # セクションの内容
                page_index = len(pages)

                pages.append({
                    'title': title,
                    'content': section_content,
                    'index': page_index
                })
                toc.append({
                    'title': title,
                    'page': page_index
                })
        else:  # ##見出しがない場合
            pages.append({
                'title': frontmatter.get('title', 'コンテンツ'),
                'content': markdown_content,
                'index': 0
            })

        return {
            'pages': pages,
            'toc': toc,
            'total_pages': len(pages)
        }
```

### utils/markdown_parser.py 完全解説

```python
import markdown
from pygments import highlight
from pygments.lexers import get_lexer_by_name, TextLexer
from pygments.formatters import HtmlFormatter
from pygments.util import ClassNotFound

class MarkdownParser:
    """MarkdownをHTMLに変換するクラス"""

    def __init__(self):
        # Markdownパーサーの初期化
        self.md = markdown.Markdown(
            extensions=[
                'fenced_code',  # ```で囲まれたコードブロック
                'tables',       # テーブル記法
                'nl2br',        # 改行を<br>に変換
                'sane_lists',   # リストのネストを改善
                'codehilite',    # コードブロックのハイライト
                'attr_list',     # 要素に属性を付加 {: .class="hoge"}
            ],
            extension_configs={
                'codehilite': {
                    'linenums': False,  # 行番号なし
                    'css_class': 'code-highlight'  # 適用するクラス名
                }
            }
        )
        # Pygmentsフォーマッターの初期化
        self.formatter = HtmlFormatter(
            style='github-dark',  # カラーテーマ
            cssclass='code-highlight'
        )

    def parse(self, content):
        """MarkdownをHTMLに変換"""
        self.md.reset()  # パーサーのリセット
        return self.md.convert(content)

    def get_highlight_styles(self):
        """シンタックスハイライトのCSSを取得"""
        return self.formatter.get_style_defs('.code-highlight')
```

---

## HTML/CSS基礎

ユーザーの画面を作るフロントエンド開発を学びます。

### HTMLの基本

**HTMLとは**

HTML（HyperText Markup Language）は、Webページの構造を記述する言語です。

**HTMLの基本構造**

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>ページタイトル</title>
</head>
<body>
    <h1>見出し</h1>
    <p>段落です。</p>
</body>
</html>
```

**よく使うHTMLタグ**

| タグ | 説明 | 使用例 |
|-----|------|--------|
| `<h1>`〜`<h6>` | 見出し | `<h1>大見出し</h1>` |
| `<p>` | 段落 | `<p>本文</p>` |
| `<a>` | リンク | `<a href="/page">リンク</a>` |
| `<img>` | 画像 | `<img src="image.jpg" alt="説明">` |
| `<ul>` `<ol>` | リスト | `<ul><li>項目</li></ul>` |
| `<div>` | 区切り | `<div>コンテンツ</div>` |
| `<span>` | インライン | `<span>強調</span>` |

**HTMLの属性**

```html
<!-- id属性：ページ内で一意の識別子 -->
<div id="header">ヘッダー</div>

<!-- class属性：スタイル適用のためのクラス名 -->
<p class="description">説明文</p>

<!-- data属性：カスタムデータの埋め込み -->
<div data-user-id="123">ユーザー情報</div>
```

### CSSの基本

**CSSとは**

CSS（Cascading Style Sheets）は、HTMLの見た目を指定する言語です。

**CSSの書き方**

```css
/* セレクタ { プロパティ: 値; } */
h1 {
    color: #333333;
    font-size: 24px;
}

/* クラスセレクタ */
.description {
    color: #666666;
}

/* IDセレクタ */
#header {
    background: #f0f0f0;
}
```

**CSS変数**

```css
:root {
    --primary-color: #f54e00;
    --background: #f2f1ed;
}

h1 {
    color: var(--primary-color);
}

body {
    background: var(--background);
}
```

**CSSの詳細度**

```css
/* 詳細度の高いルールが優先される */
h1 { color: red; }          /* 詳細度: 0, 010 */
h1.title { color: blue; }    /* 詳細度: 0, 110 → 優先 */
```

### デザインシステム

**デザイントークン**

```css
:root {
    /* 色 */
    --cursor-dark: #26251e;
    --cursor-cream: #f2f1ed;
    --accent: #f54e00;

    /* フォント */
    --font-gothic: system-ui;
    --font-serif: 'Source Serif 4';
    --font-mono: ui-monospace;
}
```

**一貫性のあるデザイン**

- 色は変数で管理
- スペースは8px単位
- フォントサイズは階層的に
- 役割ごとにルールを決める

---

## テンプレート詳解

Flaskのテンプレート機能を使って、動的なWebページを作ります。

### テンプレートとは

テンプレートは、HTMLの中にPythonのコードを埋め込む仕組みです。

### テンプレートの基本構造

**base.html**

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}デフォルトタイトル{% endblock %}</title>
</head>
<body>
    {% include 'components/header.html' %}
    <main>{% block content %}{% endblock %}</main>
    {% include 'components/footer.html' %}
</body>
</html>
```

**解説**

| 構文 | 説明 |
|------|------|
| `{% ... %}` | Pythonのコードを実行 |
| `{{ ... }}` | 変数を表示 |
| `{# ... #}` | コメント |
| `{% block %}` | ブロック定義（継承元で上書き可能） |
| `{% endblock %}` | ブロックの終了 |

### templates/index.html 解説

```html
{% extends "base.html" %}  {# base.htmlを継承 #}

{% block title %}本棚 - Bookshelf4MD{% endblock %}  {# タイトルを上書き #}

{% block content %}  {# コンテンツブロックを定義 #}
<section class="books-section">
    <div class="section-header">
        <h2 class="section-title">ドキュメント</h2>
        <div class="view-toggle">  {# 表示切替ボタン #}
            <button class="view-toggle-btn" data-mode="shelf">
                📚
            </button>
            <button class="view-toggle-btn" data-mode="list">
                📋
            </button>
        </div>
    </div>

    <div class="books-container {{ view_mode }}-mode">  {# 動的にクラスを追加 #}
        {% for book in books %}  {# booksリストを繰り返し #}
        <article class="book-card" data-filename="{{ book.filename }}">
            <h3>{{ book.title }}</h3>
            <p>{{ book.description }}</p>
            <a href="{{ url_for('view_book', filename=book.filename) }}">
                読む →
            </a>
        </article>
        {% endfor %}
    </div>
</section>
{% endblock %}
```

**主なフィルター**

| フィルター | 説明 | 例 |
|----------|------|------|
| `url_for` | URLを生成 | `{{ url_for('index') }}` |
| `safe` | HTMLをエスケープしない | `{{ html_content\|safe }}` |
| `default` | デフォルト値 | `{{ value\|default('デフォルト') }}` |

### templates/book.html 解説

```html
{% extends "base.html" %}

{% block title %}{{ title }} - Bookshelf4MD{% endblock %}

{% block content %}
<article class="book-page">
    {% include 'components/sidebar_toc.html' %}  {# サイドバーを読み込み #}

    <div class="book-main">
        <div class="book-header-bar">
            <a href="{{ url_for('index') }">← 戻る</a>
            {% include 'components/progress_bar.html' %}  {# 進捗バー #}
        </div>

        <div class="book-content">
            <h1>{{ current_page.title }}</h1>
            <div class="page-body">
                {{ html_content|safe }}  {# Markdownを変換したHTMLを表示 #}
            </div>
        </div>
    </div>
</article>
{% endblock %}
```

### コンポーネントの分離

**components/sidebar_toc.html**

```html
<aside class="sidebar" id="sidebar">
    <div class="sidebar-inner">
        <h3 class="sidebar-title">目次</h3>
        <nav class="sidebar-nav">
            <ul class="toc-list">
                {% for item in toc %}
                <li class="toc-item">
                    <a href="{{ url_for('view_book', filename=filename, page_num=item.page + 1) }}"
                       class="toc-link {% if item.page + 1 == current_page_num %}active{% endif %}">
                        {{ item.title }}
                    </a>
                </li>
                {% endfor %}
            </ul>
        </nav>
    </div>
</aside>
```

**components/progress_bar.html**

```html
<div class="progress-container">
    <div class="progress-info">
        <span class="progress-label">{{ current_page_num }} / {{ total_pages }}</span>
        <span class="progress-percent">{{ "%.1f"|format(progress) }}%</span>
    </div>
    <div class="progress-bar-bg">
        <div class="progress-bar-fill" style="width: {{ progress }}%"></div>
    </div>
</div>
```

---

## CSSデザインシステム詳解

Cursor風のデザインシステムを適用したCSSを解説します。

### CSS変数の定義

```css
:root {
    /* Primary Colors */
    --cursor-dark: #26251e;
    --cursor-cream: #f2f1ed;
    --cursor-light: #e6e5e0;
    --accent: #f54e00;

    /* Surface Scale */
    --surface-300: #ebeae5;
    --surface-400: #e6e5e0;

    /* Text Colors */
    --text-primary: #26251e;
    --text-secondary: rgba(38, 37, 30, 0.55);

    /* Borders */
    --border-default: rgba(38, 37, 30, 0.1);

    /* Shadows */
    --shadow-card: rgba(0,0,0,0.14) 0px 28px 70px, rgba(0,0,0,0.1) 0px 14px 32px;

    /* Fonts */
    --font-gothic: system-ui;
    --font-serif: 'Source Serif 4';
    --font-mono: ui-monospace;
}
```

### 基本スタイル

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    background: var(--cursor-cream);
    color: var(--text-primary);
    font-family: var(--font-gothic);
    font-size: 16px;
    line-height: 1.50;
}
```

**解説**

| プロパティ | 説明 |
|-----------|------|
| `box-sizing: border-box` | パディングを含めて幅を計算 |
| `line-height: 1.50` | 行の高さを1.5倍に設定 |

### ボタンスタイル

```css
.btn-primary {
    background: var(--surface-300);
    color: var(--text-primary);
    padding: 10px 14px;
    border-radius: 8px;
    text-decoration: none;
    transition: all 0.15s;
}

.btn-primary:hover {
    color: var(--error);  /* ホバーで赤系に変化 */
}
```

### カードスタイル

```css
.card {
    background: var(--surface-400);
    border: 1px solid var(--border-default);
    border-radius: 8px;
    transition: box-shadow 0.2s;
}

.card:hover {
    box-shadow: var(--shadow-card);
}
```

### レスポンシブデザイン

```css
/* デスクトップ */
.books-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 24px;
}

/* モバイル */
@media (max-width: 600px) {
    .books-container {
        grid-template-columns: 1fr;
    }
}
```

**メディアクエリの使い方**

```css
/* max-width: 1200px */
.container {
    max-width: 1200px;
    margin: 0 auto;  /* 中央寄せ */
    padding: 0 24px;
}
```

---

## JavaScript詳解

ユーザー操作に応答する動きを実装します。

### JavaScriptの基本

**変数の定義**

```javascript
// constで再代入不可の変数
const appName = 'Bookshelf4MD';

// letで再代入可能な変数
let currentPage = 1;

// 組み込み演算子
const totalPages = 10;
const progress = (currentPage / totalPages) * 100;
```

**関数の定義**

```javascript
function greet(name) {
    return `こんにちは、${name}さん！`;
}

// アロー関数（ES6）
const add = (a, b) => a + b;
```

**DOM操作**

```javascript
// 要素の取得
const button = document.querySelector('.btn-primary');
const buttons = document.querySelectorAll('.view-toggle-btn');

// 要素の操作
element.textContent = 'クリックしました';
element.classList.add('active');
element.style.color = 'red';
```

### 表示モード切り替え

```javascript
function initViewToggle() {
    const buttons = document.querySelectorAll('.view-toggle-btn');
    const container = document.querySelector('.books-container');

    buttons.forEach(btn => {
        btn.addEventListener('click', async () => {
            const mode = btn.dataset.mode;  // data-mode属性を取得

            // サーバーにリクエスト
            const response = await fetch(`/set_view_mode/${mode}`, {
                method: 'POST'
            });

            // 表示を更新
            buttons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            container.classList.remove('shelf-mode', 'list-mode');
            container.classList.add(`${mode}-mode`);
        });
    });
}
```

**解説**

| メソッド | 説明 |
|---------|------|
| `querySelector()` | 最初のマッチする要素を取得 |
| `querySelectorAll()` | 全てのマッチする要素を取得 |
| `addEventListener()` | イベントリスナーを追加 |
| `dataset.mode` | `data-mode`属性の値を取得 |
| `classList.add()` | クラスを追加 |
| `classList.remove()` | クラスを削除 |

### サイドバー操作

```javascript
function initSidebar() {
    const sidebar = document.getElementById('sidebar');
    const toggle = document.getElementById('sidebarToggle');
    const close = document.getElementById('sidebarClose');

    // トグルボタンで開閉
    toggle.addEventListener('click', () => {
        sidebar.classList.toggle('open');
    });

    // 閉じるボタン
    close.addEventListener('click', () => {
        sidebar.classList.remove('open');
    });
}
```

### コピーボタン機能

```javascript
function initCopyButtons() {
    const codeBlocks = document.querySelectorAll('pre code');

    codeBlocks.forEach(codeBlock => {
        const pre = codeBlock.parentElement;
        if (pre.classList.contains('has-copy-button')) return;

        // ヘッダーを作成
        const header = document.createElement('div');
        header.className = 'code-header';

        // コピーボタンを作成
        const copyBtn = document.createElement('button');
        copyBtn.className = 'copy-button';
        copyBtn.textContent = 'コピー';

        // クリックイベント
        copyBtn.addEventListener('click', async () => {
            await navigator.clipboard.writeText(codeBlock.textContent);
            copyBtn.textContent = 'コピーしました！';
            setTimeout(() => {
                copyBtn.textContent = 'コピー';
            }, 2000);
        });

        header.appendChild(copyBtn);
        pre.insertBefore(header, pre.firstChild);
        pre.classList.add('has-copy-button');
    });
}
```

**Clipboard API**

```javascript
// テキストをクリップボードにコピー
await navigator.clipboard.writeText('コピーするテキスト');

// フォールバッグ
try {
    await navigator.clipboard.writeText(text);
} catch {
    // 非対応
}
```

### キーボードナビゲーション

```javascript
document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' && currentPageNum < totalPages) {
        // 次のページへ
        window.location.href = `/book/${filename}/page/${currentPageNum + 1}`;
    }
});
```

### イベントの種類

| イベント | 発火タイミング | 例 |
|--------|--------------|-----|
| `click` | クリック時 | ボタン押下 |
| `keydown` | キー押下時 | 矢印キー操作 |
| `DOMContentLoaded` | HTML読み込み完了時 | 初期化処理 |
| `submit` | フォーム送信時 | フォーム処理 |

### 非同期処理

```javascript
// fetch APIでデータを取得
async function loadData() {
    try {
        const response = await fetch('/api/books');
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error('エラー:', error);
    }
}
```

---

## 動作解説

Bookshelf4MDの完全な動作フローを解説します。

### アプリケーション起動の流れ

```
ユーザーがstart.batを実行
    ↓
.venvのPythonが起動
    ↓
Flaskアプリケーション(app.py)がロード
    ↓
設定(config.py)が読み込まれる
    ↓
ユーティリティモジュールが初期化される
    ↓
サーバーが http://localhost:5000 で待機開始
```

### トップページ表示までの流れ

```
1. ブラウザで http://localhost:5000 にアクセス
    ↓
2. Flaskルーター: @app.route('/') がマッチ
    ↓
3. index()関数が実行される
    ↓
4. MARKDOWN_DIR から全.mdファイルをスキャン
    ↓
5. 各ファイルのフロントマターを解析
    ↓
6. BookInfoオブジェクトのリストを作成
    ↓
7. Cookieからview_modeを取得（デフォルト'shelf'）
    ↓
8. render_template('index.html', ...) を実行
    ↓
9. Jinja2テンプレートがHTMLに変換される
    ↓
10. レスポンスとしてHTMLが返される
    ↓
11. ブラウザがHTMLをレンダリング
    ↓
12. static/js/main.js がDOMContentLoadedイベントで初期化
```

### 本のページ表示までの流れ

```
1. ユーザーが書籍カードをクリック
    ↓
2. href="/book/tutorial/01-introduction/page/1" に遷移
    ↓
3. Flaskルーター: @app.route('/book/<path:filename>/page/<int:page_num>') がマッチ
    ↓
4. view_book()関数が filename='tutorial/01-introduction', page_num=1 で実行
    ↓
5. ファイルパスを構築: mds/tutorial/01-introduction.md
    ↓
6. Markdownファイルの内容を読み込み
    ↓
7. FrontmatterParserでフロントマターを解析
    ↓
8. PageSplitterで##見出しでページ分割
    ↓
9. page_num-1のインデックスでページデータを取得
    ↓
10. MarkdownParserでMarkdown→HTML変換
    ↓
11. render_template('book.html', ...) を実行
    ↓
12. テンプレート変数が展開される
    ↓
13. ブラウザがHTMLをレンダリング
    ↓
14. main.jsでコピーボタン、キーボードナビゲーションが初期化
```

### 表示モード切り替えの流れ

```
1. ユーザーが📋ボタンをクリック
    ↓
2. JavaScriptのclickイベント発火
    ↓
3. initViewToggle()内のハンドラーが実行
    ↓
4. data-mode属性から'mode'を取得
    ↓
5. fetch('/set_view_mode/list', {method: 'POST'}) を実行
    ↓
6. Flaskの set_view_mode()ルートが呼ばれる
    ↓
7. resp.set_cookie('view_mode', 'list') でCookieを設定
    ↓
8. JSONレスポンス {"status": "ok"} を返す
    ↓
9. JavaScriptでクラスを切り替え
    ↓
10. CSSの.list-modeルールが適用される
```

### コピーボタンの処理フロー

```
1. ページ読み込み完了(DOMContentLoaded)
    ↓
2. initCopyButtons()が実行される
    ↓
3. document.querySelectorAll('pre code') で全コードブロックを取得
    ↓
4. 各codeBlockの親要素(pre)にヘッダーを追加
    ↓
5. コピー用button要素を作成してヘッダーに追加
    ↓
6. クリックイベントリスナーを設定
    ↓
7. ユーザーが「コピー」ボタンをクリック
    ↓
8. navigator.clipboard.writeText() でクリップボードにコピー
    ↓
9. ボタンのテキストを「コピーしました！」に変更
    ↓
10. 2秒後に「コピー」に戻す
```

### ファイル構成と役割

| ファイル | 役割 | タイミング |
|---------|------|----------|
| `config.py` | 設定値の定義 | アプリ起動時 |
| `app.py` | ルーティングとリクエスト処理 | リクエストごと |
| `utils/frontmatter_parser.py` | YAMLフロントマター解析 | ファイル読み込み時 |
| `utils/page_splitter.py` | ページ分割と目次生成 | 本の表示時 |
| `utils/markdown_parser.py` | Markdown→HTML変換 | 本の表示時 |
| `templates/base.html` | ベーステンプレート | 全ページ |
| `templates/index.html` | トップページ | `/` アクセス時 |
| `templates/book.html` | 本のページ | `/book/...` アクセス時 |
| `templates/components/*.html` | 再利用コンポーネント | テンプレートから参照 |
| `static/css/styles.css` | スタイル定義 | 全ページ |
| `static/js/main.js` | インタラクティブ機能 | ページ読み込み時 |

### データの流れ図

```
┌─────────────────────────────────────────────────────────────────┐
│                        ユーザーのブラウザ                        │
│  ┌────────────┐  ┌────────────┐  ┌──────────────────────────┐  │
│  │   HTML     │  │    CSS     │  │       JavaScript         │  │
│  │ (構造)     │  │  (スタイル) │  │   (インタラクション)     │  │
│  └────────────┘  └────────────┘  └──────────────────────────┘  │
└──────────────────────────────┬──────────────────────────────────┘
                               │ HTTPリクエスト
                               ↓
┌─────────────────────────────────────────────────────────────────┐
│                      Flask サーバー(app.py)                      │
│  ┌────────────┐  ┌────────────┐  ┌──────────────────────────┐  │
│  │  Routing   │  │  Request   │  │      Response            │  │
│  │  (@route)  │  │  Handling  │  │   (render_template)      │  │
│  └────────────┘  └────────────┘  └──────────────────────────┘  │
└──────────────────────────────┬──────────────────────────────────┘
                               │ データ取得
                               ↓
┌─────────────────────────────────────────────────────────────────┐
│                      ユーティリティモジュール                     │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────┐  │
│  │FrontmatterParser │  │  PageSplitter    │  │MarkdownParser│  │
│  │  (YAML解析)      │  │ (ページ分割)     │  │  (HTML変換)  │  │
│  └──────────────────┘  └──────────────────┘  └──────────────┘  │
└──────────────────────────────┬──────────────────────────────────┘
                               │ ファイル読み込み
                               ↓
┌─────────────────────────────────────────────────────────────────┐
│                   Markdownファイル(mds/ディレクトリ)              │
│  ┌────────────┐  ┌────────────┐  ┌──────────────────────────┐  │
│  │Frontmatter │  │   Markdown  │  │   ## 見出し              │  │
│  │(YAMLメタデータ)│  │  (本文)    │  │   (ページ区切り)        │  │
│  └────────────┘  └────────────┘  └──────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 実践演習

学んだ知識を応用して、新しい機能を実装します。

### 演習1: 検索機能の追加

書籍をタイトルと説明文から検索できる機能を実装します。

**ステップ1: HTMLに検索ボックスを追加**

```html
<!-- templates/index.html -->
<div class="section-header">
    <h2 class="section-title">ドキュメント</h2>

    <!-- 検索ボックスを追加 -->
    <div class="search-box">
        <input type="text" id="searchInput" placeholder="検索...">
    </div>

    <div class="view-toggle">
        <!-- 既存のトグルボタン -->
    </div>
</div>
```

**ステップ2: CSSでスタイル適用**

```css
/* static/css/styles.css */

.search-box {
    flex: 1;
    max-width: 300px;
    margin: 0 20px;
}

#searchInput {
    width: 100%;
    padding: 10px 14px;
    border: 1px solid var(--border-default);
    border-radius: 8px;
    background: var(--surface-400);
    color: var(--text-primary);
    font-size: 14px;
}

#searchInput:focus {
    outline: none;
    border-color: var(--accent);
}
```

**ステップ3: JavaScriptで検索機能実装**

```javascript
// static/js/main.js に追加

function initSearch() {
    const searchInput = document.getElementById('searchInput');
    const bookCards = document.querySelectorAll('.book-card');

    if (!searchInput) return;

    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase();

        bookCards.forEach(card => {
            const title = card.querySelector('h3').textContent.toLowerCase();
            const description = card.querySelector('p').textContent.toLowerCase();

            if (title.includes(query) || description.includes(query)) {
                card.style.display = '';
            } else {
                card.style.display = 'none';
            }
        });
    });
}

// DOMContentLoaded で呼び出し
document.addEventListener('DOMContentLoaded', () => {
    // 既存の初期化...
    initSearch();
});
```

**解説**

| メソッド | 説明 |
|---------|------|
| `toLowerCase()` | 大文字小文字を区別しない検索 |
| `includes()` | 文字列が含まれるか判定 |
| `style.display` | 要素の表示/非表示を切り替え |

### 演習2: お気に入り機能

Cookieを使ってお気に入りを保存する機能を実装します。

**ステップ1: お気に入りボタンを追加**

```html
<!-- templates/index.html の book-card 内 -->
<article class="book-card" data-filename="{{ book.filename }}">
    <button class="favorite-btn" data-filename="{{ book.filename }}">
        <span class="favorite-icon">☆</span>
    </button>
    <h3>{{ book.title }}</h3>
    <!-- 既存のコンテンツ -->
</article>
```

**ステップ2: CSSでスタイル適用**

```css
.favorite-btn {
    position: absolute;
    top: 12px;
    right: 12px;
    background: var(--surface-300);
    border: none;
    border-radius: 50%;
    width: 36px;
    height: 36px;
    cursor: pointer;
    font-size: 18px;
    transition: all 0.2s;
}

.favorite-btn:hover {
    background: var(--surface-400);
    transform: scale(1.1);
}

.favorite-btn.active {
    background: var(--accent);
    color: white;
}

.favorite-btn.active .favorite-icon {
    content: '★';
}
```

**ステップ3: JavaScriptで機能実装**

```javascript
function initFavorites() {
    const buttons = document.querySelectorAll('.favorite-btn');

    // Cookieからお気に入りを読み込み
    const favorites = getCookie('favorites');
    const favoriteSet = favorites ? JSON.parse(favorites) : [];

    // 既存のお気に入りをハイライト
    favoriteSet.forEach(filename => {
        const btn = document.querySelector(`.favorite-btn[data-filename="${filename}"]`);
        if (btn) btn.classList.add('active');
    });

    // クリックイベント
    buttons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.stopPropagation(); // カードクリックを防止
            const filename = btn.dataset.filename;
            toggleFavorite(filename, btn);
        });
    });
}

function toggleFavorite(filename, btn) {
    let favorites = getCookie('favorites');
    let favoriteSet = favorites ? JSON.parse(favorites) : [];

    const index = favoriteSet.indexOf(filename);

    if (index > -1) {
        // 削除
        favoriteSet.splice(index, 1);
        btn.classList.remove('active');
    } else {
        // 追加
        favoriteSet.push(filename);
        btn.classList.add('active');
    }

    // Cookieに保存（365日間）
    setCookie('favorites', JSON.stringify(favoriteSet), 365);
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    const expires = `expires=${date.toUTCString()}`;
    document.cookie = `${name}=${value};${expires};path=/`;
}
```

**解説**

| 機能 | 説明 |
|------|------|
| `JSON.parse()` | Cookieから配列を読み出し |
| `JSON.stringify()` | 配列を文字列に変換して保存 |
| `e.stopPropagation()` | 親要素のイベントを防止 |
| `indexOf()` | 配列内の要素を検索 |

### 演習3: ダークモード切替

CSS変数を切り替えるダークモードを実装します。

**ステップ1: CSS変数を定義**

```css
/* static/css/styles.css */

:root {
    /* ライトモード（既存） */
    --cursor-cream: #f2f1ed;
    --cursor-dark: #26251e;
    --text-primary: #26251e;
    --surface-400: #e6e5e0;
}

[data-theme="dark"] {
    /* ダークモード */
    --cursor-cream: #1a1a1a;
    --cursor-dark: #f2f1ed;
    --text-primary: #f2f1ed;
    --surface-400: #2a2a2a;
}

body {
    background: var(--cursor-cream);
    color: var(--text-primary);
    transition: background 0.3s, color 0.3s;
}
```

**ステップ2: トグルボタンを追加**

```html
<!-- templates/components/header.html -->
<button id="themeToggle" class="theme-toggle">
    <span class="theme-icon">🌙</span>
</button>
```

**ステップ3: JavaScriptで実装**

```javascript
function initThemeToggle() {
    const toggle = document.getElementById('themeToggle');
    if (!toggle) return;

    // Cookieからテーマを読み込み
    const theme = getCookie('theme') || 'light';
    document.documentElement.setAttribute('data-theme', theme);
    updateThemeIcon(theme);

    toggle.addEventListener('click', () => {
        const current = document.documentElement.getAttribute('data-theme');
        const newTheme = current === 'dark' ? 'light' : 'dark';

        document.documentElement.setAttribute('data-theme', newTheme);
        setCookie('theme', newTheme, 365);
        updateThemeIcon(newTheme);
    });
}

function updateThemeIcon(theme) {
    const icon = document.querySelector('.theme-icon');
    icon.textContent = theme === 'dark' ? '☀️' : '🌙';
}
```

### 演習4: ページ送りボタンの改善

現在のキーボードナビゲーションに加え、画面上のボタンでもページ移動できるようにします。

**HTMLを追加**

```html
<!-- templates/book.html の book-main 内 -->
<div class="book-navigation">
    {% if current_page_num > 1 %}
    <a href="{{ url_for('view_book', filename=filename, page_num=current_page_num - 1) }}"
       class="nav-btn prev-btn">
        ← 前のページ
    </a>
    {% endif %}

    <span class="nav-info">{{ current_page_num }} / {{ total_pages }}</span>

    {% if current_page_num < total_pages %}
    <a href="{{ url_for('view_book', filename=filename, page_num=current_page_num + 1) }}"
       class="nav-btn next-btn">
        次のページ →
    </a>
    {% endif %}
</div>
```

**CSSを追加**

```css
.book-navigation {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
    padding: 24px 0;
    margin-top: 40px;
}

.nav-btn {
    padding: 10px 20px;
    background: var(--surface-300);
    color: var(--text-primary);
    text-decoration: none;
    border-radius: 8px;
    transition: all 0.2s;
}

.nav-btn:hover {
    background: var(--surface-400);
}

.nav-info {
    font-weight: 500;
}
```

### 演習5: 読書履歴の記録

最後に読んだページをCookieに記録し、次回開いた時に続きから読めるようにします。

**Flaskバックエンド**

```python
# app.py に追加

@app.route('/save_progress', methods=['POST'])
def save_progress():
    data = request.get_json()
    filename = data.get('filename')
    page_num = data.get('page_num')

    resp = jsonify({'status': 'ok'})
    resp.set_cookie(f'progress_{filename}', str(page_num), max_age=365*24*60*60)
    return resp

@app.route('/get_progress/<path:filename>')
def get_progress(filename):
    page_num = request.cookies.get(f'progress_{filename}')
    return jsonify({'page_num': int(page_num) if page_num else 1})
```

**JavaScriptフロントエンド**

```javascript
// ページ表示時に進捗を保存
function saveReadingProgress(filename, page_num) {
    fetch('/save_progress', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({filename, page_num})
    });
}

// ページ読み込み時に呼び出し
document.addEventListener('DOMContentLoaded', () => {
    const filename = document.querySelector('[data-filename]')?.dataset.filename;
    const currentPageNum = {{ current_page_num }};

    if (filename && currentPageNum) {
        saveReadingProgress(filename, currentPageNum);
    }
});
```

**トップページで続きを表示**

```html
<!-- templates/index.html -->
{% for book in books %}
<article class="book-card" data-filename="{{ book.filename }}">
    {% if book.continue_page %}
    <div class="continue-reading">
        <a href="{{ url_for('view_book', filename=book.filename, page_num=book.continue_page) }}">
            続きから読む ({{ book.continue_page }}ページ目)
        </a>
    </div>
    {% endif %}
    <!-- 既存のコンテンツ -->
</article>
{% endfor %}
```

```python
# app.pyのindex()関数内
for book in books:
    # 進捗情報を取得
    progress_page = request.cookies.get(f'progress_{book.filename}')
    if progress_page:
        book.continue_page = int(progress_page)
```

---

## デプロイと次のステップ

作成したアプリケーションを本番環境で公開します。

### デプロイ構成

```
┌─────────────────────────────────────────────────────────────┐
│                      インターネット                          │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ↓
┌─────────────────────────────────────────────────────────────┐
│                      nginx (ポート80/443)                   │
│                      - HTTPS終端                            │
│                      - 静的ファイル配信                      │
│                      - リバースプロキシ                      │
└──────────────────────────────┬──────────────────────────────┘
                               │ / (動的リクエスト)
                               ↓
┌─────────────────────────────────────────────────────────────┐
│                   Gunicorn (ポート8000)                     │
│                   - WSGIサーバー                            │
│                   - ワーカープロセス管理                    │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ↓
┌─────────────────────────────────────────────────────────────┐
│                    Flaskアプリケーション                    │
│                    (app.py)                                 │
└─────────────────────────────────────────────────────────────┘
```

### Gunicornの設定

**インストール**

```bash
pip install gunicorn
```

**起動コマンド**

```bash
# 基本的な起動
gunicorn -w 4 -b 0.0.0.0:8000 app:app

# オプションの説明
# -w 4: 4つのワーカープロセス
# -b 0.0.0.0:8000: 8000番ポートで待機
# app:app: app.pyのappインスタンス
```

**gunicorn.conf.py設定ファイル**

```python
# gunicorn.conf.py
import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1  # CPUコア数 × 2 + 1
bind = "0.0.0.0:8000"
timeout = 120
keepalive = 5
max_requests = 1000  # メモリリーク対策
max_requests_jitter = 100  # ワーカー再起動を分散
preload_app = True  # メモリ節約
```

**起動（設定ファイル使用）**

```bash
gunicorn -c gunicorn.conf.py app:app
```

### nginxの設定

**基本設定**

```nginx
# /etc/nginx/sites-available/bookshelf4md

server {
    listen 80;
    server_name your-domain.com;

    # 静的ファイルの直接配信
    location /static {
        alias /path/to/app/static;
        expires 30d;  # ブラウザキャッシュ
        add_header Cache-Control "public, immutable";
    }

    # 動的リクエストをGunicornに転送
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
    }
}
```

**HTTPS設定（Let's Encrypt）**

```bash
# CertbotでSSL証明書取得
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

```nginx
# HTTPS設定が自動追加される
server {
    listen 443 ssl;
    server_name your-domain.com;

    ssl_certificate /etc/letsencrypt/live/your-domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;

    # 既存の設定
    # ...
}

# HTTP→HTTPSリダイレクト
server {
    listen 80;
    server_name your-domain.com;
    return 301 https://$server_name$request_uri;
}
```

### Systemdサービス設定

**サービスファイル作成**

```ini
# /etc/systemd/system/bookshelf4md.service

[Unit]
Description=Bookshelf4MD Gunicorn Service
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/path/to/app
Environment="PATH=/path/to/app/.venv/bin"
ExecStart=/path/to/app/.venv/bin/gunicorn -c gunicorn.conf.py app:app
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

**サービス操作**

```bash
# サービス有効化
sudo systemctl enable bookshelf4md

# サービス起動
sudo systemctl start bookshelf4md

# サービス状態確認
sudo systemctl status bookshelf4md

# ログ確認
sudo journalctl -u bookshelf4md -f
```

### 本番環境の設定

**環境変数の設定**

```bash
# .env (本番環境)
SECRET_KEY=強力なランダム文字列
FLASK_ENV=production
FLASK_DEBUG=False
```

```python
# config.py の修正
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
    raise ValueError("SECRET_KEY environment variable is required")

DEBUG = False
SESSION_COOKIE_SECURE = True  # HTTPS必須
```

**セキュリティ対策**

| 設定 | 目的 |
|------|------|
| `SECRET_KEY` | セッション暗号化 |
| `SESSION_COOKIE_SECURE=True` | HTTPSのみでCookie送信 |
| `SESSION_COOKIE_HTTPONLY=True` | JavaScriptからCookieアクセス禁止 |
| `DEBUG=False` | エラー詳細非表示 |

### デプロイ手順

**サーバー準備**

```bash
# 1. サーバーに接続
ssh user@server

# 2. 必要なパッケージインストール
sudo apt update
sudo apt install python3 python3-venv nginx certbot

# 3. プロジェクト配置
git clone your-repo-url /var/www/bookshelf4md
cd /var/www/bookshelf4md

# 4. 仮想環境作成
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install gunicorn

# 5. 環境変数設定
cp .env.example .env
nano .env  # SECRET_KEYなどを設定

# 6. nginx設定
sudo cp deploy/nginx.conf /etc/nginx/sites-available/bookshelf4md
sudo ln -s /etc/nginx/sites-available/bookshelf4md /etc/nginx/sites-enabled/
sudo nginx -t  # 設定確認
sudo systemctl reload nginx

# 7. サービス登録
sudo cp deploy/bookshelf4md.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable bookshelf4md
sudo systemctl start bookshelf4md

# 8. SSL証明書取得
sudo certbot --nginx -d your-domain.com
```

### トラブルシューティング

**アプリが起動しない**

```bash
# ログ確認
sudo journalctl -u bookshelf4md -n 50

# よくある問題
# - ポート番号の競合: sudo lsof -i :8000
# - ファイルパーミッション: sudo chown -R www-data:www-data /path/to/app
# - 仮想環境のパス: which python3 で確認
```

**502 Bad Gateway**

```bash
# Gunicornが動いているか確認
sudo systemctl status bookshelf4md

# ポート番号が一致しているか確認
sudo netstat -tlnp | grep 8000
```

**静的ファイルが表示されない**

```bash
# nginxのエラーログ
sudo tail -f /var/log/nginx/error.log

# パスが正しいか確認
ls -la /path/to/app/static
```

### 次のステップ

**学習リソース**

| トピック | リソース |
|---------|----------|
| Flask公式ドキュメント | https://flask.palletsprojects.com/ |
| Pythonチュートリアル | https://docs.python.org/ja/3/tutorial/ |
| MDN Web Docs | https://developer.mozilla.org/ja/ |
| nginxドキュメント | https://nginx.org/en/docs/ |

**次に学ぶべき技術**

- データベース（SQLite/PostgreSQL）
- ユーザー認証（Flask-Login）
- API開発（Flask-RESTful）
- フロントエンドフレームワーク（Vue.js/React）
- テスト（pytest）
- コンテナ（Docker）
- CI/CD（GitHub Actions）

**ポートフォリオ作成のヒント**

1. **機能追加**: 独自の機能を実装
2. **デザイン改善**: UI/UXを向上
3. **パフォーマンス**: 高速化に取り組む
4. **コード品質**: リファクタリングとテスト
5. **ドキュメント**: READMEとAPIドキュメント作成

**アイデアの実装**

- コメント機能
- タグ付けとフィルタリング
- PDFエクスポート
- 読書時間の統計
- マルチユーザー対応
- ダークモード自動切り替え
- 検索機能の強化
- お気に入り機能

---

## 全章のまとめ

このチュートリアルで学んだ内容：

1. **Webアプリケーションの仕組み**: クライアント/サーバーモデル
2. **開発環境**: Python、仮想環境、パッケージ管理
3. **Python基礎**: 変数、関数、クラス、モジュール
4. **Flask**: ルーティング、テンプレート、リクエスト処理
5. **ユーティリティ**: フロントマター、ページ分割、Markdown変換
6. **HTML/CSS**: 構造とスタイルの分離
7. **テンプレート**: Jinja2による動的ページ生成
8. **CSSデザイン**: 変数、レスポンシブ、ホバー効果
9. **JavaScript**: DOM操作、イベント、非同期処理
10. **データフロー**: リクエストからレスポンスまでの全体像
11. **実践演習**: 検索、お気に入り、ダークモードの実装
12. **デプロイ**: nginx、Gunicorn、本番環境構築

これで自分でWebアプリケーションを作成し、公開できる基礎が身につきました。次は自分のアイデアを形にしていきましょう。
