'''
In this file shown how to use string methods
capitalize()	Converts the first character to upper case
casefold()  	Converts string into lower case
center()	    Returns a centered string
count()     	Returns the number of times a specified value occurs in a string
encode()	    Returns an encoded version of the string
endswith()  	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	        Searches the string for a specified value and returns the position of where it was found
format()	    Formats specified values in a string
format_map()	Formats specified values in a string
index()	        Searches the string for a specified value and returns the position of where it was found
isalnum()   	Returns True if all characters in the string are alphanumeric
isalpha()	    Returns True if all characters in the string are in the alphabet
isascii()   	Returns True if all characters in the string are ascii characters
isdecimal()	    Returns True if all characters in the string are decimals
isdigit()   	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()   	Returns True if all characters in the string are lower case
isnumeric() 	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()   	Returns True if all characters in the string are whitespaces
istitle()   	Returns True if the string follows the rules of a title
isupper()   	Returns True if all characters in the string are upper case
join()      	Converts the elements of an iterable into a string
ljust()     	Returns a left justified version of the string
lower()     	Converts a string into lower case
lstrip()	    Returns a left trim version of the string
maketrans()	    Returns a translation table to be used in translations
partition()	    Returns a tuple where the string is parted into three parts
replace()	    Returns a string where a specified value is replaced with a specified value
rfind()	        Searches the string for a specified value and returns the last position of where it was found
rindex()	    Searches the string for a specified value and returns the last position of where it was found
rjust()	        Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	    Splits the string at the specified separator, and returns a list
rstrip()	    Returns a right trim version of the string
split()	        Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	        Returns a trimmed version of the string
swapcase()	    Swaps cases, lower case becomes upper case and vice versa
title()	        Converts the first character of each word to upper case
translate()	    Returns a translated string
upper()	        Converts a string into upper case
zfill()	        Fills the string with a specified number of 0 values at the beginning
'''

if __name__ == '__main__':
    # string = input('Enter a string: ')
    # if not string:
    string = 'string for testing is "Hello World" і\t "Привіт"'
    print(f'string = {string}')
    print()

    print('Method capitalize() is:')
    print(string.capitalize())
    print()

    print('Method casefold() is:')
    print(string.casefold())
    print()

    print('Method center(100, "_")')
    print(string.center(100, '_'))
    print()

    print('Method count("ing", 0, -4)')
    print(string.count('ing', 0, -4))
    print()

    print('Method encode(encoding="ascii", errors="backslashreplace")')
    print(string.encode(encoding='ascii', errors='backslashreplace'))
    print('Method encode(encoding="ascii", errors="ignore")')
    print(string.encode(encoding='ascii', errors='ignore'))
    print('Method encode(encoding="ascii", errors="namereplace")')
    print(string.encode(encoding='ascii', errors='namereplace'))
    print('Method encode(encoding="ascii", errors="strict")')
    try:
        print(string.encode(encoding='ascii', errors='strict'))
    except UnicodeEncodeError:
        print('catched UnicodeEncodeError')
    print('Method encode(encoding="ascii", errors="replace")')
    print(string.encode(encoding='ascii', errors='replace'))
    print('Method encode(encoding="ascii", errors="xmlcharrefreplace")')
    print(string.encode(encoding='ascii', errors='xmlcharrefreplace'))
    print()

    print('Method endswith("риві", 2, -2)')
    print(string.endswith('риві', 2, -2))
    print()

    print('Method expandtabs()')
    print(string.expandtabs(25))
    print(string.expandtabs(23))
    print(string.expandtabs(21))
    print(string.expandtabs(19))
    print(string.expandtabs(17))
    print(string.expandtabs(15))
    print(string.expandtabs(13))
    print()

    print('Method find()')
    i = 0
    find_list = []
    find_str = 't'
    while True:
        position = string.find(find_str, i)
        if position == -1:
            break
        find_list.append(position)
        i = position + 1
    print(find_list)
    print()

    print('Method format()')
    # named indexes:
    txt1 = "My name is {fname}, I'm {age}".format(fname="John", age=36)
    # numbered indexes:
    txt2 = "My name is {0}, I'm {1}".format("John", 36)
    # empty placeholders:
    txt3 = "My name is {}, I'm {}".format("John", 36)
    print(txt1)
    print(txt2)
    print(txt3)
    print('We have {:<8} chickens'.format(48))
    print(f'We have {48:<8} chickens')
    print('We have {:>10} chickens'.format(48))
    print(f'We have {48:>10} chickens')
    print('We have {:^9} chickens'.format(48))
    print(f'We have {48:^9} chickens')
    print('The temperature is between {1:=4} and {0:=4} celsius'.format(7, -3))
    print(f'The temperature is between {-3:=4} and {7:=4} celsius')
    print('The temperature is between {1:+4} and {0:+4} celsius'.format(7, -3))
    print(f'The temperature is between {-3:+4} and {7:+4} celsius')
    print('The temperature is between {0:-4} and {1:-4} celsius'.format(-3, 7))
    print(f'The temperature is between {-3:-4} and {7:-4} celsius')
    print('The temperarure is between {1: } and {0: } celsius'.format(7, -3))
    print(f'The temperature is between {-3: } and {7: } celsius')
    print('Universe is {years:,} years old'.format(years=13800000000))
    years = 13800000000
    print(f'Universe is {years:,} years old')
    print('Universe is {years:_} years old'.format(years=13800000000))
    print(f'Universe is {years:_} years old')
    num = 252
    num2 = 0o237
    print('Number {0} in binary is {0:b}'.format(num))
    print(f'Number {num} in binary is {num:b}')
    print('Number 0o237 in decimal is {0:d}'.format(num2))
    print(f'Number 0o237 in decimal is {num2:d}')
    print('Scientific lowercase of number {0} is {0:e}'.format(num))
    print(f'Scientific lowercase of number {num} is {num:e}')
    print('Scientific uppercase of number {0} is {0:E}'.format(num))
    print(f'Scientific uppercase of number {num} is {num:E}')
    print('Float number with default decimals is {number:f}'.format(number=num))
    print(f'Float number with default decimals is {num:f}')
    print('Float number with 2 decimals is {:.2f}'.format(num))
    print(f'Float number with 2 decimals is {num:.2f}')
    print('Number {0} in octal is {0:o}'.format(num))
    print(f'Number {num} in octal is {num:o}')
    print('Number {number} in hex lowercase is {number:x}'.format(number=num))
    print(f'Number {num} in hex lowercase is {num:x}')
    print('Number {n} in hex uppercase is {n:X}'.format(n=num))
    print(f'Number {num} in hex uppercase is {num:X}')
    print('Default float number {0} in percentage view by default is {0:%}'.format(num/1000))
    print(f'Default float number {num/1000} in percentage view by default is {num/1000:%}')
    print('Float number with 2 decimals {n:.2f} in percentage view with 2 decimals is {n:.2%}'.format(n=num/1000))
    print(f'Float numver with 2 decimals {num/1000:.2f} in percentage view with 2 decimals is {num/1000:.2%}')
    print()

    print('Method format_map()')
    mapping = {'temp1': -3,
               'temp2': 7}
    print('Temperature is between {temp1:.1f} and {temp2:.1f} celsius'.format_map(mapping))
    print()

    print('Method index(). Carefully because of throwing ValueError')
    string = 'string for testing is "Hello World" і\t "Привіт"'
    print(string)
    print(string.index('for', 2, len(string)))
    try:
        print(string.find('for in'))
        print(string.index('for in'))
    except ValueError:
        print('There is no "for in" in given string')
    print()

    print('Method isalnum()')
    string = 'Company vs 88'
    print(string)
    print(string.isalnum())
    print(string.replace(' ','').isalnum())
    print()

    print('Method isalpha()')
    print(string)
    print(string.isalpha())
    print(string[:-2].isalpha())
    print(string[:-2].replace(' ', '').isalpha())
    print()

    print('Method isascii()')
    print(string)
    print(string.isascii())
    print()

    print('Method isdecimal()')
    string = 'company vs 88'
    a = "\u0030"  # unicode for 0
    b = "\u0047"  # unicode for G
    c = "²"
    d = "\u00B2"  # unicode for ²
    print('c==d',c==d, sep=' ==> ')
    print(string, string.isdecimal(), sep=' ==> ')
    str = string[-2::]
    print(str, str.isdecimal(), sep=' ==> ')
    print(a, a.isdecimal(), sep=' ==> ')
    print(b, b.isdecimal(), sep=' ==> ')
    print(c, c.isdecimal(), sep=' ==> ')
    print()

    print('Method isdigit()')
    print(a, a.isdigit(), sep=' ==> ')
    print(b, b.isdigit(), sep=' ==> ')
    print(c, c.isdigit(), sep=' ==> ')
    print()

    print('Method isnumeric()')
    a = "\u0030"  # unicode for 0
    b = "\u00B2"  # unicode for &sup2;
    c = "¾"
    d = "-1"
    e = "1.5"
    print(a, a.isnumeric(), sep=' ==> ')
    print(b, b.isnumeric(), sep=' ==> ')
    print(c, c.isnumeric(), sep=' ==> ')
    print(d, d.isnumeric(), sep=' ==> ')
    print(e, e.isnumeric(), sep=' ==> ')
    print()

    print('Method isidentifier()')
    a = "MyFolder"
    b = "Demo002"
    c = "2bring"
    d = "my demo"
    print(a, a.isidentifier(), sep=' ==> ')
    print(b, b.isidentifier(), sep=' ==> ')
    print(c, c.isidentifier(), sep=' ==> ')
    print(d, d.isidentifier(), sep=' ==> ')
    print()

    print('Method islower')
    a = "Hello world!"
    b = "hello 123"
    c = "mynameisPeter"
    print(a, a.islower(), sep=' ==> ')
    print(b, b.islower(), sep=' ==> ')
    print(c, c.islower(), sep=' ==> ')
    print()

    print('Method isprintable()')
    a = "Hello!\nAre you #1?"
    b = "Hello! Are you #1?"
    print(a, a.isprintable(), sep=' ==> ')
    print(b, b.isprintable(), sep=' ==> ')
    print()

    print('Method isspace()')
    a = '       '
    b = '    s   '
    print(a, a.isspace(), sep=' ==> ')
    print(b, b.isspace(), sep=' ==> ')
    print()

    print('Method istitle()')
    a = "HELLO, AND WELCOME TO MY WORLD"
    b = "HelLo"
    c = "22 Names"
    d = "This Is %'!?"
    print(a, a.istitle(), sep=' ==> ')
    print(b, b.istitle(), sep=' ==> ')
    print(c, c.istitle(), sep=' ==> ')
    print(d, d.istitle(), sep=' ==> ')
    print()

    print('Method isupper()')
    a = "Hello World!"
    b = "hello 123"
    c = "MY NAME IS PETER"
    print(a, a.isupper(), sep=' ==> ')
    print(b, b.isupper(), sep=' ==> ')
    print(c, c.isupper(), sep=' ==> ')
    print()

    print('Method join()')
    myDict = {"name": "John", "country": "Norway", "age": 35, "wife": True}
    mySeparator = "TEST"
    x = mySeparator.join(myDict)
    print(f'{myDict}, {mySeparator} ==> {x}')
    print()

    print('Method ljust()')
    str = 'banana'
    str2 = 'VsKesha'
    print(f'{str}==>{str.ljust(100, "_")}')
    print(f'{str2}==>{str2.ljust(100, "0")}')
    print()

    print('Method rjust()')
    str = 'banana'
    str2 = 'VsKesha'
    print(f'{str}==>{str.rjust(100, "_")}')
    print(f'{str2}==>{str2.rjust(100, "0")}')
    print()

    print('Method center()')
    str = 'banana'
    str2 = 'VsKesha'
    print(f'{str}==>{str.center(100, "_")}')
    print(f'{str2}==>{str2.center(100, "0")}')
    print()

    print('Method lower()')
    a = "Hello World!"
    b = "hello 123"
    c = "MY NAME IS PETER"
    print(a, a.lower(), sep=' ==> ')
    print(b, b.lower(), sep=' ==> ')
    print(c, c.lower(), sep=' ==> ')
    print()

    print('Mehtod lstrip()')
    str = ",,,,,ssaaww.....banana"
    str2 = "1\t2\n    banana"
    print(str, str.lstrip('wb,as.'), sep=' ==> ')
    print(str2, str2.expandtabs(10).lstrip('2 1\n'), sep=' ==> ')
    print()

    print('Methods maketrans() and translate()')
    string = 'Good evening VsKesha'
    x = 'VKseah'
    y = 'Blouhk'
    z = 'oGd vnig'
    table = string.maketrans(x, y, z)
    for key, value in table.items():
        print(chr(key), ': ', 'delete' if not value else chr(value), sep='')
    print(string, '==>', string.translate(table))
    print()

    print('Method partition()')
    string = 'I could eat bananas all day'
    print(string, '==>', string.partition('banan'))
    print()

    print('Method replace()')
    string ="one one was a race horse, two two was one too."
    print(string, '==>', string.replace('one', 'three', 2))
    print(string, '==>', string.replace(' ', ''))
    print()

    print('Method rfind()')
    string = "one one was a race horse, two two was one too."
    find_str = 'o'
    find_list = []
    i = len(string)
    while True:
        position = string.rfind(find_str, 0, i)
        if position == -1:
            break
        find_list.append(position)
        i = position
    print(find_list[::-1])

    print('Method rindex(). Carefully because of throwing ValueError')
    string = 'string for testing is "Hello World" і\t "Привіт"'
    print(string)
    print(string.rindex('in', 2, len(string)))
    try:
        print(string.rfind('for in'))
        print(string.rindex('for in'))
    except ValueError:
        print('There is no "for in" in given string')
    print()

    print('Method rpartition()')
    string = 'I could eat bananas all day'
    print(string, '==>', string.rpartition('ana'))
    print(string, '==>', string.partition('ana'))
    print()

    print('Methods split() and rsplit()')
    string = "apple#banana#cherry#orange"
    print(string, string.split('#'), sep=' ==> ')
    print(string, string.rsplit('#'), sep=' ==> ')
    print(string, string.split('#', 2), sep=' ==> ')
    print(string, string.rsplit('#', 2), sep=' ==> ')

    print('Method rstrip()')
    txt = "banana,,,,,ssqqqww....."
    print(txt, '==>', txt.rstrip(",.qsw"))
    print()

    print('Method splitlines()')
    txt = "Thank you for the music\nWelcome to the jungle"
    print(txt, '==>', txt.splitlines(True))
    print()

    print('Method startswith()')
    print(txt, '==>', txt.startswith('yo', 6, len(txt)))
    print()

    print('Method strip()')
    txt = ",,,,,rrttgg.....banana....rrr"
    print(txt, '==>', txt.strip(",.grt"))
    print()

    print('Method swapcase()')
    a = "Hello World!"
    b = "hello 123"
    c = "MY NAME IS PETER"
    print(a, a.swapcase(), sep=' ==> ')
    print(b, b.swapcase(), sep=' ==> ')
    print(c, c.swapcase(), sep=' ==> ')
    print()

    print('Method title()')
    a = "Hello WorLd!"
    b = "hello 123"
    c = "MY NAME IS PETER"
    d = "hello b2b2b2 and 3g3g3g"
    e = "Welcome to my 2nd world"
    lst = [a, b, c, d, e]
    for string in lst:
        print(string.ljust(30), '==>', string.title())
    print()

    print('Method upper()')
    for string in lst:
        print(string.ljust(30), '==>', string.upper())
    print()

    print('Method zfill()')
    for s in lst:
        print(s.ljust(30), '==>', s.zfill(100))
