def spin_words(sentence):
    return ' '.join(word[::-1] if len(word) > 4 else word for word in sentence.split())


def abc(w):
    return sorted(w)


if __name__ == '__main__':
    str1 = "Hey fellow warriors"
    str2 = "This is a test"
    str3 = "This is another test"
    for s in (str1, str2, str3):
        print(f'{s} --> {spin_words(s)}')
    print(abc('Py2thon'))