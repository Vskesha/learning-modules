def main():
    arr = bytes((0, 1, 2, 3))
    print(arr[1])

    # Bytes literals have their own syntax:
    print(arr)
    arr = b"\x00\x01\x02\x03"

    # Only valis 'bytes' are allowed:
    try:
        bytes((0, 300))
    except ValueError:
        print('ValueError: bytes must be in range(0, 256)')

    # Bytes are immutable:
    try:
        arr[1] = 23
    except TypeError:
        print("TypeError: 'bytes' object does not support item assignment")

    try:
        del arr[1]
    except TypeError:
        print("TypeError: 'bytes' object doesn't support item deletion")


if __name__ == '__main__':
    main()
