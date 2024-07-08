Foo = type("Foo", (), {})
x = Foo()
print(type(x))


class Foo:
    pass


x = Foo()
print(type(x))
