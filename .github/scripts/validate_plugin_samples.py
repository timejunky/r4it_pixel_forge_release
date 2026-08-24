#!/usr/bin/env python3
"""Validate plugin.json sidecars on the public `plugins` branch (no Python import)."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ID_RE = re.compile(
    r"^(?:com\.r4it\.pixelforge\.external|pixelforge\.external)\.[a-z][a-z0-9_]*$"
)
REQUIRED = ("id", "name", "version", "api", "description", "provides", "entry")


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _manifest_paths(root: Path) -> list[Path]:
    found: list[Path] = []
    if not root.is_dir():
        return found
    for path in sorted(root.iterdir()):
        if not path.is_dir() or path.name.startswith("."):
            continue
        for candidate in [path / "plugin.json", *sorted(path.glob("*.plugin.json"))]:
            if candidate.is_file() and candidate not in found:
                found.append(candidate)
    return found


def _validate_one(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return [f"{path}: invalid JSON ({exc})"]
    if not isinstance(data, dict):
        return [f"{path}: manifest must be an object"]
    for key in REQUIRED:
        if key not in data or data.get(key) in (None, "", []):
            errors.append(f"{path}: missing {key}")
    plugin_id = str(data.get("id") or "")
    if plugin_id and not ID_RE.match(plugin_id):
        errors.append(f"{path}: id {plugin_id!r} is not pixelforge.external.*")
    if data.get("api") not in (1, "1"):
        errors.append(f"{path}: api must be 1")
    provides = data.get("provides")
    if provides is not None and (
        not isinstance(provides, list) or not all(isinstance(item, str) and item for item in provides)
    ):
        errors.append(f"{path}: provides must be a list of strings")
    entry = str(data.get("entry") or "plugin.py")
    parts = Path(entry).parts
    if ".." in parts or Path(entry).is_absolute():
        errors.append(f"{path}: entry must stay in the plugin folder")
        return errors
    entry_path = (path.parent / Path(entry).name).resolve()
    try:
        entry_path.relative_to(path.parent.resolve())
    except ValueError:
        errors.append(f"{path}: entry escapes the plugin folder")
        return errors
    if not entry_path.is_file():
        errors.append(f"{path}: entry {entry} does not exist")
    return errors


def main() -> int:
    root = _repo_root()
    manifests = _manifest_paths(root)
    if len(manifests) < 5:
        print(f"expected plugin samples, found {len(manifests)} manifests in {root}", file=sys.stderr)
        return 1
    errors: list[str] = []
    for path in manifests:
        errors.extend(_validate_one(path))
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"ok: {len(manifests)} plugin manifests")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
