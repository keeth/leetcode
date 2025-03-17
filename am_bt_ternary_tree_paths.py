from typing import List


class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children


def ternary_tree_paths(root: Node) -> List[str]:
    def dfs(node, ancestors, acc):
        if not node.children:
            acc.append(ancestors)
        for child in node.children:
            new_path = ancestors + [child.val]
            dfs(child, new_path, acc)

    root_acc = []
    dfs(root, [root.val], root_acc)

    return root_acc


# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    num = int(next(nodes))
    children = [build_tree(nodes, f) for _ in range(num)]
    return Node(f(val), children)


def test_0():
    tree = build_tree(iter([1, 3, 2, 1, 3, 0, 4, 0, 6, 0]), int)
    assert ternary_tree_paths(tree) == [[1, 2, 3], [1, 4], [1, 6]]
