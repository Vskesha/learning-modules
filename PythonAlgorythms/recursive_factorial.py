def recursive_factorial(n):
    return 1 if n == 0 else recursive_factorial(n-1) * n

if __name__ == '__main__':
    print(recursive_factorial(0), recursive_factorial(3), recursive_factorial(5), recursive_factorial(10))
