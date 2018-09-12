"""
Problem

Given a list of integers, write a function that will return a list,
in which for each index the element will be the product of all the integers except for the element at that index


For example, an input of [1,2,3,4] would return [24,12,8,6] by performing [2×3×4,1×3×4,1×2×4,1×2×3] *
"""


def index_prod(lst):
    output = [None] * len(lst)

    product = 1

    for i, n in enumerate(lst):
        output[i] = product
        product *= n

    product = 1

    for i, n in reversed(tuple(enumerate(lst))):
        output[i] *= product
        product *= n

    return output


def index_prod_2(lst):
    output = [None] * len(lst)

    product = 1
    i = 0

    while i < len(lst):
        output[i] = product
        product *= lst[i]
        i += 1

    product = 1
    i = len(lst) - 1

    while i >= 0:
        output[i] *= product
        product *= lst[i]
        i -= 1

    return output


if __name__ == '__main__':
    a = index_prod_2([1, 2, 3, 4, 5])
    print(a)
