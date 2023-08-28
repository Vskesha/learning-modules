from types import SimpleNamespace


if __name__ == '__main__':
    car1 = SimpleNamespace(color='red', mileage=3812.4, automatic=True)

    print(car1)

    car1.mileage = 12
    car1.windshield = 'broken'
    del car1.automatic

    print(car1)
    