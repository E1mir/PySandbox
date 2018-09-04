def selection_sort(arr):
    for fill_slot in range(len(arr) - 1, 0, -1):
        position_of_max = 0

        for location in range(1, fill_slot + 1):
            if arr[location] > arr[position_of_max]:
                position_of_max = location

        arr[fill_slot], arr[position_of_max] = arr[position_of_max], arr[fill_slot]


if __name__ == '__main__':
    array = [5, 7, 4, 4, 6, 8, 9, 0, 4, 2, 4]
    selection_sort(array)
    print(array)
