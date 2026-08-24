"""plugins/social_watermark.py
Custom watermark provider for Social Media assets.
"""

from PIL import Image, ImageDraw


def social_watermark_factory(context):
    """Watermark provider factory.

    Args:
        context (dict): Contains 'target', 'size', 'name', 'language', 'homepage'.

    Returns:
        callable: A function that takes an Image and returns an Image.

    """

    def apply(img: Image.Image) -> Image.Image:
        # Ensure RGBA for compositing
        if img.mode != "RGBA":
            out = img.convert("RGBA")
        else:
            out = img.copy()

        draw = ImageDraw.Draw(out)
        w, h = out.size

        # Example: Draw a semi-transparent red circle at bottom right
        radius = min(w, h) // 10
        margin = int(min(w, h) * 0.05)

        draw.ellipse((w - margin - radius * 2, h - margin - radius * 2, w - margin, h - margin), fill=(255, 0, 0, 128))
        return out

    return apply


def setup(api):
    # Register the provider with a unique key 'social_mark'
    api.register_watermark("social_mark", social_watermark_factory)


def register(api):
    setup(api)
