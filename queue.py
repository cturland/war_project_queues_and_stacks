class Queue:
    def __init__(self):
        """
        Initialise an empty queue.
        Internally uses a Python list.
        """
        self.items = []

    def is_empty(self):
        """
        Returns True if the queue is empty, False otherwise.
        """
        return len(self.items) == 0

    def enqueue(self, item):
        """
        Adds an item to the back of the queue.
        """
        self.items.append(item)

    def dequeue(self):
        """
        Removes and returns the item at the front of the queue.
        Raises IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")
        return self.items.pop(0)  # remove from the front

    def front(self):
        """
        Returns the item at the front without removing it.
        Raises IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot access front of an empty queue")
        return self.items[0]

    def size(self):
        """
        Returns the number of items currently in the queue.
        """
        return len(self.items)

    def __str__(self):
        """
        Returns a string representation of the queue,
        showing the front on the left and back on the right.
        """
        return f"Queue: {self.items}"
