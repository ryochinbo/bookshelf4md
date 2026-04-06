import re
from .frontmatter_parser import FrontmatterParser


class PageSplitter:
    """Markdownを##見出しでページ分割するクラス"""

    def __init__(self):
        self.heading_pattern = re.compile(r'^##\s+(.+)$', re.MULTILINE)
        self.frontmatter_parser = FrontmatterParser()

    def split(self, content):
        """
        Markdownコンテンツを##見出しで分割

        Args:
            content: Markdownファイルの内容

        Returns:
            dict: {'pages': list, 'toc': list}
        """
        # フロントマターを解析
        parsed = self.frontmatter_parser.parse(content)
        markdown_content = parsed['content']
        frontmatter = parsed['frontmatter']

        # ##見出しで分割
        parts = self.heading_pattern.split(markdown_content)

        pages = []
        toc = []

        if len(parts) > 1:
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
                title = parts[i].strip()
                section_content = parts[i + 1].strip()
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
        else:
            # ##見出しがない場合
            pages.append({
                'title': frontmatter.get('title', 'コンテンツ'),
                'content': markdown_content,
                'index': 0
            })
            toc.append({
                'title': frontmatter.get('title', 'コンテンツ'),
                'page': 0
            })

        return {
            'pages': pages,
            'toc': toc,
            'frontmatter': frontmatter,
            'total_pages': len(pages)
        }
