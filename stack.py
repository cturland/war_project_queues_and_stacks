class Stack:
    def __init__(self):
        """
        Initialise an empty stack.
        Internally uses a Python list.
        """
        self.items = []

    def is_empty(self):
        """
        Returns True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def push(self, item):
        """
        Adds an item to the top of the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Removes and returns the top item from the stack.
        Raises an IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        return self.items.pop()

    def peek(self):
        """
        Returns the top item without removing it.
        Raises an IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot peek into an empty stack")
        return self.items[-1]

    def size(self):
        """
        Returns the number of items currently in the stack.
        """
        return len(self.items)

    def __str__(self):
        """
        Returns a string representation of the stack,
        showing the bottom element on the left and top on the right.
        """
        return f"Stack: {self.items}"
