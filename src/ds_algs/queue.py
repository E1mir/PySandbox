class Queue(object):
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def is_empty(self):
        return self._items == []

    def size(self):
        return len(self._items)

    def __str__(self):
        return ", ".join(map(str, self._items))


if __name__ == '__main__':
    q = Queue()
    print(q.size())
    print(q.is_empty())

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue('Three')
    print(q)
    print(q.dequeue())
    print(q)
    q.enqueue('Four')
    print(q)
    q.dequeue()
    q.dequeue()
    print(q)