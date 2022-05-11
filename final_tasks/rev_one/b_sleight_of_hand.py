# ID 68114327

import re
import sys


def data_count(t, matrix):
    numbers = []
    max_point = 0
    for i in range(1, 10):
        count = matrix.count(str(i))
        numbers.append(count)

    for i, value in enumerate(numbers):
        if value == 0:
            continue
        if int(value) <= t:
            max_point += 1
    return max_point


def valid_keys(keys):
    if not keys.isnumeric():
        print(f'Вы ввели {keys[0]}, требуется ввести число'
              f' от 1 до 5 включительно.')
        sys.exit(1)
    elif 5 < int(keys) or int(keys) < 1:
        print(f'Вы ввели {keys[0]}, требуется ввести число'
              f' от 1 до 5 включительно.')
        sys.exit(1)


def valid_matrix(matrix):
    pat = re.compile(r"[1-9.]+")
    if re.fullmatch(pat, matrix) is None:
        print(f'Необходимо ввести '
              f'число от 1 до 9 включительно, или точку.')
        sys.exit(1)


def main():
    keys = input()
    valid_keys(keys)
    keys_int = int(keys) * 2

    matrix = ''
    matrix = ''.join([matrix + input() for _ in range(4)])
    valid_matrix(matrix)
    print(data_count(keys_int, matrix))


if __name__ == '__main__':
    main()
