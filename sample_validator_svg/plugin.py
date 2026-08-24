"""Sample SVG validator/fixer plugin.

Validator checks for a viewBox attribute and warns if missing.
Fixer returns the input path unchanged (placeholder for real optimization).
"""

_meta = {"id": "sample_validator_svg", "version": "0.1", "author": "dev"}


def _validate_svg(input_path: str):
    warnings = []
    try:
        with open(input_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        if "viewBox" not in content:
            warnings.append("SVG missing viewBox; scaling may be incorrect.")
        if "<script" in content:
            warnings.append("Embedded scripts detected; consider removing for safety.")
    except Exception as e:
        warnings.append(f"Failed to read SVG: {e}")
    return warnings


def _fix_svg(input_path: str, output_path: str | None = None):
    # Placeholder: copy through; real implementation could normalize, remove metadata, etc.
    return input_path


def register(api):
    if getattr(api, "register_validator", None):
        api.register_validator("svg_basic", _validate_svg)
    if getattr(api, "register_fixer", None):
        api.register_fixer("svg_basic", _fix_svg)


def unregister(api):
    # No-op; registry keyed by names and not exposed for removal here
    pass


def info():
    return _meta
