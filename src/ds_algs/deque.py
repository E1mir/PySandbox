class Deque(object):
    def __init__(self):
        self._items = []

    def add_front(self, item):
        self._items.append(item)

    def add_rear(self, item):
        self._items.insert(0, item)

    def remove_front(self):
        return self._items.pop()

    def remove_rear(self):
        return self._items.pop(0)

    def is_empty(self):
        return self._items == []

    def size(self):
        return len(self._items)

    def __str__(self):
        return ", ".join(map(str, self._items))


if __name__ == '__main__':
    d = Deque()
    d.add_front('Hello')
    d.add_rear('World')
    print(d)
    print(d.size())
    print("{} {}".format(d.remove_front(), d.remove_rear()))
    print(d.size())
