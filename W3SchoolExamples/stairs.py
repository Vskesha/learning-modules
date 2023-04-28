from timeit import repeat
from functools import lru_cache


@lru_cache(maxsize=16)
def steps_to(st):
    if st < 1:
        return 0
    if st < 3:
        return st
    if st == 3:
        return 4
    return steps_to(st-1) + steps_to(st-2) + steps_to(st-3)


if __name__ == '__main__':
    # setup_code = 'from __main__ import steps_to'
    # stmt = 'steps_to(30)'
    # times = repeat(stmt=stmt, setup=setup_code, repeat=3, number=10)
    # print(times)
    # print('Minimum execution time is: ', min(times))

    print(steps_to(30))
    print(steps_to.cache_info())
