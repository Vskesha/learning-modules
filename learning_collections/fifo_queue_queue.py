from queue import Queue


if __name__ == '__main__':
    q = Queue()

    q.put('eat')
    q.put('sleep')
    q.put('code')

    print(q)

    print(q.get())
    print(q.get())
    print(q.get())

    print(q.get_nowait())

    print(q.get())
