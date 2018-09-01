import itertools
from collections import OrderedDict


def list_join_trick():
    """
    List joins without loop
    """
    some_list = [[1, 2, 3], [4, 5], [6], [7, 8, 9]]
    joined = sum(some_list, [])
    print(joined)
    # It would be better if you use itertools instead of sum func
    joined = list(itertools.chain.from_iterable(some_list))
    print(joined)


def list_tuple_unpacking():
    """
    List, tuple and set unpacking method
    """
    seq = [1, 2, 3, 4]
    *a, b, c = seq
    print(a, b, c)
    a, *b, c = seq
    print(a, b, c)
    a, b, *c = seq
    print(a, b, c)
    a, b, c, *d = seq
    print(a, b, c, d)
    a, b, c, d, *e = seq
    print(a, b, c, d, e)


def matrix_transposing():
    """
    Matrix transposing method (change row and column)
    If you regularly encounter similar problems, I strongly recommend to
    use NumPy library: http://www.numpy.org/
    """
    original = [
        ('a', 'b'),
        ('c', 'd'),
        ('e', 'f')
    ]
    """ Expectation is
    transposed = [
        ('a', 'c', 'e'), 
        ('b', 'd', 'f')
    ]
    """
    transposed = list(zip(*original))
    print(transposed)


def list_duplicate_removing():
    """
    Remove duplicate from list
    """
    items = [2, 2, 3, 3, 1, 7, 4, 5, 8, 9, 7, 6, 0]
    # without saving the order
    unique = list(set(items))
    print(unique)

    # with saving the order by using OrderedDict
    unique = list(OrderedDict.fromkeys(items).keys())
    print(unique)


def dict_sorting():
    """
    Sort dictionary by their values
    """
    d = {'apple': 40, 'orange': 80, 'banana': 70}
    sorted_l = sorted(d, key=d.get, reverse=False)
    print(sorted_l)


if __name__ == '__main__':
    dict_sorting()
