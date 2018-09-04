def bubble_sort(arr):
    for n in range(len(arr) - 1, 0, -1):
        for k in range(n):
            if arr[k] > arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]


if __name__ == '__main__':
    array = [2, 6, 7, 4, 1, 8, 5, 9, 3, 10, 15, 12, 13, 11, 14]
    bubble_sort(array)
    print(array)
