def recursion(n):
    """Function that shows how recursion work"""
    if n == 1:
        print('The deepest state of recurse')
    else:
        print(f'Beginning of the {n} recurse')
        recursion(n - 1)
        print(f'Ending of the {n} recurse')


if __name__ == '__main__':
    recursion(5)