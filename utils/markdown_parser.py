import markdown
from pygments import highlight
from pygments.lexers import get_lexer_by_name, TextLexer
from pygments.formatters import HtmlFormatter
from pygments.util import ClassNotFound


class MarkdownParser:
    """MarkdownをHTMLに変換するクラス"""

    def __init__(self):
        self.md = markdown.Markdown(
            extensions=[
                'fenced_code',
                'tables',
                'nl2br',
                'sane_lists',
                'codehilite',
                'attr_list',
            ],
            extension_configs={
                'codehilite': {
                    'linenums': False,
                    'css_class': 'code-highlight'
                }
            }
        )
        self.formatter = HtmlFormatter(
            style='github-dark',
            cssclass='code-highlight'
        )

    def parse(self, content):
        """
        MarkdownをHTMLに変換

        Args:
            content: Markdown形式の文字列

        Returns:
            str: HTMLに変換された文字列
        """
        self.md.reset()
        return self.md.convert(content)

    def render_code_block(self, code, language=None):
        """
        コードブロックをシンタックスハイライト付きでレンダリング

        Args:
            code: コード文字列
            language: プログラミング言語

        Returns:
            str: ハイライトされたHTML
        """
        if not language:
            language = 'text'

        try:
            lexer = get_lexer_by_name(language)
        except ClassNotFound:
            lexer = TextLexer()

        return highlight(code, lexer, self.formatter)

    def get_highlight_styles(self):
        """シンタックスハイライトのCSSを取得"""
        return self.formatter.get_style_defs('.code-highlight')
