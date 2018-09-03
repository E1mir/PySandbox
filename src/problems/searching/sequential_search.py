def sequential_search(array, element):
    pos = 0

    found = False

    while pos < len(array) and not found:
        if array[pos] == element:
            found = True
        else:
            pos += 1
    return found


def ordered_sequential_search(array, element):
    """
    Array must be ordered!
    """
    pos = 0
    found = False
    stopped = False
    while pos < len(array) and not found and not stopped:
        if array[pos] == element:
            found = True
        else:
            if array[pos] > element:
                stopped = True
            else:
                pos += 1
    return found


if __name__ == '__main__':
    searching_elem = 7
    arr = [1, 2, 4, 6, 23, 36, 25, 356, 245, 35, 245, 6, 7356, 6, 7]
    r1 = sequential_search(arr, searching_elem)
    print(r1)
    ordered_arr = sorted([1, 2, 4, 6, 23, 36, 25, 356, 245, 35, 245, 6, 7356, 6, 7])
    r2 = ordered_sequential_search(ordered_arr, searching_elem)
    print(r2)
