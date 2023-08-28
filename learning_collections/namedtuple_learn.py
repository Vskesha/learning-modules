from collections import namedtuple
from sys import getsizeof


if __name__ == '__main__':
    p = namedtuple('Point', ['x', 'y', 'z'])
    p1 = p(1, 2, 3)
    p2 = 1, 2, 3

    print(getsizeof(p1))
    print(getsizeof(p2))

    print(p1)
    print(p2)

    print(p)
    print(dir(p))