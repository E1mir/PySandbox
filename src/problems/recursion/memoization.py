factorial_memo = {}


def fact(k):
    if k < 2:
        return 1

    if k not in factorial_memo:
        factorial_memo[k] = k * fact(k - 1)

    return factorial_memo[k]


print(fact(400))


class Memoize(object):

    def __init__(self, f):
        self.f = f
        self.memo = {}

    def __call__(self, *args, **kwargs):
        if args not in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]


def factorial(k):
    if k < 2:
        return 1

    return k * factorial(k - 1)


factorial_m = Memoize(factorial)

print(factorial_m(400))
