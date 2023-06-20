import dis


def main():
    dis.dis(compile("(23, 'a', 'b', 'c')", "", "eval"))
    dis.dis(compile("[23, 'a', 'b', 'c']", "", "eval"))


if __name__ == '__main__':
    main()
