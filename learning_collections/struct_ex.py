from struct import Struct


if __name__ == '__main__':
    MyStruct = Struct('i?f')
    data = MyStruct.pack(23, False, 42.0)

    print(data)

    print(MyStruct.unpack(data))
    