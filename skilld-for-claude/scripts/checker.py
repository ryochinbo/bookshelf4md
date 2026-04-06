#!/usr/bin/env python3
"""Bookshelf4MD形式チェッカー"""

import re
import json
import sys
from pathlib import Path

def check_filename(filepath):
    """ファイル名が英数字とハイフンのみかチェック"""
    name = filepath.stem
    if bool(re.match(r'^[a-zA-Z0-9-]+$', name)):
        return True, f"OK ({name})"
    else:
        return False, f"ファイル名に英数字とハイフン以外が含まれています: {name}"

def check_frontmatter(content):
    """YAMLフロントマターのチェック"""
    # ---で囲まれたYAMLフロントマターの存在確認
    frontmatter_pattern = r'^---\s*\n(.*?)\n---\s*\n'
    match = re.match(frontmatter_pattern, content, re.DOTALL)
    if not match:
        return False, "フロントマターが見つかりません"

    yaml_content = match.group(1)

    # 必須フィールドのチェック
    if 'title:' not in yaml_content:
        return False, "titleフィールドがありません"

    # coverパスの形式チェック（ある場合）
    if 'cover:' in yaml_content:
        cover_match = re.search(r'cover:\s*(.+)', yaml_content)
        if cover_match:
            cover_path = cover_match.group(1).strip()
            if not cover_path.startswith('/media_'):
                return False, f"coverパスが `/media_` 形式ではありません: {cover_path}"

    return True, "OK"

def check_page_splitting(content):
    """ページ分割が ## で行われているかチェック"""
    # ## で始まる行の数をカウント
    headings = re.findall(r'^##\s+', content, re.MULTILINE)

    if len(headings) < 1:
        return False, "## でのページ分割がありません"

    # # (単一の#) が使われていないか確認
    single_hashes = re.findall(r'^#\s[^#]', content, re.MULTILINE)
    if single_hashes:
        return False, f"単一の # が使われています（{len(single_hashes)}箇所）"

    return True, f"OK ({len(headings)} ページ)"

def check_media_paths(content):
    """メディアパスが /media_ 形式かチェック"""
    # 画像のチェック
    images = re.findall(r'!\[.*?\]\(([^)]+)\)', content)
    for img_path in images:
        if not img_path.startswith('/media_'):
            return False, f"画像パスが `/media_` 形式ではありません: {img_path}"

    # 動画のチェック
    videos = re.findall(r'<source[^>]+src=["\']([^"\']+)["\']', content)
    for video_path in videos:
        if not video_path.startswith('/media_'):
            return False, f"動画パスが `/media_` 形式ではありません: {video_path}"

    return True, "OK"

def check_code_blocks(content):
    """コードブロックに言語指定があるかチェック"""
    # ```lang または ```lang{...} のパターン
    code_blocks = re.findall(r'```(\w+)', content)

    if len(code_blocks) == 0:
        return True, "OK (コードブロックなし)"

    # すべてのコードブロックに言語指定があるか
    for lang in code_blocks:
        if lang.lower() in ['text', 'plain', '']:
            return False, f"コードブロックに言語指定がありません: {lang}"

    return True, f"OK ({len(code_blocks)} コードブロック)"

def grade_assertions(output_dir):
    """アサーションを実行して結果を返す"""
    md_files = list(Path(output_dir).glob('*.md'))
    if not md_files:
        return []

    results = []
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        checks = [
            ('filename', *check_filename(md_file)),
            ('frontmatter', *check_frontmatter(content)),
            ('page_splitting', *check_page_splitting(content)),
            ('media_paths', *check_media_paths(content)),
            ('code_blocks', *check_code_blocks(content))
        ]

        for check_name, passed, text in checks:
            results.append({
                'text': check_name,
                'passed': passed,
                'evidence': text
            })

    return results

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python checker.py <output_dir>")
        sys.exit(1)

    output_dir = sys.argv[1]
    results = grade_assertions(output_dir)

    # 結果をJSONで出力
    print(json.dumps(results, ensure_ascii=False, indent=2))
