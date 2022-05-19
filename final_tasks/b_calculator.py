"""
ID 68490038
"""
OPERATIONS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: y - x,
    '*': lambda x, y: x * y,
    '/': lambda x, y: y // x
}


class Stack:
    def __init__(self):
        self.items = []
        self.size = 0

    @property
    def is_empty(self):
        return self.size == 0

    def push(self, element):
        self.size += 1
        self.items.append(element)

    def pop(self):
        if self.is_empty:
            raise IndexError
        else:
            self.size -= 1
            return self.items.pop()


def calculator(line_in):
    stack = Stack()
    for value in line_in:
        operation = OPERATIONS.get(value)
        stack.push(operation(stack.pop(), stack.pop()) if operation else int(value))

    return stack.pop()


if __name__ == '__main__':
    line_in = input().split(' ')
    print(calculator(line_in))
