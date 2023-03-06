import re


def solve_runes(runes):
    can_be_zero = all(len(n) == 1 or n[0] != '?' for n in re.split(r'[-+*=]+', runes.strip('-')))
    for d in '0123456789':
        if d in runes or d == '0' and not can_be_zero:
            continue
        if eval(runes.replace('=', '==').replace('?', d)):
            return int(d)
    return -1


def solve_runes2(runes):
    start = int(bool(re.search(r'\b0\d+', runes.replace('?', '0'))))
    for d in sorted(set(map(str, range(start, 10))) - set(runes)):
        if eval(runes.replace('=', '==').replace('?', d)):
            return int(d)
    return -1


if __name__ == '__main__':
    print(solve_runes("1+1=?"), 2, "Answer for expression '1+1=?' ")
    print(solve_runes("123*45?=5?088"), 6, "Answer for expression '123*45?=5?088' ")
    print(solve_runes("-5?*-1=5?"), 0, "Answer for expression '-5?*-1=5?' ")
    print(solve_runes("19--45=5?"), -1, "Answer for expression '19--45=5?' ")
    print(solve_runes("??*??=302?"), 5, "Answer for expression '??*??=302?' ")
    print(solve_runes("?*11=??"), 2, "Answer for expression '?*11=??' ")
    print(solve_runes("??*1=??"), 2, "Answer for expression '??*1=??' ")
