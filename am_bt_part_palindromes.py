from typing import List


def partition(s: str) -> List[List[str]]:
    def is_leaf(path):
        return "".join(path) == s

    def get_edges(path):
        prefix = "".join(path)
        suffix = s[len(prefix) :]
        edges = []
        for i in range(len(suffix)):
            edges.append(suffix[: i + 1])
        return edges

    def is_valid(edge):
        return list(edge) == list(reversed(edge))

    acc = []

    def dfs(index, path):
        if is_leaf(path):
            acc.append(path)
            return
        for edge in get_edges(path):
            if not is_valid(edge):
                continue
            dfs(index + 1, path + [edge])

    dfs(0, [])
    return acc


def test_0():
    assert sorted(partition("aab")) == [["a", "a", "b"], ["aa", "b"]]
