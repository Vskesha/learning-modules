from collections import deque


if __name__ == '__main__':
    q = deque()

    q.append('eat')
    q.append('sleep')
    q.append('code')

    print(q)

    print(q.popleft())
    print(q.popleft())
    print(q.popleft())
    print(q.popleft())
