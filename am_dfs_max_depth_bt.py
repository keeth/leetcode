class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_tree_depth(root: Node):
    def depth_of_subtree(node: Node) -> int:
        if not node:
            return 0
        left = depth_of_subtree(node.left)
        right = depth_of_subtree(node.right)
        return max(left, right) + 1

    return depth_of_subtree(root) - 1


# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


def test_0():
    tree = build_tree(iter([5, 4, 3, "x", "x", 8, "x", "x", 6, "x", "x"]), int)
    assert max_tree_depth(tree) == 2
