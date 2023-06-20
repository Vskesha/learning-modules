from collections import ChainMap


def main():
    dict1 = {'one': 1, 'two': 2}
    dict2 = {'three': 3, 'four': 4}
    chain = ChainMap(dict1, dict2)
    print(chain)

    # ChainMap searches each collection in the chain
    # from left to right until it finds the key (or fails):
    print(chain["three"])

    print(chain["one"])

    print(chain["missing"])


if __name__ == '__main__':
    main()
