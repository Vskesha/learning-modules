from decimal import Decimal, getcontext

def formulaFibWithDecimal(n):
    getcontext().prec = 300000

    root_5 = Decimal(5).sqrt()
    phi = ((1 + root_5) / 2)

    a = ((phi ** n) - ((-phi) ** -n)) / root_5

    return round(a)


if __name__ == '__main__':
    i = 1000000
    print(f'fib({i:0>4}) = {formulaFibWithDecimal(i)}')