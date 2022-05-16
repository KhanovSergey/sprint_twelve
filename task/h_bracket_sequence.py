# def is_correct_bracket_seq(text):
#     while '()' in text or '[]' in text or '{}' in text:
#         text = text.replace('()', '')
#         text = text.replace('[]', '')
#         text = text.replace('{}', '')
#
#     # Возвращаем True, если text с пустой строкой
#     return not text

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]


def is_correct_bracket_seq():
    brackets_three_types = {'(': ')', '{': '}', '[': ']'}
    s = Stack()
    for i in bracket_seq:
        if i in brackets_three_types.keys():
            s.push(i)
        elif not s.isEmpty() and brackets_three_types[s.peek()] == i:
            s.pop()
        else:
            s.push(i)
            break
    return s


if __name__ == '__main__':
    bracket_seq = list(input())
    if is_correct_bracket_seq().isEmpty():
        print('True')
    else:
        print('False')


