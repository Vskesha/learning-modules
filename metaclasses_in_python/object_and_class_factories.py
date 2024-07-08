class Foo:
    def __init__(self):
        self.attr = 100


x = Foo()
print(x.attr)
y = Foo()
print(y.attr)
z = Foo()
print(z.attr)


# class Meta(type):
#     def __new__(cls, name, bases, attrs):
#         x = super().__new__(cls, name, bases, attrs)
#         x.attr = 100
#         return x


class Meta(type):
    def __init__(cls, name, bases, attrs):
        cls.attr = 100


class X(metaclass=Meta):
    pass


print(X.attr)


class Y(metaclass=Meta):
    pass


print(Y.attr)


class Z(metaclass=Meta):
    pass


print(Z.attr)
