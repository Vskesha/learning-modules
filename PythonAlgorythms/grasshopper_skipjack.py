from random import randint


def all_combinations(n, price, comb=None):
    if n > len(price) - 1:
        print('Price list is short')
        return
    if comb is None:
        comb = [1]
    if comb[-1] == n - 1:
        comb = comb + [n]
        # comb.append(n) DON'T WORK BECAUSE WE NEED TO CREATE NEW LIST
    if comb[-1] > n - 1:
        print(comb, end='-->', sep='')
        summ = 0
        for pos in comb:
            summ += price[pos]
        print(summ)
        return
    for var in range(1,3):
        comb.append(comb[-1] + var)
        all_combinations(n, price, comb)
        comb.pop()



def traj_number(n):
    k = [0, 1] + [0] * n
    for i in range(2, n+1):
        k[i] = k[i-2] + k[i-1]
    return k[n]


def count_trajectories(n, allowed: list):
    k = [0, 1, int(allowed[2])] + [0] * (n-2)
    for i in range(3, n+1):
        if allowed[i]:
            k[i] = k[i-1] + k[i-2] + k[i-3]
    return k[n]


def count_min_cost(n, price:list):
    c = [float('-inf'), price[1], price[1] + price[2]] + [0] * (n-2)
    for i in range(3, n+1):
        c[i] = price[i] + min(c[i-1], c[i-2])
    return c[n]


if __name__ == '__main__':
    print(count_trajectories(10, [True, True, True, False, True, False, True, True, True, True, True]))
    price = [0] + [randint(1, 10) for x in range(10)]
    print(price)
    print(traj_number(9))
    print(count_min_cost(10, price))
    all_combinations(10, price)