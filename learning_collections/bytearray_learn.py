def main():
    arr = bytearray((0, 1, 2, 3))
    print(arr[1])

    # The bytearray repr:
    print(arr)

    # Bytearrays are mutable:
    arr[1] = 23
    print(arr)
    print(arr[1])

    # Bytearrays can grow and shrink in size:
    del arr[1]
    print(arr)
    arr.append(42)
    print(arr)

    # Bytearrays can only hold 'bytes'
    # (integers in the range 0 <= x <= 255)
    try:
        arr[1] = 'hello'
    except TypeError:
        print("TypeError: 'str' object cannot be interpreted as an integer")

    try:
        arr[1] = 300
    except ValueError:
        print("ValueError: byte must be in range(0, 256)")

    # Bytearrays can be converted back into bytes objects:
    # (This will copy the data)
    print(bytes(arr))


if __name__ == '__main__':
    main()
