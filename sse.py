import queue


class SSEMessageQueue:
    def __init__(self):
        self.listeners = []

    def listen(self):
        q = queue.Queue(maxsize=5)
        self.listeners.append(q)
        return q

    def announce(self, data: str, event: str = "update"):
        message = self.format_sse(data, event)
        for i in reversed(range(len(self.listeners))):
            try:
                self.listeners[i].put_nowait(message)
            except queue.Full:
                del self.listeners[i]

    @staticmethod
    def format_sse(data: str, event=None) -> str:
        message = f"data: {data}\n\n"
        if event is not None:
            message = f"event: {event}\n{message}"
        return message
