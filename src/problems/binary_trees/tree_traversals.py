from problems.binary_trees.tree import BinaryTree


def generate_tree():
    r = BinaryTree("Main root")
    r.insert_left(1)
    r.insert_right(2)

    # Left child of the main root
    b_1 = r.get_left_child()
    # Right child of the main root
    b_2 = r.get_right_child()

    b_1.insert_left(11)
    b_1.insert_right(12)
    b_2.insert_left(21)
    b_2.insert_right(22)

    # Left child of b_1
    b_1_1 = b_1.get_left_child()
    # Right child of b_1
    b_1_2 = b_1.get_left_child()
    # Left child of b_2
    b_2_1 = b_2.get_left_child()
    # Right child of b_2
    b_2_2 = b_2.get_right_child()

    b_1_1.insert_left(111)
    b_1_1.insert_right(112)
    b_1_2.insert_left(121)
    b_1_2.insert_right(122)
    b_2_1.insert_left(211)
    # b_2_1 has not a right child
    b_2_2.insert_left(221)
    b_2_2.insert_right(222)

    # Left child of b_1_1
    b_1_1_1 = b_1_1.get_left_child()
    # Right child of b_1_1
    b_1_1_2 = b_1_1.get_right_child()
    # Left child of b_1_2
    b_1_2_1 = b_1_2.get_left_child()
    # Right child of b_1_2
    b_1_2_2 = b_1_2.get_right_child()
    # Left child of b_2_1
    b_2_1_1 = b_2_1.get_left_child()
    # b_2_1 has not right child
    # Left child of b_2_2
    b_2_2_1 = b_2_2.get_left_child()
    # Right child of b_2_2
    b_2_2_2 = b_2_2.get_right_child()

    b_1_1_1.insert_left(1111)
    # b_1_1_1 has not right child
    b_1_1_2.insert_left(1121)
    b_1_1_2.insert_right(1122)
    # b_1_2_1 has not child
    b_1_2_2.insert_left(1221)
    b_1_2_2.insert_right(1222)
    # b_2_1_1 has not child
    b_2_2_1.insert_left(2211)
    b_2_2_1.insert_right(2212)
    # b_2_2_2 has not left child
    b_2_2_2.insert_right(2222)

    return r


def pre_order(tree):
    if tree:
        print(tree.get_root_value())
        pre_order(tree.get_left_child())
        pre_order(tree.get_right_child())


def post_order(tree):
    if tree is not None:
        post_order(tree.get_left_child())
        post_order(tree.get_right_child())
        print(tree.get_root_value())


if __name__ == '__main__':
    my_tree = generate_tree()
    pre_order(my_tree)
    print("----------------------------------")
    post_order(my_tree)
