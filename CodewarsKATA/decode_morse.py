# from preloaded import MORSE_CODE
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
MORSE_CODE = {value: key for key, value in MORSE_CODE_DICT.items()}


def decode_morse2(morse_code):
    string = ''
    for word in morse_code.strip().split('   '):
        w = ''
        for ch in word.split(' '):
            w =  w + MORSE_CODE[ch]
        string += w
        string += ' '
    return string.strip()


def decode_morse(morse_code: str):
    return ' '.join(''.join(MORSE_CODE[ch] for ch in word.split(' ')) for word in morse_code.strip().split('   '))


if __name__ == '__main__':
    # print(MORSE_CODE)
    print(decode_morse('.... . -.--   .--- ..- -.. .'))
