from typing import List
from collections import defaultdict, deque


def left(i, j, width, height) -> tuple | None:
    if i > 0:
        return (i - 1, j)
    return None


def up(i, j, width, height) -> tuple | None:
    if j > 0:
        return (i, j - 1)
    return None


def right(i, j, width, height) -> tuple | None:
    if i < width - 1:
        return (i + 1, j)
    return None


def down(i, j, width, height) -> tuple | None:
    if j < height - 1:
        return (i, j + 1)
    return None


def get_color(image: list[list[int]], coord: tuple) -> int:
    return image[coord[0]][coord[1]]


def set_color(image: list[list[int]], coord: tuple, color: int):
    image[coord[0]][coord[1]] = color


def flood_fill(
    r: int, c: int, replacement: int, image: List[List[int]]
) -> List[List[int]]:
    if not image or not image[0]:
        return []
    graph = defaultdict(list)
    h = len(image)
    w = len(image[0])
    for i in range(w):
        for j in range(h):
            neighbors = [
                up(i, j, w, h),
                down(i, j, w, h),
                left(i, j, w, h),
                right(i, j, w, h),
            ]
            graph[(i, j)] = [node for node in neighbors if node is not None]

    start = (r, c)
    target_color = get_color(image, start)
    queue = deque([start])
    visited = set([start])
    while len(queue) > 0:
        cur = queue.popleft()
        if get_color(image, cur) == target_color:
            set_color(image, cur, replacement)
            for neighbor in graph[cur]:
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)

    return image


def test_ff1():
    assert flood_fill(
        2,
        2,
        9,
        [
            [0, 1, 3, 4, 1],
            [3, 8, 8, 3, 3],
            [6, 7, 8, 8, 3],
            [12, 2, 8, 9, 1],
            [12, 3, 1, 3, 2],
        ],
    ) == [
        [0, 1, 3, 4, 1],
        [3, 9, 9, 3, 3],
        [6, 7, 9, 9, 3],
        [12, 2, 9, 9, 1],
        [12, 3, 1, 3, 2],
    ]
