"""Sample plugin: translations + theme provider

Demonstrates the two most common plugin integration points:
  - register_translations(lang_code, mapping) — contribute i18n strings
  - register_theme_provider(theme_id, provider) — register a custom UI theme

The theme provider callable receives keyword arguments:
    app         QApplication instance
    store       SettingsStore (read-only access recommended)
    project_root absolute path to the project root directory
    dark        bool — True when dark mode is active in settings

Usage:
    Copy this folder to ~/.pixelforge/plugins/sample_translations_theme/

"""

_meta = {
    "id": "sample_translations_theme",
    "version": "0.1",
    "author": "dev",
    "description": "Example: custom translations and a theme provider",
}

_CATPPUCCIN_DARK_QSS = """
QMainWindow, QWidget { background-color: #1e1e2e; color: #cdd6f4; font-size: 13px; }
QTabWidget::pane { border: 1px solid #45475a; border-radius: 10px; background: #181825; }
QTabBar::tab { background: #313244; color: #a6adc8; border-radius: 8px 8px 0 0; padding: 8px 16px; margin-right: 4px; }
QTabBar::tab:selected { background: #181825; color: #cba6f7; font-weight: 600; }
QFrame#card { background: #181825; border: 1px solid #45475a; border-radius: 12px; padding: 12px; }
QPushButton#btnPrimary { background-color: #cba6f7; color: #11111b; border: 0; border-radius: 8px; font-weight: 600; }
QPushButton#btnPrimary:hover { background-color: #b4befe; }
QLineEdit, QComboBox { background: #313244; border: 1px solid #585b70; border-radius: 8px; color: #cdd6f4; padding: 5px 8px; }
QToolBar { background: #181825; border-bottom: 1px solid #45475a; }
QStatusBar { background: #11111b; border-top: 1px solid #45475a; }
QPushButton#workflowIndicator { color: #cba6f7; font-weight: 600; border: 1px solid transparent; border-radius: 6px; padding: 2px 10px; }
QPushButton#workflowIndicator:hover { border-color: #585b70; background: #313244; }
"""

_CATPPUCCIN_LIGHT_QSS = """
QMainWindow, QWidget { background-color: #eff1f5; color: #4c4f69; font-size: 13px; }
QTabWidget::pane { border: 1px solid #ccd0da; border-radius: 10px; background: #ffffff; }
QTabBar::tab { background: #dce0e8; color: #6c6f85; border-radius: 8px 8px 0 0; padding: 8px 16px; margin-right: 4px; }
QTabBar::tab:selected { background: #ffffff; color: #8839ef; font-weight: 600; }
QFrame#card { background: #ffffff; border: 1px solid #ccd0da; border-radius: 12px; padding: 12px; }
QPushButton#btnPrimary { background-color: #8839ef; color: #ffffff; border: 0; border-radius: 8px; font-weight: 600; }
QPushButton#btnPrimary:hover { background-color: #7c3aed; }
QLineEdit, QComboBox { background: #ffffff; border: 1px solid #ccd0da; border-radius: 8px; color: #4c4f69; padding: 5px 8px; }
QToolBar { background: #e6e9ef; border-bottom: 1px solid #ccd0da; }
QStatusBar { background: #dce0e8; border-top: 1px solid #ccd0da; }
QPushButton#workflowIndicator { color: #8839ef; font-weight: 600; border: 1px solid transparent; border-radius: 6px; padding: 2px 10px; }
QPushButton#workflowIndicator:hover { border-color: #ccd0da; background: #ffffff; }
"""


def _apply_sample_theme(*, app, store, project_root, dark: bool, **_kwargs):
    """Catppuccin-style theme with distinct palette and stylesheet."""
    try:
        from PySide6.QtGui import QPalette, QColor

        palette = app.palette()
        if dark:
            palette.setColor(QPalette.ColorRole.Window, QColor("#1e1e2e"))
            palette.setColor(QPalette.ColorRole.WindowText, QColor("#cdd6f4"))
            palette.setColor(QPalette.ColorRole.Base, QColor("#181825"))
            palette.setColor(QPalette.ColorRole.Text, QColor("#cdd6f4"))
            palette.setColor(QPalette.ColorRole.Button, QColor("#313244"))
            palette.setColor(QPalette.ColorRole.ButtonText, QColor("#cdd6f4"))
            palette.setColor(QPalette.ColorRole.Highlight, QColor("#89b4fa"))
            palette.setColor(QPalette.ColorRole.HighlightedText, QColor("#1e1e2e"))
            app.setPalette(palette)
            app.setStyleSheet(_CATPPUCCIN_DARK_QSS)
        else:
            palette.setColor(QPalette.ColorRole.Window, QColor("#eff1f5"))
            palette.setColor(QPalette.ColorRole.WindowText, QColor("#4c4f69"))
            palette.setColor(QPalette.ColorRole.Base, QColor("#ffffff"))
            palette.setColor(QPalette.ColorRole.Text, QColor("#4c4f69"))
            palette.setColor(QPalette.ColorRole.Button, QColor("#dce0e8"))
            palette.setColor(QPalette.ColorRole.ButtonText, QColor("#4c4f69"))
            palette.setColor(QPalette.ColorRole.Highlight, QColor("#1e66f5"))
            palette.setColor(QPalette.ColorRole.HighlightedText, QColor("#ffffff"))
            app.setPalette(palette)
            app.setStyleSheet(_CATPPUCCIN_LIGHT_QSS)
    except Exception as e:
        print(f"[sample_translations_theme] theme apply failed: {e}")


def register(api):
    api.register_translations(
        "en",
        {
            "sample_plugin_hello": "Hello from sample plugin",
            "sample_plugin_theme_name": "Sample theme (Catppuccin-style)",
        },
    )
    api.register_translations(
        "de",
        {
            "sample_plugin_hello": "Hallo vom Beispiel-Plugin",
            "sample_plugin_theme_name": "Beispiel-Thema (Catppuccin-Stil)",
        },
    )

    api.register_theme_provider(
        "sample-catppuccin",
        {
            "label": "Sample theme (Catppuccin-style)",
            "apply": _apply_sample_theme,
            "provides_stylesheet": True,
        },
    )


def unregister(api):
    pass


def info():
    return _meta
