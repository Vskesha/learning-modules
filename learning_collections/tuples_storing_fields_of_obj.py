def main():
    # Fields: color, mileage, automatic
    car1 = ('red', 3812.4, True)
    car2 = ('blue', 40231, False)

    # Tuple instances have a nice repr:
    print(car1)
    print(car2)

    # Get mileage:
    print(car2[1])

    # Tuples are immutable:
    try:
        car2[1] = 12
    except TypeError:
        print("TypeError: 'tuple' object does not support item assignment")

    # No protection against missing or extra fields
    # or a wrong order:
    car3 = (3431.5, 'green', True, 'silver')


if __name__ == '__main__':
    main()
