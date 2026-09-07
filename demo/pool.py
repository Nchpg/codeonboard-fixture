"""Connection pooling."""

import threading

MAX_CONNECTIONS = 10


class Pool:
    """A fixed-size connection pool."""

    def __init__(self, size: int = MAX_CONNECTIONS) -> None:
        self._size = size
        self._lock = threading.Lock()
        self._free: list[object] = []
        self._in_use = 0

    def acquire(self) -> object:
        """Take a connection, raising PoolFull past the configured size."""
        with self._lock:
            if self._free:
                self._in_use += 1
                return self._free.pop()
            if self._in_use >= self._size:
                raise PoolFull(f"pool exhausted at {self._size} connections")
            self._in_use += 1
        return object()

    def release(self, conn: object) -> None:
        """Give a connection back to the pool."""
        with self._lock:
            self._in_use -= 1
            self._free.append(conn)


class PoolFull(RuntimeError):
    """Raised when the pool has no capacity left."""
