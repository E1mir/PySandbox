"""
Task: Given 2 numbers a, b. Find sum all of numbers between [a, b], b included.

Input: a, b where a <= b. a, b from 1 to 10^9.
Output: sum between [a, b]

Example: a = 1, b = 3
Answer = 6
"""


def best_solution(a, b):
    if 1 <= a <= b:
        return sum_from_zero(b) - sum_from_zero(a) + a
    else:
        raise ValueError


def sum_from_zero(num):
    return (num * (num + 1)) // 2


def simple_solution(a, b):
    if 1 <= a <= b:
        return sum(range(a, b + 1))
    else:
        raise ValueError


if __name__ == '__main__':
    # s1 = simple_solution(6 ** 121, 10 ** 135)  # it takes a lot of time
    s1 = simple_solution(12, 562)
    print(s1)
    s2 = best_solution(6 ** 121, 10 ** 135)
    print(s2)
