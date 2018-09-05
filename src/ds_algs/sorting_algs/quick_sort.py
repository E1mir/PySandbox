def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)


def quick_sort_helper(arr, first, last):
    if first < last:
        split_point = partition(arr, first, last)
        quick_sort_helper(arr, first, split_point - 1)
        quick_sort_helper(arr, split_point + 1, last)


def partition(arr, first, last):
    pivot_value = arr[first]
    left_mark = first + 1
    right_mark = last

    done = False

    while not done:

        while left_mark <= right_mark and arr[left_mark] <= pivot_value:
            left_mark += 1

        while right_mark >= left_mark and arr[right_mark] >= pivot_value:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            arr[left_mark], arr[right_mark] = arr[right_mark], arr[left_mark]

    arr[first], arr[right_mark] = arr[right_mark], arr[first]

    return right_mark


if __name__ == '__main__':
    array = [2, 6, 7, 4, 1, 8, 5, 9, 3, 10, 15, 12, 13, 11, 14, 16]
    quick_sort(array)
    print(array)
