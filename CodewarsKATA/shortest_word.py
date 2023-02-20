def find_short(s):
    return min(len(word) for word in s.split(' '))


if __name__ == '__main__':
    print(find_short('The quick brown fox jumps over a lazy dog'))