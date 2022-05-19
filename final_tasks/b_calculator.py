# https://ru.stackoverflow.com/questions/1292258/Стек-доработка-по-коду-питон-Нужна-помощь
#
# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self): #- 8:9
#         try:
#             return self.items.pop()
#         except IndexError:
#             raise IndexError('Недостаточно операндов для вычисления.')
#
#     def size(self):
#         return len(self.items)
#
#
# OPERATORS = {'+': lambda x, y: x + y,
#              '-': lambda x, y: x - y,
#              '*': lambda x, y: x * y,
#              '/': lambda x, y: x // y}
#
#
# def calculator(line, stack=None, operators=OPERATORS):
#     stack = Stack() if stack is None else stack
#     for element in line:
#         if element in operators:
#             el1, el2 = stack.pop(), stack.pop()
#             stack.push(operators[element](el2, el1))
#         else:
#             try:
#                 stack.push(int(element)) # - 29 строка
#             except:
#                 raise KeyError('WRONG_KEY')
#     return stack.pop()
#
#
# if __name__ == '__main__':
#     line = input().split()
#     print(calculator(line))

# ----------------------------------------------------------------

import math



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
             '*': lambda x, y: x * y,
             '/': lambda x, y: x / y,
             '%': lambda x, y: x % y,
             '^': lambda x, y: x ** y,
             '+': lambda x, y: x + y,
             '-': lambda x, y: x - y,
             }


# def MyInt(value):
#     if isinstance(value, str):
#         return int(value)
#     return math.floor(value)


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
    # from decimal import Decimal

    line = input().split()
    print(calculator(line))
    # for line in (
    # "10 2 4 * -", "12 5 /", "-1 3 /", "1.5 3.7 + 2.1 *", "2+3j -5-7j *", "2 3 ^ 3 %", "2 0 /", "1 2 3 +", "1 2 + *"):
    #     print(f'\n Выражение : "{line}"')
    #     line = line.split()
    #     for t in (int, MyInt, float, complex, Decimal):
    #         print(f"{t.__name__:>10} = ", end='')
    #         try:
    #             print(calculator(line, converter=t))
    #         except (KeyError, IndexError, ZeroDivisionError, TypeError) as err:
    #             print("Ошибка!", err)
