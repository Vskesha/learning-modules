def gen_bin(m, prefix=''):
    if m == 0:
        print(prefix)
        return
    gen_bin(m - 1, prefix + '0')
    gen_bin(m - 1, prefix + '1')


def generate_numbers(n: int, m: int, prefix=None):
    """ prints all numbers with length m with forwarding zeroes.
        n - quantity of digits"""
    prefix = prefix or []
    if m == 0:
        print(prefix)
        return
    for digit in range(n):
        prefix.append(digit)
        generate_numbers(n, m - 1, prefix)
        prefix.pop()


if __name__ == '__main__':
    generate_numbers(2, 5)
    gen_bin(5)
