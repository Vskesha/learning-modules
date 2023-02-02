def binary_search(a: list, key: int):
    """
    Binary search in sorted list
    :param key: number that we find
    :param a: sorted list
    :return: tuple of (first index of key(-1 if not found), amount of elements equal key)
    """
    left = left_bound(a, key)
    right = right_bound(a, key)
    amount = right - left - 1
    index = left + 1 if amount else -1
    return index, amount


def left_bound(a: list, key: int):
    left = -1
    right = len(a)
    while right - left > 1:
        middle = (left + right) // 2
        if a[middle] < key:
            left = middle
        else:
            right = middle
    return left


def right_bound(a: list, key: int):
    left = -1
    right = len(a)
    while right - left > 1:
        middle = (left + right) // 2
        if a[middle] <= key:
            left = middle
        else:
            right = middle
    return right


if __name__ == '__main__':
    seq = [1, 3, 3, 3, 5, 5, 6, 7, 7, 9]
    print(seq)
    for i in range(11):
        print(f'For {i} boundaries are {binary_search(seq, i)}')
