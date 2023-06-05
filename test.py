def describe(s: str):
    print(s)


def assert_equals(a, b, c=None):
    if c and a != b:
        print(c, end=' :')
    if a == b:
        print('Test passed')
    else:
        print(f'{a} should equal {b}')


def testtime():
    pass


if __name__ == '__main__':
    out = iter('vskesha')
    print(','.join([next(out) for _ in range(7)]))
    x = 1
    for _ in range(10):
        x ^= 1
        # x = (x + 1) % 2
        print(x)
