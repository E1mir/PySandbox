"""
Problem
Given a string of words, reverse all the words. For example:

Given:

'This is the best'
Return:

'best the is This'
As part of this exercise you should remove all leading and trailing whitespace.
So that inputs such as:

'  space here'  and 'space here      '
both become:

'here space'
"""
from nose.tools import assert_equal


class ReversalTest(object):

    def test(self, sol):
        assert_equal(sol('    space before'), 'before space')
        assert_equal(sol('space after     '), 'after space')
        assert_equal(sol('   Hello John    how are you   '), 'you are how John Hello')
        assert_equal(sol('1'), '1')
        print("ALL TEST CASES PASSED")


def reverse_sentence_best_1(snt):
    return " ".join(reversed(snt.split()))


def reverse_sentence_best_2(snt):
    return " ".join(snt.split()[::-1])


def reverse_sentence_alg(snt):
    words = []
    length = len(snt)
    spaces = [' ', ]

    i = 0

    while i < length:

        if snt[i] not in spaces:

            word_start = i

            while i < length and snt[i] not in spaces:
                i += 1

            words.append(snt[word_start:i])

        i += 1

    # return " ".join(reversed(words))
    return final_output(words)


def final_output(words_list):
    result = ""
    for i in range(len(words_list) - 1, -1, -1):
        if i == 0:
            result += words_list[i]
        else:
            result += "{} ".format(words_list[i])

    return result


if __name__ == '__main__':
    s = "  hello    world,  this  is amazing!    "
    a = reverse_sentence_best_1(s)
    b = reverse_sentence_alg(s)
    print(b)
    # print(a)

    t = ReversalTest()

    t.test(reverse_sentence_best_1)
    t.test(reverse_sentence_best_2)
    t.test(reverse_sentence_alg)
