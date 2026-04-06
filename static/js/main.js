// ========================================
// Bookshelf4MD - Main JavaScript
// ========================================

(function() {
    'use strict';

    // ========================================
    // 表示モード切り替え
    // ========================================
    function initViewToggle() {
        const toggleButtons = document.querySelectorAll('.view-toggle-btn');
        const booksContainer = document.querySelector('.books-container');

        if (!toggleButtons.length || !booksContainer) return;

        toggleButtons.forEach(btn => {
            btn.addEventListener('click', async function() {
                const mode = this.dataset.mode;

                // クッキーを設定
                try {
                    const response = await fetch('/set_view_mode/' + mode, {
                        method: 'POST'
                    });
                    if (response.ok) {
                        // ボタンの状態を更新
                        toggleButtons.forEach(b => b.classList.remove('active'));
                        this.classList.add('active');

                        // コンテナのクラスを更新
                        booksContainer.classList.remove('shelf-mode', 'list-mode');
                        booksContainer.classList.add(mode + '-mode');
                    }
                } catch (error) {
                    console.error('Failed to set view mode:', error);
                }
            });
        });

        // リストモードでカードクリックを処理
        document.querySelectorAll('.book-card').forEach(card => {
            card.addEventListener('click', function(e) {
                // リンク自体がクリックされた場合は無視
                if (e.target.closest('a')) return;

                const filename = this.dataset.filename;
                if (filename) {
                    window.location.href = '/book/' + filename;
                }
            });
        });
    }

    // ========================================
    // サイドバー（目次）
    // ========================================
    function initSidebar() {
        const sidebar = document.getElementById('sidebar');
        const sidebarToggle = document.getElementById('sidebarToggle');
        const sidebarClose = document.getElementById('sidebarClose');

        if (!sidebar) return;

        // トグルボタン
        if (sidebarToggle) {
            sidebarToggle.addEventListener('click', function() {
                sidebar.classList.toggle('open');
            });
        }

        // 閉じるボタン
        if (sidebarClose) {
            sidebarClose.addEventListener('click', function() {
                sidebar.classList.remove('open');
            });
        }

        // メインコンテンツクリックで閉じる（モバイル）
        const bookMain = document.querySelector('.book-main');
        if (bookMain) {
            bookMain.addEventListener('click', function() {
                if (window.innerWidth <= 900) {
                    sidebar.classList.remove('open');
                }
            });
        }
    }

    // ========================================
    // コピーボタン
    // ========================================
    function initCopyButtons() {
        // 既存のコードブロックにコピーボタンを追加
        addCopyButtonsToExistingBlocks();

        // MutationObserverで動的に追加されるコードブロックを監視
        if (document.querySelector('.book-page')) {
            const observer = new MutationObserver(function(mutations) {
                mutations.forEach(function(mutation) {
                    if (mutation.addedNodes.length) {
                        addCopyButtonsToExistingBlocks();
                    }
                });
            });

            observer.observe(document.querySelector('.book-page'), {
                childList: true,
                subtree: true
            });
        }
    }

    function addCopyButtonsToExistingBlocks() {
        const codeBlocks = document.querySelectorAll('pre code');

        codeBlocks.forEach(function(codeBlock) {
            const pre = codeBlock.parentElement;
            if (pre.classList.contains('has-copy-button')) return;

            pre.classList.add('has-copy-button');

            // wrapperを作成
            const wrapper = document.createElement('div');
            wrapper.className = 'code-block-wrapper';

            // headerを作成
            const header = document.createElement('div');
            header.className = 'code-header';

            // 言語を取得
            const language = codeBlock.className.match(/language-(\w+)/);
            const langLabel = language ? language[1] : 'code';

            const langSpan = document.createElement('span');
            langSpan.className = 'code-language';
            langSpan.textContent = langLabel;

            const copyBtn = document.createElement('button');
            copyBtn.className = 'copy-button';
            copyBtn.textContent = 'コピー';
            copyBtn.setAttribute('aria-label', 'コードをコピー');

            header.appendChild(langSpan);
            header.appendChild(copyBtn);

            // preの前にwrapperを挿入
            pre.parentNode.insertBefore(wrapper, pre);

            // wrapperにheaderとpreを追加
            wrapper.appendChild(header);
            wrapper.appendChild(pre);

            copyBtn.addEventListener('click', function() {
                copyCode(codeBlock, copyBtn);
            });
        });
    }

    async function copyCode(codeBlock, button) {
        const code = codeBlock.textContent;

        try {
            await navigator.clipboard.writeText(code);
            button.textContent = 'コピーしました!';
            button.classList.add('copied');

            setTimeout(function() {
                button.textContent = 'コピー';
                button.classList.remove('copied');
            }, 2000);
        } catch (error) {
            console.error('Copy failed:', error);

            // フォールバック
            const textarea = document.createElement('textarea');
            textarea.value = code;
            textarea.style.position = 'fixed';
            textarea.style.opacity = '0';
            document.body.appendChild(textarea);
            textarea.select();
            try {
                document.execCommand('copy');
                button.textContent = 'コピーしました!';
                button.classList.add('copied');
                setTimeout(function() {
                    button.textContent = 'コピー';
                    button.classList.remove('copied');
                }, 2000);
            } catch (e) {
                button.textContent = '失敗';
            }
            document.body.removeChild(textarea);
        }
    }

    // ========================================
    // キーボードナビゲーション
    // ========================================
    function initKeyboardNavigation() {
        document.addEventListener('keydown', function(e) {
            // ブックページでない場合は無視
            if (!window.currentPageNum || !window.totalPages) return;

            // 入力フィールド内では無視
            if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

            // 前のページ
            if ((e.key === 'ArrowLeft' || e.key === 'b' || e.key === 'B') && window.currentPageNum > 1) {
                const prevUrl = '/book/' + window.filename + '/page/' + (window.currentPageNum - 1);
                window.location.href = prevUrl;
            }
            // 次のページ
            else if ((e.key === 'ArrowRight' || e.key === 'n' || e.key === 'N') && window.currentPageNum < window.totalPages) {
                const nextUrl = '/book/' + window.filename + '/page/' + (window.currentPageNum + 1);
                window.location.href = nextUrl;
            }
        });
    }

    // ========================================
    // コードブロックスタイル
    // ========================================
    function addCodeBlockStyles() {
        const style = document.createElement('style');
        style.textContent = `
            .code-block-wrapper {
                margin: 24px 0;
                border: 1px solid rgba(38, 37, 30, 0.1);
            }

            .code-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 8px 12px;
                background: #e6e5e0;
                border-bottom: 1px solid rgba(38, 37, 30, 0.1);
            }

            .code-language {
                font-family: ui-monospace, monospace;
                font-size: 11px;
                color: rgba(38, 37, 30, 0.35);
                text-transform: uppercase;
                letter-spacing: 0.5px;
            }

            .copy-button {
                background: transparent;
                border: none;
                color: rgba(38, 37, 30, 0.55);
                font-size: 11px;
                cursor: pointer;
                padding: 4px 8px;
                transition: all 0.15s;
            }

            .copy-button:hover {
                background: #e1e0db;
                color: #26251e;
            }

            .copy-button.copied {
                color: #1f8a65;
            }

            /* Pygments code-highlightの背景色を統一 */
            .code-block-wrapper .code-highlight {
                background: #1a1915 !important;
            }

            .code-block-wrapper .code-highlight pre {
                background: #1a1915 !important;
                margin: 0 !important;
                padding: 16px !important;
                border: none !important;
                border-radius: 0 !important;
            }

            .code-block-wrapper .code-highlight code {
                background: transparent !important;
                border-radius: 0 !important;
            }
        `;
        document.head.appendChild(style);
    }

    // ========================================
    // スムーズスクロール
    // ========================================
    function initSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
            anchor.addEventListener('click', function(e) {
                const href = this.getAttribute('href');
                if (href === '#') return;

                const target = document.querySelector(href);
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    }

    // ========================================
    // 初期化
    // ========================================
    document.addEventListener('DOMContentLoaded', function() {
        initViewToggle();
        initSidebar();
        initCopyButtons();
        initKeyboardNavigation();
        initSmoothScroll();
        addCodeBlockStyles();
    });

})();
