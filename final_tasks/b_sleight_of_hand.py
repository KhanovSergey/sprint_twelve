# ID 68065846

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
    print(max_point)


def main():
    t = int(input()) * 2
    matrix = ''
    matrix = ''.join([matrix + input() for _ in range(4)])
    data_count(t, matrix)


if __name__ == '__main__':
    main()
