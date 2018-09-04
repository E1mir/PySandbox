def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        position = i

        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1

        arr[position] = current_value


if __name__ == '__main__':
    array = [5, 7, 4, 4, 6, 8, 9, 0, 4, 2, 4]
    insertion_sort(array)
    print(array)
