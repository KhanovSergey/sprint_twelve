# https://translated.turbopages.org/proxy_u/en-ru.ru.8aec7c55-628392f5-0d9e636b-74722d776562/https/www.geeksforgeeks.org/fibonacci-number-modulo-m-and-pisano-period/
# def pisanoPeriod(m):
#     previous, current = 0, 1
#     for i in range(0, m * m):
#         previous, current = current, (previous + current) % m
#
#         # A Pisano Period starts with 01
#         if (previous == 0 and current == 1):
#             return i + 1
#
#
# # Calculate Fn mod m
# def fibonacciModulo(n, m):
#     # Getting the period
#     pisano_period = pisanoPeriod(m)
#
#     # Taking mod of N with
#     # period length
#     n = n % int(pisano_period)
#
#     previous, current = 0, 1
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     for i in range(n - 1):
#         previous, current = current, previous + current
#
#     return (current % m)
#
#
# if __name__ == '__main__':
#     n, k = (int(i) for i in input().split())
#     print(fibonacciModulo(n, k))

def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current \
            = current, (previous + current) % m

        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1


# Calculate Fn mod m
def fibonacciModulo(n, m):
    # Getting the period
    pisano_period = pisanoPeriod(m)

    # Taking mod of N with
    # period length
    print(pisano_period)
    print(type(pisano_period))
    print(type(n))
    n = n % pisano_period

    previous, current = 0, 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    for i in range(n - 1):
        previous, current \
            = current, previous + current

    return (current % m)


# Driver Code
if __name__ == '__main__':
    n, m = (int(i) for i in input().split())
    print(n, m)
    print(fibonacciModulo(n, m))