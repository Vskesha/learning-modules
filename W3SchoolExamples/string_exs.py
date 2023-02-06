import textwrap
import collections
from string import ascii_lowercase
import itertools


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
    for ind in range(4):
        if string[ind] == string.upper()[ind]:
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


def right_marks(number: int, width: int):
    return str(number).ljust(width, '*')


def comma_separate(number: float):
    return '{:,}'.format(number)


def perc(number: float):
    return '{:.2%}'.format(number)


def left_center_right(number: float, width: int):
    left = str(number).ljust(width)
    center = str(number).center(width)
    right = str(number).rjust(width)
    return left, center, right


def count_occurrences(string: str, substring: str):
    return string.count(substring)


def reverse_string(string: str):
    return string[::-1]


def reverse_words(string: str):
    return ' '.join(reversed(string.split()))


def remove_letters(string: str, letters: str):
    for letter in letters:
        string = string.replace(letter, '')
    return string
    # Another way is
    # return ''.join(letter for letter in string if letter not in letters)


def count_repeated_characters(string: str):
    count_dict = collections.defaultdict(int)
    for char in string.replace(' ', ''):
        count_dict[char] += 1
    print(count_dict)
    return {keyy: count_dict[keyy] for keyy in sorted(count_dict, key=count_dict.get,
                                                      reverse=True) if count_dict[keyy] > 1}


def superscript(string: str):
    superscript_map = {
        "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶",
        "7": "⁷", "8": "⁸", "9": "⁹", "a": "ᵃ", "b": "ᵇ", "c": "ᶜ", "d": "ᵈ",
        "e": "ᵉ", "f": "ᶠ", "g": "ᵍ", "h": "ʰ", "i": "ᶦ", "j": "ʲ", "k": "ᵏ",
        "l": "ˡ", "m": "ᵐ", "n": "ⁿ", "o": "ᵒ", "p": "ᵖ", "q": "۹", "r": "ʳ",
        "s": "ˢ", "t": "ᵗ", "u": "ᵘ", "v": "ᵛ", "w": "ʷ", "x": "ˣ", "y": "ʸ",
        "z": "ᶻ", "A": "ᴬ", "B": "ᴮ", "C": "ᶜ", "D": "ᴰ", "E": "ᴱ", "F": "ᶠ",
        "G": "ᴳ", "H": "ᴴ", "I": "ᴵ", "J": "ᴶ", "K": "ᴷ", "L": "ᴸ", "M": "ᴹ",
        "N": "ᴺ", "O": "ᴼ", "P": "ᴾ", "Q": "Q", "R": "ᴿ", "S": "ˢ", "T": "ᵀ",
        "U": "ᵁ", "V": "ⱽ", "W": "ᵂ", "X": "ˣ", "Y": "ʸ", "Z": "ᶻ", "+": "⁺",
        "-": "⁻", "=": "⁼", "(": "⁽", ")": "⁾"}
    transtable = str.maketrans(superscript_map)
    return string.translate(transtable)


def char_position(string: str):
    for pos, char in enumerate(string):
        print(f'Current character {char} position at {pos}')


def is_all_alphabet_letters(string: str):
    alphabet = ascii_lowercase
    # print(alphabet)
    for let in alphabet:
        if let not in string.lower():
            return False
    return True


def analog_split(string: str):
    return string.split()


def lowercase_n_characters(string: str, n: int):
    return string[0:n].lower() + string[n:]


def swap_commas_dots(string: str):
    transtab = str.maketrans(',.', '.,')
    return string.translate(transtab)


def count_and_return_vowels(string: str):
    count_vowels = 0
    vowel_list = list()
    for vowel in 'aeyuio':
        if vowel in string.lower():
            vowel_list.append(vowel)
            count_vowels += string.count(vowel)
    return count_vowels, vowel_list


def split_n_delimiter(string: str, delimiter=' ', maxsplit=-1):
    return string.rsplit(sep=delimiter, maxsplit=maxsplit)


def first_non_repeating_character(string: str):
    for char in string.replace(' ','').lower():
        if string.lower().count(char) == 1:
            return char
    return None


def all_repeat(string: str, rep_number: int = 1):
    return [rep for rep in itertools.product(string, repeat=rep_number)]


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
    print(textwrap.fill(text_without_indentations(sample_text), width=60, 
                        drop_whitespace=True, replace_whitespace=True))
    print(add_prefix_each_line(text_without_indentations(sample_text), '>'))
    print(first_line_indent(sample_text, '|||||'))
    print(round_2_decimals(3.1415926), round_2_decimals(12.99999))
    print(two_decimals_sign(3.141592), two_decimals_sign(-12.999999))
    print(no_decimals(3.1415), no_decimals(-12.999999))
    print(zero_fill(20, 10), zero_fill(101, 8))
    print(right_marks(123, 10))
    print('{:*<10d}'.format(123))
    print(comma_separate(30000000.890890))
    print(perc(0.25), perc(2.34567))
    print('Left, center and right alignment of number 22, width = 10')
    print(*left_center_right(22, 10), sep='\n')
    print('and by formatted placeholders: ')
    print('{0:<10}\n{0:^10}\n{0:>10}\n'.format(22))
    print(count_occurrences('Welcome to w3resource.com', 'w3'))
    print(f'Reverse to "placeholder" is: "{reverse_string("placeholder")}"')
    print(''.join(reversed("placeholder")))
    print('The quick brown fox')
    print(reverse_words('The quick brown fox'))
    print('The quick brown fox')
    print(remove_letters('The quick brown fox', 'aeiou'))
    for key, value in count_repeated_characters('the quick brown fox jumps over the lazy dog').items():
        print(f'{key}: {value}')
    for i in range(100):
        for j in range(100):
            if i*100+j > 7450:
                print(chr(i*100+j), end=' ')
        print()
    print('\u00b3', ord('\u00b3'), chr(ord('\u00b3')))
    print('superstring', superscript('The brown fox jumps over the lazy dog'))
    print(f'cubic cm: cm{superscript("3")} and square cm is: cm{superscript("2")}')
    print('and what about this?')
    print('01234567890 ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz')
    print(superscript('01234567890 ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz'))
    # for char in superscript('01234567890 ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz'):
    #     print(f'{char}: {ord(char)}')
    char_position('JavaScript')
    print(is_all_alphabet_letters('The quick brown fox jumps over the lazy dog'))
    print(is_all_alphabet_letters('The quick brown fox jumps over the lazy cat'))
    print(analog_split('This is a test string'))
    print(lowercase_n_characters('W3RESOURCE.COM', 4))
    print(swap_commas_dots('32.054,23'))
    for x in count_and_return_vowels('Welcome to w3resources.com'):
        print(x)
    print(split_n_delimiter('w,3,r,e,s,o,u,r,c,e', ',', 1))
    print(split_n_delimiter('w,3,r,e,s,o,u,r,c,e', ',', 2))
    print(split_n_delimiter('w,3,r,e,s,o,u,r,c,e', ',', 5))
    print(first_non_repeating_character('abcdef'))
    print(first_non_repeating_character('abcabcdef'))
    print(first_non_repeating_character('aabbcc'))
    print(all_repeat('xyz', 3))
    print(all_repeat('xyz', 2))
    print(all_repeat('abcd', 4))
    for numb in all_repeat(range(2), 4):
        print(*numb, sep='')