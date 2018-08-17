"""
Problem
Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.

Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

Input:

finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
Output:

5 is the missing number
"""
from nose.tools import assert_equal
import collections


class TestFinder(object):

    def test(self, sol):
        assert_equal(sol([5, 5, 7, 7], [5, 7, 7]), 5)
        assert_equal(sol([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]), 5)
        assert_equal(sol([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]), 6)
        print('ALL TEST CASES PASSED')


def find_missed1(lst1, lst2):
    lst1.sort()
    lst2.sort()

    for num1, num2 in zip(lst1, lst2):
        if num1 != num2:
            return num1

    return lst1[-1]


def find_missed2(arr1, arr2):
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1


def find_missed_best(arr1, arr2):
    result = 0

    for num in arr1 + arr2:
        result ^= num  # using XOR operation
        print(result)

    return result


if __name__ == '__main__':
    a = find_missed1([5, 5, 7, 7], [5, 7, 7])
    b = find_missed2([5, 5, 7, 7], [5, 7, 7])
    c = find_missed_best([5, 5, 7, 7], [5, 7, 7])
    print(a)
    print(b)
    print(c)

    t = TestFinder()
    t.test(find_missed1)
    t.test(find_missed2)
    t.test(find_missed_best)
