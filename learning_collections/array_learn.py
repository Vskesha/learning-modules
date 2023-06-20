import array


def main():
    arr = array.array('f', (1.0, 1.5, 2.0, 2.5))
    print(arr[1])

    # Arrays have a nice repr:
    print(arr)

    # Arrays are mutable:
    arr[1] = 23.0
    print(arr)

    del arr[1]
    print(arr)

    arr.append(42.0)
    print(arr)

    # Arrays are "typed":
    try:
        arr[1] = 'hello'
    except TypeError:
        print('TypeError: must be real number, not str')


if __name__ == '__main__':
    main()
