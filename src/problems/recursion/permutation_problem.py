from nose.tools import assert_equal
from itertools import permutations


class TestPerm(object):

    def test(self, solution):
        assert_equal(sorted(solution('abc')), sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        assert_equal(sorted(solution('dog')), sorted(['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']))
        print('All test cases passed.')


def permute(s):
    out = []
    # Base case
    if len(s) == 1:
        out = [s]
    else:
        # for every letter in string

        for i, let in enumerate(s):
            # For every permutation resulting from Step 2 and 3
            for perm in permute(s[:i] + s[i + 1:]):
                # print('Current letter is: {}'.format(let))
                # print('Perm is: {}'.format(perm))
                out += [let + perm]

    return out


if __name__ == '__main__':
    print(permute("abcd"))
    t = TestPerm()
    t.test(permute)