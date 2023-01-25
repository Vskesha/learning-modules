def recursive_gcd(a, b):
    return a if b == 0 else recursive_gcd(b, a%b)


if __name__ == '__main__':
    print(recursive_gcd(120, 5), recursive_gcd(24, 9), recursive_gcd(4, 5), recursive_gcd(34, 51), recursive_gcd(12, 1024))
