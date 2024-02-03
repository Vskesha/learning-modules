from numpy import random

separator = '=' * 50

x = random.randint(100)
print(x)
print(separator)

x = random.rand()
print(x)
print(separator)

x = random.randint(100, size=5)
print(x)
print(separator)

x = random.randint(100, size=(3, 5))
print(x)
print(separator)

x = random.rand(5)
print(x)
print(separator)

x = random.rand(3, 5)
print(x)
print(separator)

x = random.choice([3, 5, 7, 9])
print(x)
print(separator)

x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)
print(separator)
