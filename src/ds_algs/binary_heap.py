class BinaryHeap(object):
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def insert(self, element):
        self.heap_list.append(element)
        self.current_size += 1
        self.percolate_up(self.current_size)

    def percolate_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i //= 2

    def percolate_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delete_min(self):
        min_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.percolate_down(1)
        return min_val

    def build_heap(self, from_list):
        i = len(from_list) // 2
        self.current_size = len(from_list)
        self.heap_list = [0] + from_list.copy()
        while i > 0:
            self.percolate_down(i)
            i -= 1

    def __str__(self):
        return ", ".join(map(str, self.heap_list))


if __name__ == '__main__':
    ls = [9, 6, 5, 2, 3]
    bh = BinaryHeap()
    bh.build_heap(ls)
    print(bh)
