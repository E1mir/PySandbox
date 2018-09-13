"""
Given a list of integers and a target number,
write a function that returns a boolean indicating
if its possible to sum two integers from the list to reach the target number
"""


def is_sum_in_list(lst, target):
    seen = set()

    for num in lst:
        num2 = target - num

        if num2 in seen:
            return True

        seen.add(num)

    return False


if __name__ == '__main__':
    a = is_sum_in_list([1, 4, 6, 8, 3, 6, 3, 2, 4, 5, 7, 9], 17)
    print(a)
