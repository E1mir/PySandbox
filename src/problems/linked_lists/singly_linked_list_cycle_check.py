"""
Problem
Given a singly linked list, write a function which takes in the first node in a singly linked list
and returns a boolean indicating if the linked list contains a "cycle".

A cycle is when a node's next point actually points back to a previous node in the list.
This is also sometimes known as a circularly linked list.
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None


def check_cycle(node):
    marker1 = node
    marker2 = node

    while marker2 is not None and marker2.next_node is not None:

        marker1 = marker1.next_node
        marker2 = marker2.next_node.next_node

        if marker2 == marker1:
            return True

    return False


a = Node(1)
b = Node(2)
c = Node(3)

a.next_node = b
b.next_node = c


print(check_cycle(a))
