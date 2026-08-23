# Pixel Forge — Community releases

Public **binary-only** release channel for the free Community tier.

- **Dev SSOT (private):** `timejunky/r4it_pixel_forge` — never push application source here.
- **This repo:** README only on `main`. Customer downloads are **GitHub Release assets** built from the private dev tree.

## What belongs here

| Allowed on `main` | Allowed on GitHub Releases |
| --- | --- |
| This README | `PixelForge-<semver>-Setup.exe` |
| `.gitignore` | `PixelForge-Community-Setup.exe` (stable latest/download name) |
| | `PixelForge-<semver>-Setup.exe.sha256.txt` |

## What must never appear here

- Python source, `pyproject.toml`, `requirements*.txt`, `_info` trees
- ZIP/tar archives of source or PyInstaller onedir folders
- Payhip secrets, internal marketing, or dev tooling

GitHub auto-generates “Source code (zip/tar.gz)” from **this** repo only. Keeping `main`
limited to this README ensures those archives contain **no application code**.

## Operator publish (from dev machine)

```powershell
cd F:\r4it\dev\r4it_pixel_forge
python tools/build_desktop_bundle.py --clean --run-smoke
python tools/build_windows_installer.py
python tools/publish_community_release.py --dry-run
python tools/publish_community_release.py
python tools/audit_community_release.py
```

Pro / Trial builds use **streamingZebra** (`api.streamingzebra.com`), not this repo.
