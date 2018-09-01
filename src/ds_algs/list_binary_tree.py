def binary_tree(r):
    """
    :param r: This is root node
    :return: returns tree
    """
    return [r, [], []]


def insert_left(root, new_branch):
    """
    :param root: current root of the tree
    :param new_branch: new branch for a tree
    :return: updated root of the tree
    """
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])

    return root


def insert_right(root, new_branch):
    """
    :param root: current root of the tree
    :param new_branch: new branch for a tree
    :return: updated root of the tree
    """
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])

    return root


def get_root_val(root):
    """
    :param root: current tree root
    :return: current tree root value
    """
    return root[0]


def set_root_val(root, new_val):
    """
    :param root: current tree root
    :param new_val: new value for root to update it
    :return: updated tree root
    """
    root[0] = new_val


def get_left_child(root):
    """
    :param root: current root
    :return: Left child of selected root
    """
    return root[1]


def get_right_child(root):
    """
    :param root: current root
    :return: Right child of selected root
    """
    return root[2]


if __name__ == '__main__':

    r = binary_tree(3)

    print(insert_left(r, 5))
    print(insert_left(r, 6))
    print(insert_right(r, 7))
    print(insert_right(r, 8))

    l = get_left_child(r)
    print(l)
    rg = get_right_child(r)
    print(rg)
