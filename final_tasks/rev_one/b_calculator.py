"""
ID 68503297
Code edits after the first review.
"""
import re
import sys


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
    OPERATIONS = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: y - x,
        '*': lambda x, y: x * y,
        '/': lambda x, y: y // x
    }

    stack = Stack()

    valid_line(line_in)

    for value in line_in.split(' '):
        operation = OPERATIONS.get(value)
        stack.push(operation(stack.pop(), stack.pop()) if operation else int(value))

    return stack.pop()


def valid_line(line_in):
    pat = re.compile(r"[-*/+0-9 ]+")
    if re.fullmatch(pat, line_in) is None:
        print(f'Необходимо ввести '
              f'числа и арифметические операции,'
              f' записаные через пробел.')
        sys.exit(1)


if __name__ == '__main__':
    line_in = input()
    print(calculator(line_in))
