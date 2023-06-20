def main():
    arr = ("one", "two", "three")
    print(arr[0])

    # Tuples have a nice repr:
    print(arr)

    # Tuples are immutable:
    try:
        arr[1] = "hello"
    except TypeError:
        print('TypeError: "tuple" object does not support item assignment')

    try:
        del arr[1]
    except TypeError:
        print("TypeError: 'tuple' object doesn't support item deletion")

    # Tuples can hold arbitrary data types:
    # (Adding elements creates a copy of the tuple)
    print(arr + (23,))


if __name__ == '__main__':
    main()
