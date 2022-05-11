
"""
ID 68148082
Code edits after the second review.
"""

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
    valid_keys(keys_input)
    keys_int = int(keys_input) * 2

    matrix = ''.join(matrix_input)
    valid_matrix(matrix)
    return data_count(keys_int, matrix)


if __name__ == '__main__':
    keys_input = input()
    matrix = ''
    matrix_input = [matrix + input() for _ in range(4)]
    print(main())
