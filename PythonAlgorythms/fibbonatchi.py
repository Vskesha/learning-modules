def fib1(n):
    if n <= 1:
        return n
    return fib1(n-1) + fib1(n-2)


def fib2(n):
    fib = [0, 1] + [0] * (n-1)
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]


if __name__ == '__main__':
    print(fib1(35))
    print(fib2(35))