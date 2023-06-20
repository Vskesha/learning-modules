import collections


def main():
    d = collections.OrderedDict(one=1, two=2, three=3)
    print(d)
    d['four'] = 4
    print(d)
    print(d.keys())


if __name__ == '__main__':
    main()
