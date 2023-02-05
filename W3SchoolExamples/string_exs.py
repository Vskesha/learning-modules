import textwrap


def length_string(string):
    return len(string)


def chars_count(string):
    char_map = {}
    for char in string:
        if char in char_map.keys():
            char_map[char] += 1
        else:
            char_map[char] = 1
    return char_map


def first2_last2(string):
    if len(string) < 2:
        return ''
    return string[0:2] + string[-2:]


def replace_next_chars_sametofirst(string: str):
    return string[0] + string[1:].replace(string[0], '$')


def swap2first_and_concat(str1, str2):
    return str2[:2] + str1[2:] + ' ' + str1[:2] + str2[2:]


def ing_ly(str1):
    if len(str1) < 3:
        return str1
    if str1[-3:] == 'ing':
        return str1 + 'ly'
    return str1 + 'ing'


def replace_not_poor(str1: str):
    not_pos = str1.find('not')
    poor_pos = str1.find('poor')
    if poor_pos > not_pos > -1:
        return str1.replace(str1[not_pos:(poor_pos+4)], 'good', 1)
    return str1


def longest_word(word_list: list):
    long_word = ''
    max_len = 0
    for word in word_list:
        if max_len < len(word):
            max_len = len(word)
            long_word = word
    return long_word, max_len


def remove_char(string: str, index: int):
    if len(string) < 1:
        return string
    return string[:index] + string[(index+1):]


def exchange_firs_last(string: str):
    if string:
        return string[-1] + string[1:-1] + string[0]
    return string


def remove_odds(string: str):
    return string[::2]


def word_count(string: str):
    string_list = string.split()
    word_map = {}
    for word in string_list:
        if word in word_map:
            word_map[word] += 1
        else:
            word_map[word] = 1
    return word_map


def lower_upper_userinput(string):
    # string = input('Enter a string: ')
    print(string.upper())
    print(string.lower())


def sorted_distinct_words(string: str):
    list_word = string.lower().split(',')
    return ','.join(sorted(list(set(list_word))))


def add_tags(tag, string):
    # return '<' + tag + '>' + string + '</' + tag + '>'
    return f'<{tag}>{string}</{tag}>'


def insert_string_middle(str1: str, str2: str):
    return str1[:len(str1)//2] + str2 + str1[len(str1)//2:]


def four_copies_of_last(string: str):
    if len(string) < 2:
        return string
    return 4 * string[-2:]


def first_three(string: str):
    return string if len(string) < 3 else string[:3]


def last_part_before_char(string: str, char: str):
    return string.rpartition(char)[0]


def reverse_if_multiple_four(string: str):
    return string if len(string) % 4 else string[::-1]


def upper_if_2of4(string: str):
    count = 0
    for i in range(4):
        if string[i] == string.upper()[i]:
            count += 1
    return string.upper() if count >= 2 else string


def lexicographi_sort(string: str):
    return sorted(string, key=str.upper)


def remove_new_line(string: str):
    return string.splitlines()[0]


def starts_with(string: str, prefix: str):
    return string.startswith(prefix)


def caesar_cipher(string: str, shift=0):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return string.lower().translate(str.maketrans(alphabet, alphabet[(shift % 26):] + alphabet[0:(shift % 26)]))


def format_width(text: str, width: int):
    return textwrap.fill(text=text, width=width)


def text_without_indentations(text: str):
    return textwrap.dedent(text)


def add_prefix_each_line(text: str, prefix: str):
    return textwrap.indent(text, prefix)


def first_line_indent(text: str, first_indent: str = ''):
    return textwrap.fill(textwrap.dedent(text), width=40, initial_indent=first_indent)


def round_2_decimals(number: float):
    return f'{number:.2f}'


def two_decimals_sign(number: float):
    return f'{number:+.2f}'


def no_decimals(number: float):
    return f'{number:.0f}'


def zero_fill(number: int, width: int):
    return str(number).zfill(width)


if __name__ == '__main__':
    print('Length of string is', length_string('w3resource.com'))
    print('Char map is: ', chars_count('google.com'))
    print('first 2 and last 2 is:')
    print(first2_last2('w3resource'))
    print(first2_last2('w3'))
    print(first2_last2('w'))
    print('replace next chars same to firs char: ', replace_next_chars_sametofirst('restart'))
    print('swap two first chars and join strings: ', swap2first_and_concat('abc', 'xyz'))
    print('ing_ly returns :')
    print(ing_ly('ab'))
    print(ing_ly('abc'))
    print(ing_ly('string'))
    print('not_poor return:')
    print(replace_not_poor('The lyrics is not that poor!'))
    print(replace_not_poor('The lyrics is poor!'))
    print('Longest word in the list is:', longest_word(["PHP", "Exercises", "Backend"]))
    print('remove char ==== ', remove_char('Python', 3))
    print('Change first and last letter in string "abcd" : ', exchange_firs_last('abcd'))
    print('Change "12345": ', exchange_firs_last('12345'))
    print('Removing odds "abcdefg" -- ', remove_odds("abcdefg"))
    print('Word count prints: ', word_count('the quick brown fox jumps over the lazy dog'))
    print('Upper lower user inputs', lower_upper_userinput("What's your favourite language? english"))
    print('sorted "The,quick,brown,fox,jumps,over,the,lazy,dog" : ',
          sorted_distinct_words("The,quick,brown,fox,jumps,over,the,lazy,dog"))
    print(add_tags('i', 'Python'))
    print(add_tags('b', 'Python Tutorial'))
    print(insert_string_middle('<<<>>>', 'HTML'))
    print(insert_string_middle('$$$$$', 'PhP'))
    print('Four copies of last:', four_copies_of_last("Python"))
    print('First Three:', first_three('Python'))
    print('Last part: ', last_part_before_char('https://www.w3resource.com/python-exercises/string', '-'))
    print('Reverse if multiple of four:', reverse_if_multiple_four('Python21'))
    print(''.join(reversed('Python')))
    print('Upper if 2of4: ', upper_if_2of4('Python'), upper_if_2of4('pYtHon'), upper_if_2of4('PYThon'))
    print(lexicographi_sort('PythOn'), lexicographi_sort('AbaBAHaLAmahA'), ''.join(lexicographi_sort('AbaBAHaLAmahA')))
    print('Remove_new_line\nremove second line\nthirdline', remove_new_line('Remove_new_line\n'
                                                                            'remove second line\nthirdline'))
    print(starts_with('w3resource.com', 'w3'))
    print('w3resource.com', caesar_cipher('w3resource.com', 3))
    print(caesar_cipher('z3uhvrxufh.frp'), caesar_cipher('z3uhvrxufh.frp', -3))
    sample_text = '''    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''
    print(format_width(sample_text, width=50))
    print(textwrap.fill(text_without_indentations(sample_text), width=60, drop_whitespace=True, replace_whitespace=True))
    print(add_prefix_each_line(text_without_indentations(sample_text), '>'))
    print(first_line_indent(sample_text, '|||||'))
    print(round_2_decimals(3.1415926), round_2_decimals(12.99999))
    print(two_decimals_sign(3.141592), two_decimals_sign(-12.999999))
    print(no_decimals(3.1415), no_decimals(-12.999999))
    print(zero_fill(20, 10), zero_fill(101, 8))
