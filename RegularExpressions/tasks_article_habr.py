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
