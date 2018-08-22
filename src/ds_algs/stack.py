class Stack(object):
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) - 1]

    def is_empty(self):
        return self._items == []

    def size(self):
        return len(self._items)

    def __str__(self):
        return ", ".join(map(str, self._items))


if __name__ == '__main__':
    s = Stack()

    print(s.is_empty())

    s.push('hello')
    s.push(2)

    print(s.peek())

    s.push(True)

    print(s.size())
    print(s.is_empty())
    print(s.pop())
    print(s)
