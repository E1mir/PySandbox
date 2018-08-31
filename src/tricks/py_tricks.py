import itertools


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


if __name__ == '__main__':
    list_tuple_unpacking()
