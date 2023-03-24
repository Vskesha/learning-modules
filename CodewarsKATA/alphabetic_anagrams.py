import test
from collections import Counter
from math import factorial, prod


def listPosition(word):
    """Return the anagram list position of the word"""
    if len(word) < 2:
        return 1
    chars = Counter(sorted(word))
    position = 0
    for char in chars:
        if char == word[0]:
            break
        chars[char] -= 1
        perm = prod([factorial(v) for v in chars.values() if v > 1])
        comb = factorial(len(word) - 1) // perm
        position += comb
        chars[char] += 1
    position += listPosition(word[1:])
    return position


if __name__ == '__main__':
    testValues = {'A': 1, 'ABAB': 2, 'AAAB': 1, 'BAAA': 4, 'QUESTION': 24572, 'BOOKKEEPER': 10743}
    for word in testValues:
        test.assert_equals(listPosition(word), testValues[word], 'Incorrect list position for: ' + word)
