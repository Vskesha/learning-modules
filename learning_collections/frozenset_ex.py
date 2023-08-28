if __name__ == '__main__':
    vowels = frozenset({'a', 'e', 'i', 'o', 'u'})

    try:
        vowels.add('p')
    except AttributeError as e:
        print(e.__class__.__name__, end=': ')
        print(e)
    # AttributeError: 'frozenset' object has no attribute 'add'

    # Frozensets are hashable and can
    # be used as dictionary keys:
    d = {frozenset({1, 2, 3}): 'hello'}
    print(d[frozenset({1, 2, 3})])
    