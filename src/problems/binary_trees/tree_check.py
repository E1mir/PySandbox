class Node(object):
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


INFINITY = float('infinity')
NEG_INFINITY = float('-infinity')


def is_BST(tree, min_val=NEG_INFINITY, max_val=INFINITY):
    if tree is None:
        return True

    if not min_val <= tree.val <= max_val:
        return False

    return is_BST(tree.left, min_val, tree.val) and is_BST(tree.right, tree.val, max_val)


def is_BST_2(tree, last_node=[NEG_INFINITY]):
    if tree is None:
        return True

    if not is_BST_2(tree.left, last_node):
        return False

    if tree.val < last_node[0]:
        return False

    last_node[0] = tree.val

    return is_BST_2(tree.right, last_node)
