from heapq import heappush, heappop

if __name__ == '__main__':
    q = []

    heappush(q, (2, 'code'))
    heappush(q, (1, 'eat'))
    heappush(q, (3, 'sleep'))

    while q:
        print(heappop(q))
    