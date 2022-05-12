class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


stack = Stack()
stack.push('apple')
stack.push('banana')
stack.push('orange')

#stack.pop()
print(stack.pop())
print(stack.pop())
print(stack.pop())


# def main():
#     valid_keys(keys_input)
#     keys_int = int(keys_input) * 2
#
#     matrix = ''.join(matrix_input)
#     valid_matrix(matrix)
#     return data_count(keys_int, matrix)
#
#
# if __name__ == '__main__':
#     keys_input = input()
#     matrix = ''
#     matrix_input = [matrix + input() for _ in range(4)]
#     print(main())
