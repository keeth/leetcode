from typing import List

lookup = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


def letter_combinations_of_phone_number(digits: str) -> List[str]:
    acc = []

    def get_edges(index):
        digit = digits[index]
        return list(lookup[digit])

    def is_leaf(index):
        return index == len(digits)

    def dfs(index, path):
        if is_leaf(index):
            acc.append("".join(path))
            return
        for edge in get_edges(index):
            dfs(index + 1, path + [edge])

    dfs(0, [])
    return acc


def test_0():
    assert letter_combinations_of_phone_number("23") == [
        "ad",
        "ae",
        "af",
        "bd",
        "be",
        "bf",
        "cd",
        "ce",
        "cf",
    ]


def test_1():
    assert letter_combinations_of_phone_number("2") == ["a", "b", "c"]


def test_2():
    assert letter_combinations_of_phone_number("56") == [
        "jm",
        "jn",
        "jo",
        "km",
        "kn",
        "ko",
        "lm",
        "ln",
        "lo",
    ]
