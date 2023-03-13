import re


if __name__ == '__main__':

    match = re.search(r'\d\d\D\d\d', r'Telephone 123-12-12 jkokl 64-32')
    print(match)
    print(match.start())
    print(match.end())
    print(match.span())
    print(match.re)
    print(match.groups())
    print(match[0])
    print()

    match = re.search(r'\d\d\D\d\d', r'Telephone 1231212 jkokl 6432')
    print(match, '\n')

    match = re.fullmatch(r'\d\d\D\d\d', r'12-12')
    print(match, '\n')

    match = re.fullmatch(r'\d\d\D\d\d', r'T. 12-12')
    print(match, '\n')

    print(re.split(r'\W+', 'Где, скажите мне, мои очки??!'), '\n')

    print(re.findall(r'\d\d\.\d\d\.\d{4}', 'Эта строка написана 19.01.2018, а могла бы и 01.09.2017'))
    print()

    for m in re.finditer(r'\d\d\.\d\d\.\d{4}', 'Эта строка написана 19.01.2018, а могла бы и 01.09.2017'):
        print('Date', m[0], 'starts from position', m.start())
    print()

    print(re.sub(r'\d\d\.\d\d\.\d{4}', r'DD.MM.YYYY', 'Эта строка написана 19.01.2018, а могла бы и 01.09.2017'), '\n')

    print(re.findall(r'\d+', '12 + ٦٧'), '\n')

    print(re.findall(r'\w+', 'Hello, мир!'), '\n')

    print(re.findall(r'\d+', '12 + ٦٧', flags=re.ASCII), '\n')

    print(re.findall(r'\w+', 'Hello, мир!', flags=re.ASCII), '\n')

    print(re.findall(r'[уеыаоэяию]+', 'ОООО ааааа ррррр ЫЫЫЫ яяяя'), '\n')

    print(re.findall(r'[уеыаоэяию]+', 'ОООО ааааа ррррр ЫЫЫЫ яяяя', flags=re.I), '\n')

    text = 'Торт\nс вишней1\nвишней2'
    print(re.findall(r'Торт.с', text))
    print(re.findall(r'Торт.с', text, flags=re.DOTALL), '\n')

    print(re.findall(r'виш\w+', text, flags=re.MULTILINE))
    print(re.findall(r'^виш\w+', text, flags=re.MULTILINE), '\n')
