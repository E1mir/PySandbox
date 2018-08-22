"""
Problem Statement
Given a string of opening and closing parentheses,
check whether it’s balanced.
We have 3 types of parentheses:
round brackets: (), square brackets: [], and curly brackets: {}.
Assume that the string doesnt contain any other character than
these, no spaces words or numbers.
As a reminder, balanced parentheses require every opening parenthesis to be
closed in the reverse order opened.
For example ‘([])’ is balanced but ‘([)]’ is not.

You can assume the input string has no spaces.
"""
from nose.tools import assert_equal


class TestBalanceCheck(object):

    def test(self, sol):
        assert_equal(sol('[](){([[[]]])}('), False)
        assert_equal(sol('[{{{(())}}}]((()))'), True)
        assert_equal(sol('[[[]])]'), False)
        print('ALL TEST CASES PASSED')


def check_balance(s):
    if len(s) % 2 != 0:
        return False
    opening = {'(', '[', '{'}
    matches = {('(', ')'), ('[', ']'), ('{', '}')}

    stack = []

    for paren in s:

        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False

            last_open = stack.pop()

            if (last_open, paren) not in matches:
                return False

    return len(stack) == 0


if __name__ == '__main__':
    t = TestBalanceCheck()
    print(check_balance('[{{{(())}}}]((()))'))
    t.test(check_balance)
