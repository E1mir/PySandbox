class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self):
        return ", ".join(map(str, self.items))


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
