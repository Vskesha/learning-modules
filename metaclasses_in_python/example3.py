Foo = type(
    "Foo",
    (),
    {
        "attr": 100,
        "attr_val": lambda x_: x_.attr
    }
)

x = Foo()
print(x.attr)
print(x.attr_val())


class Foo:
    attr = 100

    def attr_val(self):
        return self.attr


x = Foo()
print(x.attr)
print(x.attr_val())
