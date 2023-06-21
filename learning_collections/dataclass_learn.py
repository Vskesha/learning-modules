from dataclasses import dataclass


@dataclass
class Car:
    color: str
    mileage: float
    automatic: bool


def main():
    car1 = Car('red', 3812.4, True)

    # Instances have a nice repr:
    print(car1)

    # Accessing fields:
    print(car1.mileage)

    # Fields are mutable:
    car1.mileage = 12
    car1.windshield = 'broken'

    # Type annotations are not enforced without
    # a separate type checking tool like mypy:
    car2 = Car('red', 'NOT_A_FLOAT', 99)
    print(car2)


if __name__ == '__main__':
    main()
