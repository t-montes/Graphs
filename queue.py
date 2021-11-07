class Queue:

    def __init__(self):
        """
        Initializing Queue.
        """
        self.queue = []

    def isEmpty(self) -> bool:
        return True if len(self.queue) == 0 else False

    def front(self) -> int:
        return self.queue[-1]

    def rear(self) -> int:
        return self.queue[0]

    def enqueue(self, x: int) -> None:
        self.x = x
        self.queue.insert(0, x)       

    def dequeue(self) -> None:
        return self.queue.pop()

