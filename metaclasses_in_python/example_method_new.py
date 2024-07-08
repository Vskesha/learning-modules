def new(cls):
    x = object.__new__(cls)
    x.attr = 100
    return x


class Foo:
    pass


Foo.__new__ = new

f = Foo()
print(f.attr)

g = Foo()
print(g.attr)
