"""
Problem
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'.
For this problem, you can falsely "compress" strings of single or double letters.
For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.

The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.
"""
from nose.tools import assert_equal


class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print('ALL TEST CASES PASSED')


# Run Tests
def compress_string(string):
    compressed = ""
    length = len(string)
    repeat_count = 1

    if length == 0:
        return ''

    for i in range(0, length - 1):
        current_idx = i
        next_idx = i + 1

        if string[current_idx] == string[next_idx]:
            repeat_count += 1
        else:
            compressed += "{}{}".format(string[current_idx], repeat_count)
            repeat_count = 1

        if next_idx == length - 1:
            compressed += "{}{}".format(string[next_idx], repeat_count)

    return compressed


def compress(s):
    r = ""
    l = len(s)

    if l == 0:
        return ""

    if l == 1:
        return s + "1"

    cnt = 1
    i = 1

    while i < l:
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            r = r + s[i - 1] + str(cnt)
            cnt = 1

        i += 1

    r = r + s[i - 1] + str(cnt)

    return r


if __name__ == '__main__':
    t = TestCompress()
    t.test(compress_string)
    t.test(compress)
