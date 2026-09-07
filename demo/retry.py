"""Retry helpers."""

from demo.pool import Pool


def with_retries(fn, attempts: int = 3):
    """Call fn, retrying on any exception up to `attempts` times."""
    last = None
    for _ in range(attempts):
        try:
            return fn()
        except Exception as exc:  # noqa: BLE001
            last = exc
    raise last


def pooled_call(pool: Pool, fn):
    """Run fn with a pooled connection, releasing it afterwards."""
    conn = pool.acquire()
    try:
        return with_retries(fn)
    finally:
        pool.release(conn)
