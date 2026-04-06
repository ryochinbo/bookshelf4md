import os
from pathlib import Path

# ベースディレクトリ
BASE_DIR = Path(__file__).resolve().parent

# Flask設定
SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
DEBUG = os.environ.get('FLASK_DEBUG', 'True') == 'True'

# ディレクトリ設定
MARKDOWN_DIR = BASE_DIR / 'mds'
MEDIA_DIR = BASE_DIR / 'static' / 'media'
STATIC_FOLDER = BASE_DIR / 'static'
TEMPLATE_FOLDER = BASE_DIR / 'templates'

# URL設定
APPLICATION_ROOT = '/'
PREFERRED_URL_SCHEME = 'http'

# セッション設定
SESSION_COOKIE_SECURE = False  # HTTPS時はTrueに
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'

# ファイルアップロード設定
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB

# nginx対応（ProxyFix用）
PROXY_FIX_COUNT = 1  # nginxのプロキシ階層数に合わせて調整
