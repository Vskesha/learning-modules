def parse_int(string):
    table = {'zer': 0,  'one': 1, 'two': 2, 'thr': 3, 'fou': 4, 'fiv': 5,
            'six': 6, 'sev': 7, 'eig': 8, 'nin': 9, 'ten': 10, 'ele': 11,
            'thi': 3, 'teen': 10, 'for': 4, 'fif': 5, 'twe': 2, 'ty': 10}
    string = string.replace(' and', ' ').replace('-', ' ').lower()
    num = 0
    for word in string.split():
        if word == 'million':
            num *= 1000000
        elif word == 'thousand':
            num += (num % 1000) * 999
        elif word == 'hundred':
            num += 99 * (num % 10)
        elif word[-2:] == 'ty':
            num += table[word[:3]] * 10
        elif word[-3:] == 'een' or word[-3:] == 'lve':
            num += table[word[:3]] + 10
        else:
            num += table[word[:3]]
    return num

if __name__ == '__main__':
    print(parse_int('one'), 1)
    print(parse_int('twenty'), 20)
    print(parse_int('two hundred forty-six'), 246)
    print(parse_int('ten million two hundred twenty-four thousand five hundred and forty-two'), 10224542)
