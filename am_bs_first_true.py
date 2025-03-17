def find_boundary(arr: list[bool]) -> int:
    if not arr:
        return -1
    if not arr[-1]:
        return -1
    left, right = 0, len(arr)
    while True:
        mid = (right - left) // 2
        if mid == 0:
            return 0
        if arr[mid] and not arr[mid - 1]:
            return mid
        elif arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return 0


def test_find_boundary():
    assert find_boundary([False, False, True, True, True]) == 2
