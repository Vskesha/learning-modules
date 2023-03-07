import test
from collections import defaultdict

def brain_luck2(code, program_input):
    data = [0] * 5000
    code_pos = data_pointer = input_pos = looping = 0
    result_string = ''
    while code_pos < len(code):
        command = code[code_pos]
        if looping:
            if command == '[':
                looping += 1
            if command == ']':
                looping -= 1
        elif command == '>':
            data_pointer += 1
        elif command == '<':
            data_pointer -= 1
        elif command == '+':
            data[data_pointer] = (data[data_pointer] + 1) % 256
        elif command == '-':
            data[data_pointer] = (data[data_pointer] - 1) % 256
        elif command == '.':
            result_string += chr(data[data_pointer])
        elif command == ',':
            data[data_pointer] = ord(program_input[input_pos])
            input_pos += 1
        elif command == '[' and not data[data_pointer]:
            looping += 1
        elif command == ']' and data[data_pointer]:
            looping -= 1
        code_pos += looping // abs(looping) if looping else 1
    return result_string


# In a nutshell
def brain_luck(code, program_input):
    inp, data, out = iter(program_input), defaultdict(int), []
    cp = dp = lp = 0
    while cp < len(code):
        c = code[cp]
        if lp:
            if c == '[':                lp += 1
            elif c == ']':              lp -= 1
        elif c == '>':                  dp += 1
        elif c == '<':                  dp -= 1
        elif c == '+':                  data[dp] = (data[dp] + 1) % 256
        elif c == '-':                  data[dp] = (data[dp] - 1) % 256
        elif c == '.':                  out.append(chr(data[dp]))
        elif c == ',':                  data[dp] = ord(next(inp))
        elif c == '[' and not data[dp]: lp += 1
        elif c == ']' and data[dp]:     lp -= 1
        cp += lp // abs(lp) if lp else 1
    return ''.join(out)


if __name__ == '__main__':
    # Echo until byte(255) encountered
    test.assert_equals(
        brain_luck(',+[-.,+]', 'Codewars' + chr(255)),
        'Codewars'
    );

    # Echo until byte(0) encountered
    test.assert_equals(
        brain_luck(',[.[-],]', 'Codewars' + chr(0)),
        'Codewars'
    );

    # Two numbers multiplier
    test.assert_equals(
        brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)),
        chr(72)
    )