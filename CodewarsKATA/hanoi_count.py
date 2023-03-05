def hanoi(disks):
    k = 0
    if disks == 1:
        return 1
    k += hanoi(disks-1)
    k += 1
    k += hanoi(disks-1)
    return k


def hanoi2(disks):
    b = 0
    for _ in range(disks):
        b = b * 2 + 1
    return b


if __name__ == '__main__':
    for i in range(1, 10):
        print(hanoi(i), end=' ')
    print()
    for i in range(1, 10):
        print(hanoi2(i), end=' ')
