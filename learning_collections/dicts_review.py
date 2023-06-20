def main():
    car1 = {
        'color': 'red',
        'mileage': 3812.4,
        'automatic': True
    }
    car2 = {
        'color': 'blue',
        'mileage': 40231,
        'automatic': False
    }

    # Dicts have a nice repr:
    print(car2)

    # Get mileage:
    print(car2['mileage'])

    # Dicts are mutable:
    car2['mileage'] = 12
    car2['windshield'] = 'broken'
    print(car2)

    # No protection against wrong field names,
    # or missing/extra fields
    car3 = {
        'colr': 'green',
        'automatic': False,
        'windshield': 'broken'
    }


if __name__ == '__main__':
    main()
