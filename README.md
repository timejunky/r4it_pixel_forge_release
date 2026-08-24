# Pixel Forge — plugin samples

Example plugins for **Pixel Forge Pro**. This branch is **not** the Windows
installer. Do not merge `plugins` into `main`.

Installers stay on [`main`](https://github.com/timejunky/r4it_pixel_forge_release)
and [Releases](https://github.com/timejunky/r4it_pixel_forge_release/releases/latest).

## Install a sample (Pro)

1. Copy one folder into `%USERPROFILE%\.pixelforge\plugins\<name>\`.
2. Restart Pixel Forge.
3. Confirm it under **Help → Plugins…**.

Each sample is a folder with `plugin.json` + Python. The host reads the JSON
**before** it runs any Python.

User plugin ids: `pixelforge.external.<name>` or
`com.r4it.pixelforge.external.<name>`.

## Restricted API

User plugins may register watermarks, file naming, attributes, translations,
themes, extra sizes, validators/fixers, and search.

The host **skips** user plugins that only declare storage, batch jobs, extra
convert targets, workflows, audit sinks, or upscalers.

Reserved provider ids (`sample_text`, `image_overlay`, `verbose`, audit sinks)
cannot be claimed by user plugins.

These files are still Python. The host limits registration, not the language
runtime.

## Samples that run as user plugins

- `social_watermark` — demo overlay
- `sample_filenaming` — filename + attributes
- `sample_custom_sizes` — extra sizes
- `sample_validator_svg` — SVG warnings
- `sample_translations_theme` — i18n + theme

## Samples that document host-only hooks

`sample_cloud`, `sample_batch`, `sample_image_workflow`, and `sample_targets`
show reserved capabilities. Pixel Forge will not load them from
`~/.pixelforge/plugins`.

## License

MIT (see `LICENSE`).
