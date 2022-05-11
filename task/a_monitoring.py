"""
ID 68316918
"""


def main():
    for i in range(m_input):
        for j in range(n_input):
            print(matrix[j][i], end=' ')
        print('')


if __name__ == '__main__':
    n_input = int(input())
    m_input = int(input())
    matrix = ''
    matrix = [input().split(' ') for _ in range(n_input)]
    main()
