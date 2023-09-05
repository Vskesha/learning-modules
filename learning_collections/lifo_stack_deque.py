from collections import deque


if __name__ == '__main__':
    s = deque()
    s.append('eat')
    s.append('sleep')
    s.append('code')

    print(s)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    