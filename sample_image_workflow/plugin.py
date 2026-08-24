"""Sample image workflow plugin
Registers a simple pre/post processing hook for images.
"""

_meta = {"id": "sample_image_workflow", "version": "0.1", "author": "dev"}


def register(api):
    def workflow(img_path):
        print(f"[sample_image_workflow] processing {img_path}")

    api.register_image_workflow("noop_workflow", workflow)


def unregister(api):
    try:
        api.unregister_target("noop_workflow")
    except Exception:
        pass


def info():
    return _meta
