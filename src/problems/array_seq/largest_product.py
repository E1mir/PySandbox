"""
Problem
Given a list of integers, find the largest
product you could make from 3 integers in the list

Requirements
You can assume that the list will always have at least 3 integers


"""


def get_largest_product(lst):
    if len(lst) < 3:
        raise ValueError("List is too short")

    high = max(lst[0], lst[1])
    low = min(lst[0], lst[1])

    high_prod_2 = lst[0] * lst[1]
    low_prod_2 = lst[0] * lst[1]

    high_prod_3 = lst[0] * lst[1] * lst[2]

    for num in lst[2:]:
        high_prod_3 = max(high_prod_3, num * high_prod_2, num * low_prod_2)

        high_prod_2 = max(high_prod_2, num * high, num * low)
        low_prod_2 = min(low_prod_2, num * high, num * low)

        high = max(high, num)
        low = min(low, num)

    return high_prod_3


if __name__ == '__main__':
    lp = get_largest_product([1, 3, 4, 6, 7, 2, 8, 9, 4, 2, 3, 4, 6, 7])
    print(lp)
