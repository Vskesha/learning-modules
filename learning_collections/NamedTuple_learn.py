from typing import NamedTuple


class Car(NamedTuple):
    color: str
    mileage: float
    automatic: bool


if __name__ == '__main__':
    car1 = Car('red', 3812.4, True)

    print(car1)
    print(car1.mileage)

    try:
        car1.mileage = 12
    except AttributeError as e:
        print(e.__class__.__name__, end=': ')
        print(e)
    # AttributeError: can't set attribute

    try:
        car1.windshield = 'broken'
    except AttributeError as e:
        print(e.__class__.__name__, end=': ')
        print(e)
    # AttributeError: 'Car' object has no attribute 'windshield'

    # Type annotation are not enforced without
    # a separate type checking tool like mypy:
    print(Car('red', 'NOT_A_FLOAT', 99))