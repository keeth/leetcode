from typing import List
from collections import deque


def shortest_path(graph: List[List[int]], a: int, b: int) -> int:
    queue = deque([a])
    visited = set([a])
    level = 0
    while len(queue) > 0:
        n = len(queue)
        for _ in range(n):
            cur_node = queue.popleft()
            if cur_node == b:
                return level
            for adj_node in graph[cur_node]:
                if adj_node in visited:
                    continue
                queue.append(adj_node)
                visited.add(adj_node)
        level += 1
    return level


def test_graph1():
    assert shortest_path([[1, 2], [0, 2, 3], [0, 1], [1]], 0, 3) == 2


def test_graph2():
    assert (
        shortest_path(
            [
                [1, 4],
                [0, 2],
                [1, 3],
                [2, 4, 5],
                [0, 3],
                [3, 6, 9],
                [5, 8],
                [8, 9],
                [6, 7],
                [5, 7],
            ],
            0,
            7,
        )
        == 5
    )
