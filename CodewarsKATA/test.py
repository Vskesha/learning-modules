def assert_equals(a, b):
    print(a == b)


if __name__ == '__main__':
    out = iter('vskesha')
    print(','.join([next(out) for _ in range(7)]))
