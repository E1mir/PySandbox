"""
Problem
Given a string,determine if it is compreised of all unique characters.
For example, the string 'abcde' has all unique characters and should return True.
The string 'aabcde' contains duplicate characters and should return false.
"""
from nose.tools import assert_equal


class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print('ALL TEST CASES PASSED')


def uni_char(string):
    chars = set()
    for letter in string:
        if letter in chars:
            return False
        else:
            chars.add(letter)
    return True


def uni_char_best(string):
    return len(set(string)) == len(string)


if __name__ == '__main__':
    t = TestUnique()
    t.test(uni_char)
    t.test(uni_char_best)
