def f(obj):
    print("attr =", obj.attr)


Foo = type("Foo", (), {"attr": 100, "attr_val": f})
x = Foo()
print(x.attr)
x.attr_val()


class Foo:
    attr = 100
    attr_val = f


x = Foo()
print(x.attr)
x.attr_val()  # noqa
