def main():
    arr = 'abcd'
    print(arr[1])

    print(arr)

    # Strings are immutable:
    try:
        arr[1] = 'e'
    except TypeError:
        print('TypeError: "str" object does not support item issignment')

    try:
        del arr[1]
    except TypeError:
        print("TypeError: 'str' object doesn't support item deletion")

    # Strings can be unpacked into a list to
    # get a mutable representation:
    print(list(arr))
    print(''.join(list(arr)))

    # Strings are recursive data structures:
    print(type('abc'))
    print(type('abc'[0]))


if __name__ == '__main__':
    main()
