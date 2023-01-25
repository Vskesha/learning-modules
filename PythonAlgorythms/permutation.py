def generate_permutation(n: int, m: int = -1, prefix=None):
    """
    Generates all permutations of n numbers in m positions
    with the prefix
    """
    m = n if m == -1 else m  # N number in N positions by default
    prefix = prefix or []
    if m == 0:
        print(*prefix, sep='', end=', ')
        return
    for number in range(1, n+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutation(n, m-1, prefix)
        prefix.pop()


def find(number, lst: list):
    """
    finding number in list lst
    :return: True if number is in lst
    """
    for x in lst:
        if x == number:
            return True
    return False


if __name__ == '__main__':
    generate_permutation(5)
