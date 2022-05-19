class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):  # - 8:9
        try:
            return self.items.pop()
        except IndexError:
            raise IndexError('Недостаточно переменных или значений,'
                             ' над которыми проводится операция.')

    def size(self):
        return len(self.items)


OPERATORS = {
             '+': lambda x, y: x + y,
             '-': lambda x, y: x - y,
             '*': lambda x, y: x * y,
             '/': lambda x, y: x / y,
             '%': lambda x, y: x % y,
             '^': lambda x, y: x ** y
             }


def calculator(line, stack=None, converter=int, operators=OPERATORS):
    stack = Stack() if stack is None else stack
    for element in line:
        if element in operators:
            el1, el2 = stack.pop(), stack.pop()
            try:
                stack.push(converter(operators[element](el2, el1)))
            except ZeroDivisionError:
                raise ZeroDivisionError(f'Деление на 0 при вычислении {el2} {element} {el1}.')
            except TypeError:
                raise TypeError(f'Неподдерживаемая операция {element} для типа {converter.__name__}.')
        else:
            try:
                stack.push(converter(element))
            except:
                raise KeyError(
                    f'Невозможно преобразовать {element} в {converter.__name__} или неподдерживаемая операция.')
    if stack.size() > 1:
        raise IndexError('Некорректное выражение - в стеке остались элементы.')
    return stack.pop()


if __name__ == '__main__':
    line = input().split()
    print(calculator(line))
