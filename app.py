import os
from pathlib import Path
from flask import Flask, render_template, send_from_directory, jsonify, request
from werkzeug.middleware.proxy_fix import ProxyFix
import config

app = Flask(__name__,
            static_folder=str(config.STATIC_FOLDER),
            template_folder=str(config.TEMPLATE_FOLDER))

# nginx対応：ProxyFixミドルウェア
app.wsgi_app = ProxyFix(
    app.wsgi_app,
    x_for=config.PROXY_FIX_COUNT,
    x_proto=config.PROXY_FIX_COUNT,
    x_host=config.PROXY_FIX_COUNT,
    x_prefix=config.PROXY_FIX_COUNT
)

app.config.from_object(config)

# ディレクトリが存在しない場合は作成
config.MARKDOWN_DIR.mkdir(exist_ok=True)
config.MEDIA_DIR.mkdir(parents=True, exist_ok=True)

# ユーティリティをインポート
from utils.frontmatter_parser import FrontmatterParser
from utils.page_splitter import PageSplitter
from utils.markdown_parser import MarkdownParser

frontmatter_parser = FrontmatterParser()
page_splitter = PageSplitter()
markdown_parser = MarkdownParser()


def get_markdown_files():
    """mds/ディレクトリ内のMarkdownファイルを取得"""
    files = []
    for file_path in config.MARKDOWN_DIR.glob('*.md'):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            parsed = frontmatter_parser.parse(content)

            # ファイル名（拡張子なし）
            filename = file_path.stem

            # フロントマターから情報を取得
            title = frontmatter_parser.get_title(
                parsed,
                default=filename
            )
            description = frontmatter_parser.get_description(parsed)
            cover = frontmatter_parser.get_cover(parsed)

            # ページ数を計算
            split_result = page_splitter.split(content)
            page_count = split_result['total_pages']

            files.append({
                'filename': filename,
                'title': title,
                'description': description,
                'cover': cover,
                'page_count': page_count
            })

    # タイトル順にソート
    files.sort(key=lambda x: x['title'])
    return files


@app.route('/')
def index():
    """ブックシェフ一覧ページ"""
    view_mode = request.cookies.get('view_mode', 'shelf')
    books = get_markdown_files()
    return render_template('index.html', books=books, view_mode=view_mode)


@app.route('/set_view_mode/<mode>', methods=['GET', 'POST'])
def set_view_mode(mode):
    """表示モードを設定"""
    if mode not in ['shelf', 'list']:
        mode = 'shelf'
    response = jsonify({'status': 'ok', 'mode': mode})
    response.set_cookie('view_mode', mode, max_age=60*60*24*365)
    return response


@app.route('/book/<filename>')
@app.route('/book/<filename>/page/<int:page_num>')
def view_book(filename, page_num=1):
    """ブック詳細ページ"""
    file_path = config.MARKDOWN_DIR / f'{filename}.md'

    if not file_path.exists():
        return render_template('404.html'), 404

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # フロントマターを解析
    parsed = frontmatter_parser.parse(content)
    frontmatter = parsed['frontmatter']

    # ページ分割
    split_result = page_splitter.split(content)
    pages = split_result['pages']
    toc = split_result['toc']
    total_pages = split_result['total_pages']

    # ページ番号のチェック
    if page_num < 1 or page_num > total_pages:
        page_num = 1

    # 現在のページ
    current_page = pages[page_num - 1]

    # MarkdownをHTMLに変換
    html_content = markdown_parser.parse(current_page['content'])

    # 進捗を計算
    progress = (page_num / total_pages) * 100

    return render_template(
        'book.html',
        filename=filename,
        title=frontmatter.get('title', filename),
        pages=pages,
        toc=toc,
        total_pages=total_pages,
        current_page=current_page,
        current_page_num=page_num,
        html_content=html_content,
        progress=progress,
        highlight_styles=markdown_parser.get_highlight_styles()
    )


@app.route('/media/<path:filename>')
def serve_media(filename):
    """メディアファイルを配信（static/media/）"""
    return send_from_directory(config.MEDIA_DIR, filename)


@app.route('/media_mds/<path:filename>')
def serve_media_from_mds(filename):
    """メディアファイルを配信（mds/フォルダ内）"""
    return send_from_directory(config.MARKDOWN_DIR, filename)


@app.route('/api/books')
def api_books():
    """ブック一覧API（将来的な拡張用）"""
    books = get_markdown_files()
    return jsonify(books=books)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=config.DEBUG)
