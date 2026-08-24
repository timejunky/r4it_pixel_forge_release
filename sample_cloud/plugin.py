"""Sample cloud storage plugin skeleton
Registers a storage backend named 'sample_s3' (skeleton only).
"""

_meta = {"id": "sample_cloud", "version": "0.1", "author": "dev"}


def register(api):
    def client_factory(config=None):
        # return a storage client object implementing minimal upload/download methods
        class Client:
            def upload(self, src, dest):
                print(f"[sample_cloud] pretend upload {src} -> {dest}")

            def download(self, src, dest):
                print(f"[sample_cloud] pretend download {src} -> {dest}")

        return Client()

    api.register_storage("sample_s3", client_factory)


def unregister(api):
    try:
        api.unregister_target("sample_s3")
    except Exception:
        pass


def info():
    return _meta
