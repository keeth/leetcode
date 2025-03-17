def binary_search(arr: list[int], target: int) -> int:
    if not arr:
        return -1
    i = len(arr) // 2
    while True:
        val = arr[i]
        if val == target:
            return i
        elif val > target:
            i = i - i // 2
        else:
            i = i + i // 2
    return 0


def test_bs1():
    assert binary_search([1, 2, 3, 4, 5, 6], 5) == 4


def test_bs2():
    assert binary_search([1, 2, 3, 4, 4, 4, 5, 6, 10, 50], 2) == 1
