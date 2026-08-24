"""Sample custom size provider plugin.

Provides additional sizes based on a context dict, e.g., homepage/theme and target.
"""

_meta = {"id": "sample_custom_sizes", "version": "0.1", "author": "dev"}


def _custom_sizes(context: dict):
    # context keys may include: target (str), homepage (str), name (str)
    target = context.get("target")
    homepage = context.get("homepage")
    name = context.get("name", "")
    out = []

    # Example: typhoon theme hero banner
    if homepage == "typhoon" and "hero" in name.lower():
        out.append(
            {"size": (1920, 640), "formats": ["webp", "avif"], "notes": "Typhoon hero banner", "target": "web_hero"}
        )

    # Example: VS Code preferences for activity bar
    if target == "vscode_activity_bar":
        out.append({"size": 16, "formats": ["webp", "svg"], "notes": "Preferred formats for VS Code activity bar"})

    return out


def register(api):
    if getattr(api, "register_custom_sizes", None):
        api.register_custom_sizes("sample_custom", _custom_sizes)


def unregister(api):
    pass


def info():
    return _meta
