import test
import re


def car_numbers(s: str) -> str:
    if re.fullmatch(r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', s):
        return 'Private'
    if re.fullmatch(r'[АВЕКМНОРСТУХ]{2}\d{5,6}', s):
        return 'Taxi'
    return 'Fail'


def words_count(s: str) -> int:
    return len(re.findall(r'[a-zа-яё0-9]+[a-zа-яё0-9-]*', s, flags=re.IGNORECASE))


def find_email(s: str) -> list:
    return re.findall(r"(?:[a-z0-9_']|[a-z0-9_'][a-z0-9_'.+-]{0,62}[a-z0-9_'])@(?:[a-z0-9][a-z0-9.-]{0,253}[a-z0-9]|[a-z0-9])", s)


def replace_time(s: str) -> str:
    return re.sub(r'(?:[01][0-9]|2[0-3])(?::[0-5][0-9]){1,2}', '(TBD)', s)


def test_pascal_reals(s: str) -> None:
    numbers = [line.strip() for line in s.splitlines()]
    for number in numbers:
        real = re.fullmatch(r'[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-][0-9]+)?', number)
        print(number, ' is ', '' if real and ('.' in number or 'e' in number.lower()) else 'ill', 'legal.', sep='')


def find_abbreviations(s: str) -> list[str]:
    return re.findall(r'[A-ZА-ЯЁ]{2,}(?: +[A-ZА-ЯЁ]{2,})*', s)


def repl_fun(match_obj):
    return f'>Censored({len(match_obj[0])})<'


def to_cube(match_obj):
    return str(int(match_obj[0]) ** 3)


def make_abbreviation(text: str) -> str:
    return ''.join(c.upper() for c in re.findall(r'\b\w', text))


def is_haiku(haiku: str) -> str:
    hai = haiku.split('/')
    if len(hai) != 3:
        return 'Не хайку. Должно быть 3 строки.'
    hai_len = [len(re.findall(r'[ёуеыаоэяию]', line.lower())) for line in hai]
    a = b = c = 0
    if hai_len[0] != 5:
        a, b, c = 1, 5, hai_len[0]
    elif hai_len[1] != 7:
        a, b, c = 2, 7, hai_len[1]
    elif hai_len[2] != 5:
        a, b, c = 3, 5, hai_len[2]
    return f'Не хайку. В {a} строке слогов не {b}, а {c}.' if a else 'Хайку!'


def to_under_from_camel(code: str) -> str:
    return re.sub(r'(?<=[a-z0-9])([A-Z])', r'_\1', code).lower()


def delete_repeted_words(text: str) -> str:
    return re.sub(r'(\b\w+\b)( +\b\1\b)+', r'\1', text)


def deer_to_hare(text: str) -> str:
    return re.search(r'олень,( +\w+){,5} +заяц', text)[0]


def format_big_numbers(text: str) -> str:
    return re.sub(r'\b\d+\b', lambda x: f'{int(x[0]):,d}', text)


if __name__ == '__main__':
    test.assert_equals(car_numbers('С227НА777'), 'Private')
    test.assert_equals(car_numbers('КУ22777'), 'Taxi')
    test.assert_equals(car_numbers('Т22В7477'), 'Fail')
    test.assert_equals(car_numbers('М227К19У9'), 'Fail')
    test.assert_equals(car_numbers(' С227НА777'), 'Fail')
    print()
    test.assert_equals(words_count('Он --- серо-буро-малиновая редиска!!\n>>>:->\nА не кот.\nwww.kot.ru'), 9)
    print()
    print(find_email('Иван Иванович!\nНужен ответ на письмо от ivanoff@ivan-chai.ru.\n'
                     'Не забудьте поставить в копию\nserge\'o-lupin@mail.ru- это важно.'))
    print(find_email('NO: foo.@ya.ru, foo@.ya.ru\nPARTLY: boo@ya_ru, -boo@ya.ru-, foo№boo@ya.ru'))
    text = 'Уважаемые! Если вы к 09:00 не вернёте\nчемодан, то уже в 09:00:01 я за себя не отвечаю.\nPS. С отношением 25:50 всё нормально!'
    print()

    print(replace_time(text))
    print()

    numbers = '''1.2 \n  1. \n    1.0e-55  \n      e-12   \n  6.5E \n        1e-12  \n  +4.1234567890E-99999           \n  7.6e+12.5 \n   99 '''
    test_pascal_reals(numbers)
    print()

    text = 'Это курс информатики соответствует ФГОС и ПООП, \nэто подтверждено ФГУ ФНЦ НИИСИ РАН'
    print(find_abbreviations(text), '\n')

    match = re.search(r'\w+', r'$$ What??')
    print(match)
    print(match.group())
    print(match[0])
    print(match.start(), match.end())
    print()

    pattern = r'\s*([ЁёА-Яа-я]+)(\d+)\s*'
    string = r'---   Опять45   ---'
    match = re.search(pattern, string)
    print(f'Found substring >{match[0]}< from the position {match.start(0)} to {match.end(0)}')
    print(f'The group of characters >{match[1]}< from the position {match.start(1)} to {match.end(1)}')
    print(f'The group of digits >{match[2]}< from the position {match.start(2)} to {match.end(2)}')
    print()

    pattern = r'\s*([ЁёА-Яа-я])+(\d)+\s*'
    string = r'---   Опять45   ---'
    match = re.search(pattern, string)
    print(f'Found substring >{match[0]}< from the position {match.start(0)} to {match.end(0)}')
    print(f'The group of characters >{match[1]}< from the position {match.start(1)} to {match.end(1)}')
    print(f'The group of digits >{match[2]}< from the position {match.start(2)} to {match.end(2)}')
    print()

    pattern = r'((\d)(\d))((\d)(\d))'
    string = r'123456789'
    match = re.search(pattern, string)
    print(string)
    print(f'Found substring >{match[0]}< from the position {match.start(0)} to {match.end(0)}')
    for i in range(1, 7):
        print(f'Group #{i} >{match[i]}< from the position {match.start(i)} to {match.end(i)}')
    print()

    print(re.findall(r'([a-z]+)(\d*)', r'foo3, im12, go, 24buz42'))
    # -> [('foo', '3'), ('im', '12'), ('go', ''), ('buz', '42')]
    print()

    print(re.split(r'(\s*)([+*/-])(\s*)', r'12  +  13*15   - 6'))
    # -> ['12', '  ', '+', '  ', '13', '', '*', '', '15', '   ', '-', ' ', '6']
    print()

    print(re.split(r'\s*([+*/-])\s*', r'12  +  13*15   - 6'))
    # -> ['12', '+', '13', '*', '15', '-', '6']
    print()

    text = 'We arrive on 03/25/2018. So you are welcome after 04/01/2018.'
    print(re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\g<2>.\g<1>.\g<3>', text))
    print()

    text = "Некоторые хорошие слова подозрительны: хор, хоровод, хороводоводовед."
    print(re.sub(r'\b[XxХх]\w*', repl_fun, text))
    print()

    print(re.sub('\d+', to_cube, 'Было закуплено 12 единиц техники по 410.37 рублей.'))
    print()

    text = 'Московский государственный институт международных отношений'
    print(make_abbreviation(text))
    text = 'микоян авиацию снабдил алкоголем, народ доволен работой авиаконструктора'
    print(make_abbreviation(text))
    print()
    print(is_haiku('Вечер за окном. / Еще один день прожит. / Жизнь скоротечна...'))
    print(is_haiku('Просто текст'))
    print(is_haiku('Как вишня расцвела! / Она с коня согнала / И князя-гордеца.'))
    print(is_haiku('На голой ветке / Ворон сидит одиноко… / Осенний вечер!'))
    print(is_haiku('Тихо, тихо ползи, / Улитка, по склону Фудзи, / Вверх, до самых высот!'))
    print(is_haiku('Жизнь скоротечна… / Думает ли об этом / Маленький мальчик.'))
    print()

    code = 'MyVar17 = OtherVar + YetAnother2Var\nTheAnswerToLifeTheUniverseAndEverything = 42'
    print(to_under_from_camel(code))
    print()

    test_text = 'Довольно распространённая ошибка ошибка — это лишний повтор повтор слова слова. Смешно, не не правда ли? Не нужно портить хор хоровод.'
    print(delete_repeted_words(test_text))
    print()

    test_text = 'Да он олень, а не заяц!'
    print(deer_to_hare(test_text))
    print()

    test_text = '''12 мало 
лучше 123 
1234 почти 
12354 хорошо 
стало 123456 
супер 1234567'''
    print(format_big_numbers(test_text))
    print()

