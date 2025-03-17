def letter_combinations(n: int) -> list[str]:
    def is_leaf(index):
        return index == n

    def get_edges(index):
        return ["a", "b"]

    acc = []

    def dfs(index, path):
        if is_leaf(index):
            acc.append("".join(path))
            return
        for edge in get_edges(index):
            path.append(edge)
            dfs(index + 1, path)
            path.pop()

    dfs(0, [])

    return acc


def test_0():
    assert sorted(letter_combinations(2)) == ["aa", "ab", "ba", "bb"]


def test_1():
    assert sorted(letter_combinations(4)) == [
        "aaaa",
        "aaab",
        "aaba",
        "aabb",
        "abaa",
        "abab",
        "abba",
        "abbb",
        "baaa",
        "baab",
        "baba",
        "babb",
        "bbaa",
        "bbab",
        "bbba",
        "bbbb",
    ]
