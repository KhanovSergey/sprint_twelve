OPERATIONS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: y - x,
    '*': lambda x, y: x * y,
    '/': lambda x, y: y // x
}

class NoItemsException(Exception):
    def __init__(self):
        pass


class Stack:
    def __init__(self):
        self._array = []
        self._size = 0

    @property
    def is_empty(self):
        return self._size == 0

    def push(self, element):
        self._size += 1
        self._array.append(element)

    def pop(self):
        if self.is_empty:
            raise NoItemsException
        else:
            self._size -= 1
            return self._array.pop()


stack = Stack()

for value in input().split(' '):
    operation = OPERATIONS.get(value)
    stack.push(operation(stack.pop(), stack.pop()) if operation else int(value))

print(stack.pop())
