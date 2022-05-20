"""
ID 68512232
Code edits after the first review.
"""
import sys


class Deck:

    def __init__(self, n):
        self.array = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = -1
        self.size = 0

        self.COMMANDS = {
            'push_front': self.push_front,
            'push_back': self.push_back,
            'pop_front': self.pop_front,
            'pop_back': self.pop_back
        }

    @property
    def is_empty(self):
        return self.size == 0

    def push_back(self, value: int):
        if self.size != self.max_n:
            self.tail = (self.tail + 1) % self.max_n
            self.array[self.tail] = value
            self.size += 1
        else:
            raise OverflowError

    def push_front(self, value: int):
        if self.size != self.max_n:
            self.head = (self.head - 1) % self.max_n
            self.array[self.head] = value
            self.size += 1
        else:
            raise OverflowError

    def pop_back(self):
        if self.is_empty:
            raise IndexError
        else:
            val = self.array[self.tail]
            self.tail = (self.tail - 1) % self.max_n
            self.size -= 1
            return val

    def pop_front(self):
        if self.is_empty:
            raise IndexError
        else:
            val = self.array[self.head]
            self.head = (self.head + 1) % self.max_n
            self.size -= 1
            return val


def valid_count_command(n):
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


def valid_command(operation, value):
    operation_val = {'push_back', 'push_front'}
    operation_not_val = {'pop_back', 'pop_front'}
    if operation in operation_val and abs(value) <= 1000:
        return
    elif operation in operation_not_val:
        return
    else:
        print(f'Необходимо ввести корректные команды и/или элементы.'
              f'Элементы - целое число, по модулю не превосходящее 1000.')
        sys.exit(1)


def main():
    valid_count_command(n)
    valid_max_dec(m)

    dec = Deck(int(m))

    for _ in range(int(n)):
        command = input()
        operation, *value = command.split()

        valid_command(operation, int(*value))

        if value:
            try:
                result = dec.COMMANDS[operation](int(*value))
                if result is not None:
                    print(result)
            except OverflowError:
                print('error')
        else:
            try:
                result = dec.COMMANDS[operation]()
                print(result)
            except IndexError:
                print('error')


if __name__ == '__main__':
    n = input()
    m = input()
    main()
