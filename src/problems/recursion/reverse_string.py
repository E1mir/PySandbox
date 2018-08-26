from nose.tools import assert_equal


class TestReverse(object):

    def test(self, solution):
        assert_equal(solution('hello'), 'olleh')
        assert_equal(solution('hello world'), 'dlrow olleh')
        assert_equal(solution('123456789'), '987654321')

        print('PASSED ALL TEST CASES!')


def reverse(s):
    if s == "":
        return ""
    return s[len(s) - 1] + reverse(s[:len(s) - 1])


def reverse_2(s):
    if len(s) <= 1:
        return s
    return reverse(s[1:]) + s[0]


if __name__ == '__main__':
    print(reverse("Hello world"))
    t = TestReverse()
    t.test(reverse)
