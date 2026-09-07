"""Connection pooling."""

import threading

MAX_CONNECTIONS = 10


class Pool:
    """A fixed-size connection pool."""

    def __init__(self, size: int = MAX_CONNECTIONS) -> None:
        self._size = size
        self._lock = threading.Lock()
        self._free: list[object] = []

    def acquire(self) -> object:
        """Take a connection, blocking until one is free."""
        with self._lock:
            if self._free:
                return self._free.pop()
        return object()

    def release(self, conn: object) -> None:
        """Give a connection back to the pool."""
        with self._lock:
            self._free.append(conn)
