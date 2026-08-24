"""Sample batch plugin skeleton
Provides a batch orchestration stub.
"""

_meta = {"id": "sample_batch", "version": "0.1", "author": "dev"}


def register(api):
    def batch_runner(tasks, concurrency=4):
        print(f"[sample_batch] running {len(tasks)} tasks with concurrency={concurrency}")
        for t in tasks:
            # each task is a callable or dict describing a job
            print(f"[sample_batch] task: {t}")

    api.register_batch("simple_batch", batch_runner)


def unregister(api):
    try:
        api.unregister_target("simple_batch")
    except Exception:
        pass


def info():
    return _meta
