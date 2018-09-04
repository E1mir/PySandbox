def bubble_sort(arr):
    for n in range(len(arr) - 1, 0, -1):
        for k in range(n):
            if arr[k] > arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]


if __name__ == '__main__':
    array = [5, 7, 4, 4, 6, 8, 9, 0, 4, 2, 4]
    bubble_sort(array)
    print(array)
