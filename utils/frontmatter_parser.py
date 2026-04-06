import re
import yaml


class FrontmatterParser:
    """YAMLフロントマターを解析するクラス"""

    def __init__(self):
        self.pattern = re.compile(r'^---\s*\n(.*?)\n---\s*\n(.*)$', re.DOTALL)

    def parse(self, content):
        """
        Markdownコンテンツからフロントマターを解析

        Args:
            content: Markdownファイルの内容

        Returns:
            dict: {'frontmatter': dict, 'content': str}
        """
        match = self.pattern.match(content)

        if match:
            yaml_text, markdown_content = match.groups()
            try:
                frontmatter = yaml.safe_load(yaml_text) or {}
            except yaml.YAMLError:
                frontmatter = {}
            return {
                'frontmatter': frontmatter,
                'content': markdown_content.strip(),
                'has_frontmatter': True
            }

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
