from collections import namedtuple


if __name__ == '__main__':
    Car = namedtuple('Car', 'color mileage automatic')
    car1 = Car('red', 3812.4, True)

    print(repr(car1))
    print(car1.mileage)

    try:
        car1.mileage = 12
    except AttributeError as e:
        print(type(e).__name__, end=': ')
        print(e)
    # AttributeError: can't set attribute

    try:
        car1.windshield = 'broken'
    except AttributeError as e:
        print(type(e).__name__, end=': ')
        print(e)
    # AttributeError: 'Car' object has no attribute 'windshield'
