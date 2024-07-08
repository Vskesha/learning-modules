from metaclasses_in_python.example1 import Foo

Bar = type("Bar", (Foo,), dict(attr=100))
x = Bar()
print(x.attr)
print(x.__class__)
print(x.__class__.__bases__)


class Bar(Foo):
    attr = 100


x = Bar()
print(x.attr)
print(x.__class__)
print(x.__class__.__bases__)
