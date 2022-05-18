def fibonacciModulo(n, k):
    ab = [1, 1]
    d = (10 ** k)
    if n < 2:
        fib = 1
    else:
        for _ in range(n - 1):
            mod = (ab[0] + ab[1]) % d
            ab[0] = ab[1]
            ab[1] = mod
            fib = ab[1]

    return fib


if __name__ == '__main__':
    n, k = (int(i) for i in input().split())
    print(fibonacciModulo(n, k))
