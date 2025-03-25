from typing import List
from collections import deque


def count_up_edges(graph):
    up_edges = {node: 0 for node in graph}
    for node in graph:
        for downstream_node in graph[node]:
            up_edges[downstream_node] += 1
    return up_edges


def task_scheduling(
    tasks: List[str], requirements: List[List[str]]
) -> List[str] | None:
    q = deque()
    graph = {task: [] for task in tasks}
    for a, b in requirements:
        graph[a].append(b)
    up_edge_counts = count_up_edges(graph)
    for node, count in up_edge_counts.items():
        if count == 0:
            q.append(node)
    output = []
    while len(q) > 0:
        node = q.popleft()
        output.append(node)
        for downstream_node in graph[node]:
            up_edge_counts[downstream_node] -= 1
            if up_edge_counts[downstream_node] == 0:
                q.append(downstream_node)
    if len(output) != len(tasks):
        return None
    return output


def test_task_scheduling():
    tasks = ["a", "b", "c", "d"]
    requirements = [["a", "b"], ["a", "c"], ["b", "d"], ["c", "d"]]
    order = task_scheduling(tasks, requirements)
    assert order == ["a", "c", "b", "d"] or order == ["a", "b", "c", "d"]
