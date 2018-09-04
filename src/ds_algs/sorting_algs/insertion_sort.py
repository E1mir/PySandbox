def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        position = i

        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1

        arr[position] = current_value


if __name__ == '__main__':
    array = [2, 6, 7, 4, 1, 8, 5, 9, 3, 10, 15, 12, 13, 11, 14]
    insertion_sort(array)
    print(array)
