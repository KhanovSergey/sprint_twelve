"""
ID 68489898
"""
import sys


class Queue:

    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

        self.COMMANDS = {
            'push_front': self.push_front,
            'push_back': self.push_back,
            'pop_front': self.pop_front,
            'pop_back': self.pop_back
        }

    def is_empty(self):
        return self.size == 0

    def push_back(self, value: int):
        if self.size != self.max_n:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            raise OverflowError

    def push_front(self, value: int):
        if self.size != self.max_n:
            self.queue[self.head - 1] = value
            self.head = (self.head - 1) % self.max_n
            self.size += 1
        else:
            raise OverflowError

    def pop_back(self):
        if self.is_empty():
            raise IndexError
        qt = self.queue[self.tail - 1]
        self.queue[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_n
        self.size -= 1
        return qt

    def pop_front(self):
        if self.is_empty():
            raise IndexError
        qh = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return qh


def valid_count_comm(n):
    try:
        int(n)
    except ValueError:
        print("Необходимо ввести количество команд -"
              "целое число не превосходящее 100000.")
        sys.exit(1)


def valid_max_dec(m):
    try:
        int(m)
    except ValueError:
        print("Необходимо ввести максимальный размер дека -"
              "целое число не превосходящее 50 000.")
        sys.exit(1)


def main():
    valid_count_comm(n)
    valid_max_dec(m)

    queue = Queue(int(m))

    for _ in range(int(n)):
        command = input()
        operation, *value = command.split()
        if value:
            try:
                result = queue.COMMANDS[operation](int(*value))
                if result is not None:
                    print(result)
            except OverflowError:
                print('error')
        else:
            try:
                result = queue.COMMANDS[operation]()
                print(result)
            except IndexError:
                print('error')


if __name__ == '__main__':
    n = input()
    m = input()
    main()
