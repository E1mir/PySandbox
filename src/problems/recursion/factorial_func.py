import math


def fact(n):
    # base case

    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def fact_2(n):
    if n == 0:
        return 1
    r = 1
    for i in range(2, n + 1):
        r *= i

    return r


fact_3 = math.factorial

print(fact(100))
print(fact_2(100))
print(fact_3(100))
