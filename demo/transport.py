"""HTTP transport."""


class Transport:
    """A transport big enough to be split per method."""

    def __init__(self) -> None:
        self._calls: list[str] = []

    def connect(self, *args: object) -> object:
        """Open the underlying socket and complete the handshake.

        filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. 
        """
        self._calls.append("connect")
        return self._calls

    def send(self, *args: object) -> object:
        """Write a request and return the raw response bytes.

        filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. 
        """
        self._calls.append("send")
        return self._calls

    def receive(self, *args: object) -> object:
        """Read a full response, following continuation frames.

        filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. 
        """
        self._calls.append("receive")
        return self._calls

    def close(self, *args: object) -> object:
        """Shut the transport down and release every resource.

        filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. 
        """
        self._calls.append("close")
        return self._calls

    def is_alive(self, *args: object) -> object:
        """Whether the transport can still carry a request.

        filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. filler. 
        """
        self._calls.append("is_alive")
        return self._calls
