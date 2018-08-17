"""
Problem

Given two strings, check to see if they are anagrams. An anagram is when
the two strings can be written using the exact same letters
(so you can just rearrange the letters to get a different phrase or word).

For example:

"public relations" is an anagram of "crap built on lies."

"clint eastwood" is an anagram of "old west action"

Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".

"""

from nose.tools import assert_equal


class AnagramTest(object):

    def test(self, sol):
        assert_equal(sol('go go go', 'gggooo'), True)
        assert_equal(sol('abc', 'cba'), True)
        assert_equal(sol('hi man', 'hi     man'), True)
        assert_equal(sol('aabbcc', 'aabbc'), False)
        assert_equal(sol('12  3', '1 2'), False)
        print("ALL TEST CASES PASSED")


def anagram_best_sol(first_str, second_str):
    first_str = str(first_str).replace(' ', '').lower()
    second_str = str(second_str).replace(' ', '').lower()

    return sorted(first_str) == sorted(second_str)


def anagram_implementation(first_str, second_str):
    first_str = str(first_str).replace(' ', '').lower()
    second_str = str(second_str).replace(' ', '').lower()

    if len(first_str) != len(second_str):
        return False

    cnt = {}

    for letter in first_str:
        if letter in cnt:
            cnt[letter] += 1
        else:
            cnt[letter] = 1

    for letter in second_str:
        if letter in cnt:
            cnt[letter] -= 1
        else:
            cnt[letter] = 1

    for k in cnt:
        if cnt[k] != 0:
            return False

    return True


if __name__ == '__main__':
    t = AnagramTest()
    t.test(anagram_best_sol)
    t.test(anagram_implementation)
