def shell_sort(arr):
    sublist_count = len(arr) // 2

    while sublist_count > 0:
        for start in range(sublist_count):
            gap_insertion_sort(arr, start, sublist_count)
        print("After increments of size:", sublist_count)
        print("Array is", arr)
        sublist_count //= 2


def gap_insertion_sort(arr, start, gap):
    for i in range(start + gap, len(arr), gap):
        current_value = arr[i]
        position = i

        while position >= gap and arr[position - gap] > current_value:
            arr[position] = arr[position - gap]
            position = position - gap

        arr[position] = current_value


if __name__ == '__main__':
    array = [2, 6, 7, 4, 1, 8, 5, 9, 3, 10, 15, 12, 13, 11, 14]
    shell_sort(array)
    print(array)
