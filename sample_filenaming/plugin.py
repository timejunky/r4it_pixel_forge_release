"""Sample filenaming/attributes plugin.

Provides a filename scheme and default attributes (e.g., copyright, author).
"""

_meta = {"id": "sample_filenaming", "version": "0.1", "author": "dev"}


def _filenaming(context: dict):
    # context may include: target, size, format, name
    parts = [context.get("name", "asset"), context.get("target", "generic")]
    size = context.get("size")
    if isinstance(size, (list, tuple)):
        parts.append(f"{size[0]}x{size[1]}")
    elif size:
        parts.append(str(size))
    fmt = context.get("format")
    stem = "-".join(parts)
    return f"{stem}.{fmt}" if fmt else stem


def _attributes(context: dict):
    return {
        "copyright": context.get("copyright", "© 2025 Your Company"),
        "author": context.get("author", "Pixel Forge"),
    }


def register(api):
    if getattr(api, "register_filenaming", None):
        api.register_filenaming("sample_scheme", _filenaming)
    if getattr(api, "register_attributes", None):
        api.register_attributes("sample_defaults", _attributes)


def unregister(api):
    pass


def info():
    return _meta
