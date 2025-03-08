from typing import List
from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order_traversal(root: Node) -> List[List[int]]:
    if not root:
        return []
    output = []
    queue = deque([root])
    while len(queue) > 0:
        n = len(queue)
        new_level = []
        for _ in range(n):
            node = queue.popleft()
            new_level.append(node.val)
            for child in [node.left, node.right]:
                if child is None:
                    continue
                queue.append(child)
        output.append(new_level)
    return output


def build_tree(nodes: deque, f):
    val = nodes.popleft()
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


def test_tree1():
    root = build_tree(
        deque(
            ["1", "2", "4", "x", "7", "x", "x", "5", "x", "x", "3", "x", "6", "x", "x"]
        ),
        int,
    )
    assert level_order_traversal(root) == [
        [1],
        [2, 3],
        [4, 5, 6],
        [7],
    ]
