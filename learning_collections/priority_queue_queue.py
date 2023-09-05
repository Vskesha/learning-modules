from queue import PriorityQueue


if __name__ == '__main__':
    q = PriorityQueue()

    q.put((2, 'code'))
    q.put((1, 'eat'))
    q.put((3, 'sleep'))

    while q:
        print(q.get())
