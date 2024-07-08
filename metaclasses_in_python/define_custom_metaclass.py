class Meta(type):
    def __new__(cls, name, bases, attrs):
        x = super().__new__(cls, name, bases, attrs)
        x.attr = 100
        return x


class Foo(metaclass=Meta):
    pass


print(Foo.attr)


class Bar(metaclass=Meta):
    pass


print(Bar.attr)


class Qux(metaclass=Meta):
    pass


print(Qux.attr)
