from collections import defaultdict


def main():
    from collections import defaultdict
    dd = defaultdict(list)

    # Accessing a missing key creates it and
    # initializes it using the default factory,
    # i.e. list() in this example:
    dd["dogs"].append("Rufus")
    dd["dogs"].append("Kathrin")
    dd["dogs"].append("Mr Sniffles")

    print(dd["dogs"])


if __name__ == '__main__':
    main()
