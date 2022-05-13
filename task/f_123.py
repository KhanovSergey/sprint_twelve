class StackMax:
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


# stack = StackMax()
# stack.push('apple')
# stack.push('banana')
# stack.push('orange')
#
# print(stack.pop())

n = 8
n_stack = ['get_max',
           'push 7',
           'pop',
           'push -2',
           'push -1',
           'pop',
           'get_max',
           'get_max'
           ]
stack = StackMax()
for i in range(len(n_stack)):
    stack.push(n_stack[i])

print(stack.size())
print(stack.peek())
# stack.push(n_stack[0])
# stack.push(n_stack[1])
# stack.push(n_stack[2])

# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
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
