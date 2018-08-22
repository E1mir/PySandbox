"""
Implement a stack using 2 stacks
"""
from nose.tools import assert_equal


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


class Queue2Stacks(object):
    def __init__(self):
        self.instack = Stack()
        self.outstack = Stack()

    def enqueue(self, item):
        self.instack.push(item)

    def dequeue(self):
        if self.outstack.is_empty():
            while not self.instack.is_empty():
                self.outstack.push(self.instack.pop())

        return self.outstack.pop()


if __name__ == '__main__':
    q = Queue2Stacks()

    for i in range(5):
        q.enqueue(i)

    for i in range(5):
        print(q.dequeue())
