class Car:

    def __init__(self, color, mileage, automatic):
        self.color = color
        self.mileage = mileage
        self.automatic = automatic

    def __repr__(self):
        return f"Car(color: '{self.color}', \n\tmileage: {self.mileage}, \n\tautomatic: {self.automatic})"


def main():
    car1 = Car('red', 3812.4, True)
    car2 = Car('blue', 40231.0, False)

    # Get the mileage:
    print(car2.mileage)

    # Classes are mutable:
    car2.mileage = 12
    car2.windshield = 'broken'

    # String representation is not very useful
    # (must add a manually written __repr__ method):
    print(car1)


if __name__ == '__main__':
    main()
