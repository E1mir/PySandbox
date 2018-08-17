import ctypes
import sys
import prettytable


class DynamicArray(object):

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, idx):
        if not 0 <= idx < self.n:  # if index out of bounds
            return IndexError('Index is out of bounds!')

        return self.A[idx]

    def append(self, element):

        if self.n == self.capacity:
            self._resize(2 * self.capacity)  # 2x if capacity isn't enough

        self.A[self.n] = element
        self.n += 1

    def _resize(self, new_capacity):

        B = self.make_array(new_capacity)

        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_capacity

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()


if __name__ == '__main__':
    dyn_array = DynamicArray()
    dyn_array.append(1)
    print(len(dyn_array))
    dyn_array.append(2)
    print(len(dyn_array))
    print(dyn_array[0])

    dyn_array = DynamicArray()  # reassign DynamicArray
    tbl = prettytable.PrettyTable(['Length', 'Size'])

    for i in range(10):
        ln = len(dyn_array)
        ctype_sz = ctypes.sizeof(dyn_array.A)
        row = [ln, ctype_sz]
        tbl.add_row(row)
        dyn_array.append(i)

    print(tbl)