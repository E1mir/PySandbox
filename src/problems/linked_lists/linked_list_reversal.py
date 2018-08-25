class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None


def reverse_linked_list(head):
    current = head
    prev_node = None

    while current:
        next_node = current.next_node

        current.next_node = prev_node

        prev_node = current
        current = next_node

    return prev_node


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next_node = b
b.next_node = c
c.next_node = d

print(a.next_node.value)
print(b.next_node.value)
print(c.next_node.value)

reverse_linked_list(a)

print(d.next_node.value)
print(c.next_node.value)
print(b.next_node.value)
