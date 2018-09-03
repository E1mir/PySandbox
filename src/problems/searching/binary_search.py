def binary_search(arr, ele):
    first = 0
    last = len(arr) - 1

    found = False

    while first <= last and not found:
        mid = (first + last) // 2

        if arr[mid] == ele:
            found = True
        else:
            if ele < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found


def binary_search_recursive(arr, ele):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr) // 2

        if arr[mid] == ele:
            return True
        else:
            if ele < arr[mid]:
                return binary_search_recursive(arr[:mid], ele)
            else:
                return binary_search_recursive(arr[mid + 1:], ele)


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    r = binary_search(array, 22)
    r2 = binary_search_recursive(array, 22)
    print(r)
    print(r2)
