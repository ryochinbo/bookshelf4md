---
title: Webアプリケーション開発ガイド
description: Bookshelf4MDのコード解説を中心に、webアプリケーションの作り方を学べる
cover: /media_mds/media_web-app-development-complete-guide/image.png
---

# Webアプリケーション開発ガイド

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

**変数とは何か？**

変数は「データを入れる箱」のようなものです。プログラムで扱う様々なデータを記憶しておくために使います。

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

**コード解説:**

- `=` は「等しい」ではなく「代入」を意味します
- 右側の値を左側の変数に入れています
- Pythonは変数の型を自動的に判断します（動的型付け）
- `message` は文字列、`count` は整数、`price` は小数、`is_active` は真偽値

**なぜこのように書くのか？**

- 変数名は英語で意味が分かる名前をつけます（日本語も使えますが、英語が一般的）
- `print()` はコンソールに表示する関数で、デバッグや確認に使います
- 各行のコメント `# ...` は出力結果を示しています

**主なデータ型**

| 型 | 説明 | 例 | いつ使う？ |
|----|------|------|----------|
| `str` | 文字列 | `"hello"` | テキストデータを扱うとき |
| `int` | 整数 | `42` | 個数、年齢など数えられるもの |
| `float` | 浮動小数点 | `3.14` | 価格、割合など小数を含むもの |
| `bool` | 真偽値 | `True`, `False` | 条件分岐の結果 |
| `list` | リスト | `[1, 2, 3]` | 複数の要素をまとめるとき |
| `dict` | 辞書 | `{"key": "value"}` | キーと値のペアを扱うとき |
| `None` | 何もない | `None` | 値が存在しないことを示すとき |

**文字列の操作**

**文字列結合の基礎**

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

**コード解説:**

1. **文字列結合（+演算子）**
   - `+` で文字列を連結できます
   - **制限**: 文字列同士しか結合できません（数値はエラーになります）

2. **f文字列（フォーマット文字列）**
   - `f"{変数名}"` の形式で変数を文字列に埋め込めます
   - Python 3.6以降で使える、最もモダンな方法

**なぜf文字列を使うのか？**

- 読みやすく、書きやすい
- 型変換を自動で行ってくれる（数値もそのまま使える）
- 複雑な式も埋め込める：`f"{1 + 1}の答えは2です"` → `"2の答えは2です"`

**他の書き方（参考）:**

```python
# format()メソッド（古い書き方）
message = "{}さんは{}歳です".format(name, age)

# %演算子（さらに古い書き方）
message = "%sさんは%d歳です" % (name, age)
```

**推奨**: 新しいコードではf文字列を使いましょう

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

**コード解説:**

1. **リストの作成とインデックス**
   - `[要素1, 要素2, ...]` でリストを作成
   - `fruits[0]` で最初の要素を取得（インデックスは0から始まります）
   - `fruits[1]` は2番目、`fruits[-1]` は最後の要素

2. **append()メソッド**
   - リストの末尾に要素を追加
   - **重要**: 元のリストを直接変更します（新しいリストを作りません）

3. **len()関数**
   - リストの要素数を取得

4. **for文での繰り返し**
   - `for 変数 in リスト:` で各要素を順番に処理
   - インデックスを使わずに要素に直接アクセスできます

**なぜこのように書くのか？**

- リストは「順序付きのコレクション」が必要なときに使います
- `append()` は新しいリストを作らないので、メモリ効率が良いです
- for文を使うと、インデックス管理を気にする必要がありません

**実践的な使い方:**

```python
# リストは後から変更可能（ミュータブル）
shopping_list = ["りんご", "バナナ"]
shopping_list.append("オレンジ")  # 追加できる
shopping_list[0] = "青りんご"      # 上書きできる

# 空のリストから始めることも多い
items = []
items.append("アイテム1")
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

プログラムの流れを制御する構文です。

**if文（条件分岐）**

```python
score = 75

if score >= 80:
    print("素晴らしい！")
elif score >= 60:
    print("合格です")
else:
    print("もう少し頑張りましょう")
```

**コード解説:**

- `if 条件:` - 条件がTrueなら実行
- `elif 条件:` - 「そうではなく、もし」の意味
- `else:` - どの条件にも当てはまらない場合
- **重要**: インデント（字下げ）がブロックの範囲を示します

**なぜelifを使うのか？**

- ネスト（入れ子）を深くしないため
- 上から順にチェックし、最初に一致したところだけ実行されます
- `if`文を連続で書くと、すべての条件がチェックされます（効率が悪い）

**for文（繰り返し）**

```python
# 0から4まで繰り返す
for i in range(5):
    print(f"現在の数字: {i}")

# リストの要素を処理
names = ["太郎", "花子", "次郎"]
for name in names:
    print(f"{name}さん、こんにちは！")
```

**コード解説:**

- `range(5)` は0, 1, 2, 3, 4 を生成（5は含まれない）
- `for 変数 in コレクション:` で各要素を順番に処理
- **while** と違って、繰り返し回数が明確なときに使います

**なぜforを使うのか？**

- インデックス管理が不要（バグを減らせる）
- 「コレクションの各要素に何かしたい」という意図が明確
- リスト、文字列、辞書など様々なコレクションに使える

**while文（条件付き繰り返し）**

```python
count = 0
while count < 5:
    print(f"カウント: {count}")
    count += 1
```

**コード解説:**

- `while 条件:` - 条件がTrueの間、繰り返し続ける
- `count += 1` は `count = count + 1` の省略形
- **注意**: 無限ループにならないよう、必ず終了条件を作ること

**forとwhileの使い分け:**

| 状況 | 使うもの | 理由 |
|------|----------|------|
| 回数が決まっている | for | range()で簡潔に書ける |
| リストの全要素を処理 | for | 要素を直接取得できる |
- 繰り返し回数が事前にわからない | while | 条件で制御できる |
- ユーザー入力を待つ | while | 入力があるまで繰り返せる |

### 関数

**関数とは何か？**

関数は「処理のまとまり」に名前をつけたものです。同じ処理を何度も使うときに、関数にしておくと便利です。

**関数の定義**

```python
def greet(name):
    """挨拶を返す関数"""
    return f"こんにちは、{name}さん！"

# 呼び出し
message = greet("太郎")
print(message)  # こんにちは、太郎さん！
```

**コード解説:**

- `def 関数名(引数):` で関数を定義
- `"""..."""` はdocstring（関数の説明文）
- `return` で呼び出し元に値を返す
- **重要**: 関数内のコードはインデントされています

**なぜ関数を使うのか？**

1. **再利用**: 同じ処理を何度も書かなくて済む
2. **管理**: 修正が必要なとき、関数内を直せば全て修正される
3. **可読性**: 関数名で「何をしているか」が分かる
4. **テスト**: 関数単位でテストできる

**良い関数の例:**

```python
# 良い例：1つのことをする関数
def calculate_tax(price):
    return price * 0.1

# 悪い例：複数のことをする関数
def process(price):
    tax = price * 0.1
    print(f"税金: {tax}")
    return price + tax
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

**コード解説:**

- Pythonは複数の値を返せます（実際はタプルとして返っています）
- 呼び出し側で複数の変数で受け取ります：`変数1, 変数2 = 関数()`
- エラー処理にも使えます（成功したかどうかを返す）

**なぜ複数の戻り値を使うのか？**

- 関数の結果と、その結果に関する情報を同時に返せる
- エラー時の戻り値を特別な値（-1やNone）にする必要がない
- コードが読みやすくなります

**デフォルト引数**

```python
def introduce(name, age=20):
    """自己紹介をする関数"""
    return f"{name}さん、{age}歳です"

print(introduce("太郎"))           # 太郎さん、20歳です
print(introduce("花子", 25))       # 花子さん、25歳です
```

**コード解説:**

- `引数名=デフォルト値` でデフォルト値を設定
- 引数を省略するとデフォルト値が使われる
- 引数を指定すると、その値が使われる

**注意点（重要！）:**

```python
# 間違い（デフォルト引数が前にある）
def introduce(age=20, name):  # エラー！
    pass

# 正しい（デフォルト引数は後ろ）
def introduce(name, age=20):  # OK
    pass
```

**なぜデフォルト引数を使うのか？**

- よく使う値を省略できる（呼び出しが簡潔に）
- オプションの引数を作れる
- 関数の柔軟性が高まる

### クラス

**クラスとは何か？**

クラスは「設計図」のようなものです。同じ種類のオブジェクトをたくさん作りたいときに使います。

**例えで理解するクラス:**

- **クラス**: 誕生証の書類（設計図）
- **インスタンス**: 実際の人間（設計図から作られた実体）
- **属性**: 名前、年齢などその人固有のデータ
- **メソッド**: 挨拶する、歩くなどその人ができる動作

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

**コード解説:**

1. **`class Person:`** - クラスの定義（クラス名は大文字で始めるのが慣例）
2. **`__init__(self, ...)`** - 初期化メソッド（インスタンス作成時に自動呼び出される）
3. **`self.name = name`** - インスタンス変数の設定（`self.`をつけて属性にする）
4. **`self`** - インスタンス自身を表す（Python特有のルール）
5. **`person = Person("太郎", 30)`** - インスタンスの作成

**なぜクラスを使うのか？**

1. **データと処理をまとめる**: 関連するデータとメソッドを1つにまとめられる
2. **再利用**: 同じ設計図から何個でもインスタンスを作れる
3. **組織化**: 大きなプログラムを整理できる

**クラスを使わない場合（比較）:**

```python
# クラスを使わない（データが散らばる）
name1 = "太郎"
age1 = 30
name2 = "花子"
age2 = 25

# 関数は別に定義
def greet_person(name, age):
    return f"{name}です、{age}歳です"

# クラスを使う（データとメソッドがまとまっている）
person1 = Person("太郎", 30)
person2 = Person("花子", 25)
print(person1.greet())  # データとメソッドがセット
```

**`self`の役割（重要！）:**

```python
class Person:
    def __init__(self, name):
        self.name = name  # このインスタンスの名前

    def greet(self):
        # self = このインスタンス自身
        return f"私は{self.name}です"  # 自分の名前を使う

person1 = Person("太郎")
person2 = Person("花子")

print(person1.greet())  # 私は太郎です（person1のname）
print(person2.greet())  # 私は花子です（person2のname）
```

**実践的な例:**

```python
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        self.is_borrowed = False  # 最初は貸出中でない

    def borrow(self):
        """本を借りる"""
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        """本を返す"""
        self.is_borrowed = False

# 使用例
book = Book("Python入門", "著者", 2000)
if book.borrow():
    print(f"{book.title}を借りました")
```

### ファイル操作

**ファイルの読み込み**

```python
# ファイルを開いて読み込み
with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

**コード解説:**

- `open(ファイル名, モード, encoding=...)` でファイルを開く
- `"r"` は読み込みモード（read）
- `encoding="utf-8"` は文字コードの指定（日本語を扱うため必須）
- `with` 文を使うと、ファイルが自動的に閉じられます

**なぜ`with`を使うのか？**

```python
# 推奨（withを使う）
with open("file.txt", "r") as f:
    content = f.read()
# ここで自動的にファイルが閉じられる

# 非推奨（withを使わない）
f = open("file.txt", "r")
content = f.read()
f.close()  # 忘れるとファイルが開きっぱなしになる（バグの原因）
```

**ファイルへの書き込み**

```python
# ファイルに書き込み
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!\n")
```

**コード解説:**

- `"w"` は書き込みモード（write）
- 既存のファイルがある場合は**上書き**されます（注意！）
- 追記したい場合は `"a"` （append）を使います

**モード一覧:**

| モード | 説明 | ファイルがない場合 |
|--------|------|-------------------|
| `"r"` | 読み込み | エラー |
| `"w"` | 書き込み（上書き） | 新規作成 |
| `"a"` | 追記 | 新規作成 |
| `"x"` | 排他作成 | 既にあるとエラー |

### 例外処理

**例外とは何か？**

プログラム実行中に起こるエラーのことです。例外処理を書くことで、エラーが起きてもプログラムがクラッシュしなくなります。

```python
try:
    # 0で割る処理
    result = 10 / 0
except ZeroDivisionError:
    print("0で割ることはできません")
finally:
    print("処理を終了します")
```

**コード解説:**

- `try:` - エラーが起こるかもしれない処理
- `except エラー名:` - エラーが起きたときの処理
- `finally:` - エラーの有無に関わらず必ず実行される

**よくある例外:**

| 例外名 | 原因 |
|--------|------|
| `ZeroDivisionError` | 0で割った |
| `FileNotFoundError` | ファイルが見つからない |
| `ValueError` | 値が正しくない（int("abc")など） |
| `KeyError` | 辞書にキーがない |
| `IndexError` | リストの範囲外のインデックス |

**実践的な例外処理:**

```python
# ファイル読み込みの例外処理
try:
    with open("data.txt", "r", encoding="utf-8") as f:
        data = f.read()
except FileNotFoundError:
    print("ファイルが見つかりません")
    data = ""  # デフォルト値を設定
except Exception as e:
    print(f"予期しないエラー: {e}")
    data = ""
```

**なぜ例外処理を使うのか？**

1. **クラッシュ防止**: エラーでプログラムが終了しない
2. **ユーザー体験**: エラーメッセージを分かりやすく表示できる
3. **デバッグ**: どこでエラーが起きたか特定しやすい

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

**なぜFlaskを選ぶのか？**

| 特徴 | Flask | Django |
|------|-------|--------|
| 学習コスト | 低い | 高い |
| 自由度 | 高い（自分で選べる） | 低い（決まっている） |
| 最初のコード | 短い | 長い |
| 用途 | 小〜中規模 | 大規模 |
| 拡張性 | 必要なものを追加 | 最初から全部入り |

**Flaskが適している場合:**
- 学習用・プロトタイプ作成
- 小〜中規模のアプリ
- 自分で設計したい場合
- シンプルなAPIサーバー

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

**コード解説:**

1. **`import os` vs `from pathlib import Path`**
   - `os`: 古くからある方法（文字列でパスを扱う）
   - `Path`: 新しい方法（オブジェクトでパスを扱う）
   - **推奨**: `Path` を使う（`/` 演算子でパス結合ができる、OS間の違いを吸収）

2. **`from flask import ...`**
   - 必要なものだけをインポート（メモリ効率）
   - `Flask()` でインスタンス作成、`render_template()` でHTMLを返す
   - `request` はオブジェクト（インポート後に使う）

3. **`import config`**
   - 自作モジュールのインポート（`.py`拡張子は不要）
   - 設定値を一元管理するため

**なぜこのようにインポートするのか？**

```python
# 推奨（明示的インポート）
from flask import Flask, render_template
Flask("...")

# 非推奨（全てインポート）
from flask import *
# どの関数がどこから来たか分かりにくい
```

**インポートのベストプラクティス:**

| 方法 | 良い点 | 悪い点 |
|------|--------|--------|
| `import flask` | 名前空間が明確 | `flask.Flask`と書く必要がある |
| `from flask import Flask` | 短く書ける | 名前衝突の可能性 |
| `from flask import *` | 何も考えなくてよい | **何がインポートされるか不明** |

**Flaskアプリケーションの初期化**

```python
app = Flask(__name__,
            static_folder=str(config.STATIC_FOLDER),  # 静的ファイルのフォルダパス
            template_folder=str(config.TEMPLATE_FOLDER))  # テンプレートのフォルダパス

# __name__: 現在のモジュール名を指定（Flaskがリソースを見つけるために必要）
# static_folder: CSS/JSファイルの場所
# template_folder: HTMLテンプレートの場所
```

**コード解説:**

1. **`__name__` とは？**
   - Pythonが自動的に用意する変数
   - 現在のモジュール名が入っている（ここでは `'__main__'` か `'app'`）
   - Flaskはこれを使ってテンプレートや静的ファイルの場所を探します

2. **なぜパスを `str()` で変換するのか？**
   - `Path` オブジェクトを文字列に変換しています
   - Flaskは文字列パスを期待しています

**`__name__` の挙動:**

```python
# app.py で実行した場合
print(__name__)  # '__main__'

# 他のファイルから import した場合
print(__name__)  # 'app' （モジュール名）
```

**最小限のFlaskアプリ:**

```python
# 最小限（全てデフォルト）
from flask import Flask
app = Flask(__name__)

# 推奨（設定を明示）
from flask import Flask
app = Flask(__name__,
            static_folder='static',      # 明示的に指定
            template_folder='templates')  # 明示的に指定
```

**なぜ設定を明示するのか？**

- コードを見ただけで構成が分かる
- フォルダ構成を変えたときに修正しやすい
- デバッグ時に迷いにくい

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

**ルーティングとは何か？**

URLと関数を紐付ける仕組みです。「このURLにアクセスしたら、この関数を実行する」というマッピングです。

```python
@app.route('/')  # ルート定義：ルートとURLパターン
def index():  # ビュー関数：リクエストがあったときに実行される関数
    """ブックシェフ一覧ページ"""
    view_mode = request.cookies.get('view_mode', 'shelf')  # クッキーから表示モードを取得
    books = get_markdown_files()  # ブック一覧を取得
    return render_template('index.html', books=books, view_mode=view_mode)
    # HTMLテンプレートをレンダリングして返す
```

**コード解説:**

1. **`@app.route('/')`**
   - デコレータと呼ばれる構文
   - 関数の直前に書いて、URLパターンを指定します
   - `/` は「ルート」（トップページ）を意味します

2. **`request.cookies.get('view_mode', 'shelf')`**
   - `request` はFlaskが自動的に用意するオブジェクト
   - クッキーから`view_mode`を取得
   - なければデフォルト値`'shelf'`を使う

3. **`render_template(...)`**
   - テンプレートエンジン（Jinja2）でHTMLを生成
   - `books=books` でデータをテンプレートに渡す

**デコレータの仕組み:**

```python
# デコレータは「関数を修飾する」構文
@app.route('/')
def index():
    ...

# これは以下と同じようなことをしています
index = app.route('/')(index)
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

**コード解説:**

- `<filename>` - 文字列のパスパラメータ（何でもマッチ）
- `<int:page_num>` - 整数のパスパラメータ（数字のみ）
- 同じURLパターンで複数の`@app.route()`を書けます

**URLパラメータの例:**

| URL | ルート定義 | 受け取る値 |
|-----|-----------|-----------|
| `/book/sample` | `/book/<filename>` | `filename = "sample"` |
| `/book/sample/page/2` | `/book/<filename>/page/<int:page_num>` | `filename = "sample"`, `page_num = 2` |
| `/user/123` | `/user/<int:user_id>` | `user_id = 123` |

**パスパラメータの型指定:**

| 指定 | 説明 | マッチする例 |
|------|------|-------------|
| `<name>` | 文字列（デフォルト） | `abc`, `123` |
| `<int:id>` | 整数のみ | `123` （`abc`は404） |
| `<float:price>` | 小数のみ | `19.99` |
| `<path:subpath>` | `/`を含むパス | `a/b/c` |

**レスポンスの返し方**

| メソッド | 説明 | 使用例 | Content-Type |
|---------|------|--------|--------------|
| `render_template()` | HTMLを返す | ページ表示 | `text/html` |
| `jsonify()` | JSONを返す | APIレスポンス | `application/json` |
| `send_from_directory()` | ファイルを返す | 画像・CSS/JS配信 | ファイル次第 |
| `redirect()` | リダイレクト | ページ移動 | 302ステータス |

**実践例:**

```python
# HTMLページを返す
@app.route('/')
def index():
    return render_template('index.html')

# APIとしてJSONを返す
@app.route('/api/books')
def api_books():
    return jsonify(books=[...])

# ファイルを返す
@app.route('/image/<filename>')
def serve_image(filename):
    return send_from_directory('images', filename)

# リダイレクト
@app.route('/old-path')
def old_path():
    return redirect('/new-path')
```

---

## ユーティリティモジュール詳解

コードを機能別に分割して、再利用しやすくします。

**なぜモジュールを分割するのか？**

| 分割しない場合 | 分割する場合 |
|---------------|-------------|
| `app.py`が数千行になる | 各ファイルが数百行で管理しやすい |
| 機能ごとの責任が不明確 | ファイル名で責任範囲が明確 |
| テストが難しい | 各モジュールを個別にテスト可能 |
| 再利用できない | 他プロジェクトで使い回せる |

**モジュール分割のベストプラクティス:**

1. **1ファイル = 1クラス** （または1つの機能グループ）
2. **ファイル名は小文字のスネークケース** (`frontmatter_parser.py`)
3. **関連する関数をまとめる**
4. **循環インポートを避ける**

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

**コード解説:**

1. **`Path(__file__).resolve().parent`**
   - `__file__`: このファイルのパス
   - `.resolve()`: 絶対パスに変換
   - `.parent`: 親ディレクトリ（プロジェクトルート）

2. **`os.environ.get()`**
   - 環境変数を安全に取得
   - 変数がない場合はデフォルト値を使う

**なぜ環境変数を使うのか？**

```python
# 推奨（環境変数）
SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key'
# 本番: 環境変数で設定（コードに含まれない）
# 開発: デフォルト値を使う

# 非推奨（ハードコード）
SECRET_KEY = 'my-secret-key-12345'
# セキュリティリスク：コードが漏れると秘密の鍵も漏れる
```

**設定のベストプラクティス:**

| 設定項目 | 開発環境 | 本番環境 |
|----------|----------|----------|
| `SECRET_KEY` | 固定値でOK | **環境変数必須** |
| `DEBUG` | `True` | **必ず`False`** |
| `SESSION_COOKIE_SECURE` | `False` | `True`（HTTPS） |

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

**正規表現の解説:**

`r'^---\s*\n(.*?)\n---\s*\n(.*)$'` を分解すると：

| パート | 説明 |
|--------|------|
| `^---` | 行頭の `---` |
| `\s*\n` | 空白文字と改行 |
| `(.*?)` | YAML部分（キャプチャ）|
| `\n---` | 改行と閉じ `---` |
| `\s*\n` | 空白文字と改行 |
| `(.*)` | Markdown本文（キャプチャ）|
| `$` | 終端 |

**`re.DOTALL` の役割:**

```python
# DOTALLなし（.は改行にマッチしない）
pattern = re.compile(r'a.*b')
pattern.match('a\nb')  # マッチしない

# DOTALLあり（.は改行にマッチする）
pattern = re.compile(r'a.*b', re.DOTALL)
pattern.match('a\nb')  # マッチする
```

**なぜ正規表現を使うのか？**

1. **柔軟性**: 空白の数に寛容になる
2. **効率**: 一度の処理で分割と抽出ができる
3. **正確性**: 行頭・行末の指定で誤マッチを防ぐ

**`yaml.safe_load()` vs `yaml.load()`:**

```python
# 推奨（安全）
yaml.safe_load(yaml_text)

# 非推奨（危険）
yaml.load(yaml_text)
# 任意のPythonオブジェクトを実行できてしまう
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

**HTMLとは何か？**

HTML（HyperText Markup Language）は、Webページの「構造」を記述する言語です。「何をどこに配置するか」を決めます。

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

**コード解説:**

| 行 | 内容 | 説明 |
|----|------|------|
| `<!DOCTYPE html>` | ドキュメントタイプ | HTML5であることを宣言 |
| `<html lang="ja">` | ルート要素 | 日本語のページであることを指定 |
| `<head>` | ヘッド | ページのメタデータ（画面には表示されない）|
| `<body>` | ボディ | ページのコンテンツ（画面に表示される）|

**なぜ各要素が必要なのか？**

1. **`<!DOCTYPE html>`**
   - ブラウザに「最新のHTML標準でレンダリング」と指示する
   - ないと「互換モード」で古いブラウザのようにレンダリングされる

2. **`lang="ja"`**
   - スクリーンリーダー（アクセシビリティ）で言語を認識するため
   - 検索エンジンがページの言語を理解するため

3. **`<meta charset="UTF-8">`**
   - 文字化けを防ぐため
   - 日本語を扱うなら必須

**よく使うHTMLタグ**

| タグ | 説明 | 使用例 | いつ使う？ |
|-----|------|--------|----------|
| `<h1>`〜`<h6>` | 見出し | `<h1>大見出し</h1>` | 文章の構造を示す |
| `<p>` | 段落 | `<p>本文</p>` | テキストの段落 |
| `<a>` | リンク | `<a href="/page">リンク</a>` | 別ページへ移動 |
| `<img>` | 画像 | `<img src="image.jpg" alt="説明">` | 画像を表示 |
| `<ul>` `<ol>` | リスト | `<ul><li>項目</li></ul>` | 箇条書き・番号付きリスト |
| `<div>` | 区切り | `<div>コンテンツ</div>` | ブックレベルの汎用コンテナ |
| `<span>` | インライン | `<span>強調</span>` | インラインの汎用コンテナ |

**`<div>` vs `<span>`:**

```html
<!-- div: ブロック要素（前後に改行が入る） -->
<div>これはブロック</div>
<div>次のブロック</div>

<!-- span: インライン（改行なし） -->
<span>これは</span><span>インライン</span>
```

**HTMLの属性**

```html
<!-- id属性：ページ内で一意の識別子 -->
<div id="header">ヘッダー</div>

<!-- class属性：スタイル適用のためのクラス名 -->
<p class="description">説明文</p>

<!-- data属性：カスタムデータの埋め込み -->
<div data-user-id="123">ユーザー情報</div>
```

**コード解説:**

- `id`: ページ内で**一意**（同じIDを2回使ってはいけない）
- `class`: 何度でも使える（スタイル適用のグループ化）
- `data-*`: JavaScriptからデータを取得するために使う

**なぜ属性を使うのか？**

```html
<!-- idの用途 -->
<div id="header">...</div>
<a href="#header">ヘッダーへ</a> <!-- ページ内リンク -->

<!-- classの用途 -->
<p class="text-red">赤い文字</p>
<p class="text-red">これも赤い文字</p> <!-- 同じスタイル -->

<!-- data属性の用途 -->
<button data-action="delete">削除</button>
<!-- JavaScriptで data-action を取得して処理を分岐 -->
```

### CSSの基本

**CSSとは何か？**

CSS（Cascading Style Sheets）は、HTMLの「見た目」を指定する言語です。「色、サイズ、配置」を決めます。

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

**コード解説:**

- `h1`: セレクタ（「どの要素にスタイルを適用するか」）
- `{ ... }`: 宣言ブロック（スタイルの集合）
- `color`: プロパティ（「何を変えるか」）
- `#333333`: 値（「どう変えるか」）
- `/* ... */`: コメント（説明文）

**セレクタの種類:**

| セレクタ | 例 | 説明 | 詳細度 |
|----------|-----|------|--------|
| 要素型 | `h1` | 全ての`<h1>`要素 | 低（0,0,1）|
| クラス | `.title` | `class="title"`の要素 | 中（0,1,0）|
| ID | `#header` | `id="header"`の要素 | 高（1,0,0）|
| 属性 | `[type="text"]` | 特定属性を持つ要素 | 中（0,1,0）|

**CSS変数（カスタムプロパティ）**

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

**コード解説:**

- `:root`: ドキュメントのルート（変数を定義する場所）
- `--variable-name`: 変数名（`--`で始める）
- `var(--variable-name)`: 変数の使用

**なぜCSS変数を使うのか？**

```css
/* 推奨（CSS変数） */
:root {
    --primary: #f54e00;
}
.button {
    background: var(--primary);
}
.link {
    color: var(--primary);
}
/* テーマカラーを1箇所で変更できる */

/* 非推奨（直接指定） */
.button {
    background: #f54e00;
}
.link {
    color: #f54e00;
}
/* 変更する場合、全箇所を修正する必要 */
```

**CSSの詳細度（優先順位）**

```css
/* 詳細度の高いルールが優先される */
h1 { color: red; }          /* 詳細度: 0, 010 */
h1.title { color: blue; }    /* 詳細度: 0, 110 → 優先 */
```

**詳細度の計算方法:**

| ルール | ID | クラス | 要素 | 計 | 詳細度 |
|------|-----|--------|------|---|----------|
| `h1` | 0 | 0 | 1 | 0,0,1 | 低 |
| `.title` | 0 | 1 | 0 | 0,1,0 | 中 |
| `#header` | 1 | 0 | 0 | 1,0,0 | 高 |
| `h1.title` | 0 | 1 | 1 | 0,1,1 | 中+ |

**詳細度のトラブル例:**

```css
/* スタイルが効かない例 */
.title {
    color: blue;  /* 詳細度: 0,1,0 */
}
h1.title {
    color: red;   /* 詳細度: 0,1,1 → 優先される！ */
}

/* 解決策：!importantは最後の手段 */
.title {
    color: blue !important;  /* 強制的に適用 */
}
/* または詳細度を上げる */
h1.title {
    color: red;  /* 0,1,1 */
}
p.title {
    color: blue;  /* 0,1,1 */
}
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

**コード解説:**

1. **`const` vs `let` vs `var`**
   - `const`: 再代入不可（推奨デフォルト）
   - `let`: 再代入可能
   - `var`: 古い書き方（使わない）

2. **なぜ`const`を推奨するのか？**

```javascript
// 推奨（const）
const apiKey = 'xxx';
// apiKey = 'yyy';  // エラー！再代入は不可

// コードを見ただけで「変わらない値」だと分かる
// バグを未然に防げる

// letが必要な場合
let count = 0;
count = count + 1;  // 更新するならlet
```

**関数の定義**

```javascript
function greet(name) {
    return `こんにちは、${name}さん！`;
}

// アロー関数（ES6）
const add = (a, b) => a + b;
```

**コード解説:**

- `function`: 関数宣言の伝統的な書き方
- `() =>`: アロー関数（ES2015で導入）
- テンプレートリテラル `` `Hello, ${name}` `` で変数埋め込み

**function vs アロー関数:**

| 特徴 | function | アロー関数 |
|------|----------|-----------|
| 書き方 | `function add(a,b) {}` | `const add = (a,b) => {}` |
| this | 呼び出し方で変化 | 定義時のthisを継承 |
| コンストラクタ | 可能 | 不可 |
| 推奨 | メソッド | コールバック関数 |

**なぜアロー関数を使うのか？**

```javascript
// 短く書ける
const add = (a, b) => a + b;  // 1行で書ける

// functionの場合
function add(a, b) {
    return a + b;
}

// thisが継承される（コールバックで便利）
class Counter {
    constructor() {
        this.count = 0;
    }

    // アロー関数推奨
    increment = () => {
        this.count++;  // thisがクラスを指す
    }
}
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

**コード解説:**

1. **`querySelector()` vs `querySelectorAll()`**
   - `querySelector()`: 最初の1つだけ取得
   - `querySelectorAll()`: 全てを取得（NodeListとして返す）

2. **要素の操作メソッド**
   - `textContent`: テキスト内容の設定・取得
   - `classList.add()`: クラスを追加
   - `style`: インラインスタイルの設定

**なぜDOM操作が必要なのか？**

- HTMLは「静的」ですが、JavaScriptで「動的」に変更できます
- ユーザー操作に応じて画面を更新できる

**querySelectorの例:**

```html
<div class="button">ボタン1</div>
<div class="button">ボタン2</div>
<div class="button">ボタン3</div>

<script>
// querySelector: 最初の1つだけ
const firstButton = document.querySelector('.button');
console.log(firstButton.textContent);  // "ボタン1"

// querySelectorAll: 全て
const allButtons = document.querySelectorAll('.button');
console.log(allButtons.length);  // 3
</script>
```

**セレクタの種類:**

| セレクタ | 例 | 説明 |
|----------|-----|------|
| `.class` | `.button` | クラス名 |
| `#id` | `#header` | ID |
| `tag` | `div` | タグ名 |
| `[attr]` | `[data-id="123"]` | 属性値 |
| `tag.class` | `div.active` | タグとクラスの組み合わせ |

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

**コード解説:**

1. **`async () => {}`**
   - 非同期関数（async）のアロー関数
   - 中で`await`を使えるようにするため

2. **`await fetch(...)`**
   - 非同期処理の完了を待つ
   - サーバーからのレスポンスを待つ間、他の処理をブロックしない

3. **`btn.dataset.mode`**
   - HTMLの`data-mode`属性の値を取得
   - `data-*`属性はJavaScriptからデータを渡すのに使う

**非同期処理とは？**

```javascript
// 同期処理（コードが順番に実行される）
console.log('1');
const result = someFunction();  // ここで完了を待つ
console.log('2');  // someFunctionが終わってから実行

// 非同期処理（完了を待たずに次へ進む）
console.log('1');
async function asyncExample() {
    const result = await someAsyncFunction();  // ここで待つ
    console.log('2');
}
console.log('3');  // asyncExampleの完了を待たずに実行
```

**なぜ非同期処理を使うのか？**

- ユーザー操作をブロックしないため
- サーバー通信中も画面を操作できる
- 複数のリクエストを同時に送れる

**`fetch` APIの解説:**

```javascript
// 基本的な使い方
fetch(url, options)
    .then(response => response.json())
    .then(data => console.log(data));

// async/awaitを使う場合（推奨）
async function getData() {
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
}
```

**このコードの流れ:**

1. ユーザーがボタンをクリック
2. クリックイベントが発火
3. サーバーにリクエストを送信（`fetch`）
4. サーバーがレスポンスを返すのを待つ（`await`）
5. レスポンスを受信したら、画面を更新

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

**コード解説:**

- `async function`: 非同期関数を定義
- `await`: Promiseの完了を待つ
- `try...catch`: エラー処理

**非同期処理のイメージ:**

```
同期処理（レストラン）
1. 注文する
2. 料理ができるのを待つ（他の客は待たされる）
3. 料理を受け取る
4. 次の客を呼べる

非同期処理（コールセンター）
1. 電話がかかってくる
2. オペレーターが対応（他の電話も同時に受けられる）
3. 対応完了
```

**Promiseの基礎:**

```javascript
// Promiseは「将来完了する値」を表す
const promise = new Promise((resolve, reject) => {
    // 非同期処理
    setTimeout(() => {
        resolve('成功！');  // 成功したとき
        // reject('失敗');   // 失敗したとき
    }, 1000);
});

// 使い方
promise
    .then(result => console.log(result))  // 成功時
    .catch(error => console.log(error));   // 失敗時
```

**async/awaitはPromiseの糖衣構文:**

```javascript
// Promiseチェーン（古い書き方）
fetch('/api/books')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.log(error));

// async/await（新しい書き方・推奨）
async function loadData() {
    try {
        const response = await fetch('/api/books');
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.log(error);
    }
}
```

**なぜasync/awaitを使うのか？**

1. **読みやすさ**: 同期処理のような書き方で非同期処理が書ける
2. **エラー処理**: `try...catch`が使える
3. **変数への代入**: 中間結果を変数に保存しやすい
    } catch (error) {
        console.error('エラー:', error);
    }
}
```

---

## 動作解説

Bookshelf4MDの完全な動作フローを解説します。

**アプリケーション全体の仕組み**

Webアプリケーションは「リクエスト-レスポンス」モデルで動作します。

1. クライアント（ブラウザ）が**リクエスト**を送る
2. サーバー（Flask）がリクエストを**処理**する
3. サーバーが**レスポンス**を返す
4. クライアントがレスポンスを**表示**する

**なぜこのモデルなのか？**

- Webの基本的な仕組み（HTTPプロトコル）に基づいている
- サーバーは「待ち受け」状態で、誰かがリクエストを送るのを待つ
- 状態を保持しない（どのリクエストも独立して処理できる）

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

**各ステップの詳細:**

| ステップ | 何が起きている | なぜ必要？ |
|---------|---------------|-----------|
| `start.bat`実行 | バッチファイルがPythonを起動 | Windowsユーザーのための簡易起動手段 |
| `.venvのPython` | 仮想環境のPythonを使う | プロジェクト固有のパッケージを分離するため |
| `app.py`ロード | Flaskアプリケーションを読み込む | ルーティング設定などを適用するため |
| `config.py`読込込み | 設定値をメモリに展開 | 定数を一箇所で管理するため |
| モジュール初期化 | パーサーなどをインスタンス化 | 再利用可能な状態にするため |
| サーバー待機開始 | ポート5000でリッスン開始 | クライアントからの接続を待つため |

**なぜ仮想環境を使うのか？**

```python
# 仮想環境なし（グローバル）
pip install flask  # システム全体にインストール
# 他のプロジェクトとバージョンが競合するかも

# 仮想環境あり（.venv）
.venv\Scripts\activate
pip install flask  # このプロジェクト専用
# 他プロジェクトに影響しない
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

**各ステップの解説:**

1. **ブラウザアクセス**
   - ユーザーがURLを入力するか、リンクをクリック
   - ブラウザはHTTP GETリクエストを送信

2. **Flaskルーティング**
   - `@app.route('/')` デコレータがURLパスをマッチ
   - マッチしたら、対応する関数を呼び出す

3. **index()関数実行**
   - ここでデータ収集とテンプレート呼び出しを行う

4. **ファイルスキャン**
   - `config.MARKDOWN_DIR.glob('*.md')` で全MDファイルを取得

5. **フロントマター解析**
   - `FrontmatterParser` でYAML部分を抽出
   - タイトル、説明、カバー画像パスを取得

6. **BookInfo作成**
   - 必要な情報を辞書にまとめる
   - テンプレートに渡しやすい形式

7. **Cookie取得**
   - `request.cookies.get('view_mode', 'shelf')`
   - ユーザーの設定を記憶

8. **テンプレートレンダリング**
   - `render_template()` でJinja2にHTML生成を委譲
   - データをテンプレートに渡す

9. **Jinja2処理**
   - テンプレート内の `{{ 変数 }}` を実際の値に置換
   - `{% 制御構文 %}` を実行

10. **レスポンス返却**
   - 生成されたHTMLをHTTPレスポンスとして返す

11. **ブラウザレンダリング**
   - 受け取ったHTMLを解析（パーシング）
   - DOMツリーを構築
   - CSSを適用して画面に描画

12. **JavaScript初期化**
   - DOMContentLoadedイベント発火
   - `initViewToggle()`、`initSidebar()` などが実行

**なぜこのような流れなのか？**

- **関心の分離**: データ処理（Python）と表示（HTML/CSS）を分ける
- **テンプレートエンジン**: HTMLとデータを分離し、再利用しやすくする
- **非同期初期化**: HTML描画を待たずにJavaScriptを実行

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
