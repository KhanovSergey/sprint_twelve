class StackMax:
    def __init__(self):
        self.items = []
        self.max = []

    def push(self, item):
        if len(self.items) == 0:
            self.max.append(int(item))
        elif int(item) > self.max[len(self.items) - 1]:
            self.max.append(int(item))
        else:
            self.max.append(self.max[len(self.items) - 1])
        self.items.append(item)

    def isEmpty(self):
        return self.items == []


def get_max(self):
    if self.isEmpty():
        return 'None'
    return self.max[len(self.items) - 1]


def pop(self):
    if self.isEmpty():
        return 'error'
    self.max.pop()
    return self.items.pop()


def main():
    st_max = StackMax()
    res = []
    for _ in range(n):
        n_stack = input().split()
        if n_stack[0] == 'push':
            st_max.push(n_stack[1])
        if n_stack[0] == 'pop':
            if pop(st_max) == 'error':
                res.append('error')
        if n_stack[0] == 'get_max':
            res.append(get_max(st_max))

    for i in res:
        print(i)


if __name__ == '__main__':
    n = int(input())
    main()

