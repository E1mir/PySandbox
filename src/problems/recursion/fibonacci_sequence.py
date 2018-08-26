# recursion
def fib_rec(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


# iteration
def fib_iter(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


c_n = 40
cache = [None] * (c_n + 1)


def fib_dyn(n):
    # base case
    if n == 0 or n == 1:
        return n

    # check cache
    if cache[n] is not None:
        return cache[n]

    # keep setting cache
    cache[n] = fib_dyn(n - 1) + fib_dyn(n - 2)

    return cache[n]


if __name__ == '__main__':
    # print(fib_rec(40)) # takes a lot of time
    print(fib_iter(40))
    print(fib_dyn(40))
