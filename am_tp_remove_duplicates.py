def remove_duplicates(arr: list[int]) -> int:
    slow, n = 0, len(arr)
    if n == 0:
        return -1

    for fast in range(n):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]

    return slow + 1


def test_rd1():
    arr = [0, 0, 1, 1, 1, 2, 2]
    i = remove_duplicates(arr)
    assert arr[:i] == [0, 1, 2]


def test_rd2():
    arr = [0, 0, 1, 1, 1, 2]
    i = remove_duplicates(arr)
    assert arr[:i] == [0, 1, 2]


def test_rd3():
    arr = [0, 0, 1, 1, 1]
    i = remove_duplicates(arr)
    assert arr[:i] == [0, 1]


def test_rd4():
    arr = [0, 0]
    i = remove_duplicates(arr)
    assert arr[:i] == [0]


def test_rd5():
    arr = [0]
    i = remove_duplicates(arr)
    assert arr[:i] == [0]
