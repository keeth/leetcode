from collections import deque, defaultdict


def find_shortest_path(edges, start_room, end_room) -> list:
    if start_room == end_room:
        return [start_room]
    graph = defaultdict(list)
    for edge in edges:
        n1, n2 = edge.split("-")
        graph[n1].append(n2)
        graph[n2].append(n1)
    visited = set([start_room])
    queue = deque([start_room])
    parent = {}
    while len(queue) > 0:
        cur_room = queue.popleft()
        for adjacent_room in graph[cur_room]:
            if adjacent_room in visited:
                continue
            queue.append(adjacent_room)
            parent[adjacent_room] = cur_room
            if adjacent_room == end_room:
                path = [end_room]
                while path[-1] != start_room:
                    path.append(parent[path[-1]])
                return list(reversed(path))

        visited.add(cur_room)
    return []


def test_path1():
    assert find_shortest_path(
        ["Kitchen-LivingRoom", "BedRoom-BathRoom", "LivingRoom-BedRoom"],
        "Kitchen",
        "BathRoom",
    ) == ["Kitchen", "LivingRoom", "BedRoom", "BathRoom"]

    assert (
        find_shortest_path(
            ["Study-Library", "Kitchen-DiningRoom", "Garden-Garage"],
            "Study",
            "Garden",
        )
        == []
    )
