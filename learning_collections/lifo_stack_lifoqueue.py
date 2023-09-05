from queue import LifoQueue


if __name__ == '__main__':
    s = LifoQueue()
    s.put('eat')
    s.put('sleep')
    s.put('code')

    print(s.get())
    print(s.get())
    print(s.get())
    print(s.get_nowait())
    print(s.get())
    