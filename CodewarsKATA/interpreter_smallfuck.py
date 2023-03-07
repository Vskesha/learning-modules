def interpreter2(code, tape):
    opened_brackets = []
    jump_forward = {}
    for i, c in enumerate(code):
        if c == '[':
            opened_brackets.append(i)
        elif c == ']':
            jump_forward[opened_brackets.pop()] = i
    jump_backward = {v: k for k, v in jump_forward.items()}
    i = 0
    pointer = 0
    tape = [int(c) for c in tape]
    while i < len(code):
        command = code[i]
        if command == '>':
            pointer += 1
        elif command == '<':
            pointer -= 1
        elif command == '*':
            tape[pointer] = 0 if tape[pointer] else 1
        elif command == '[':
            i = i if tape[pointer] else jump_forward[i]
        elif command == ']':
            i = jump_backward[i] if tape[pointer] else i
        if pointer < 0 or pointer >= len(tape):
            break
        i += 1
    return ''.join(str(n) for n in tape)


def interpreter(code, tape):
    tape = list(map(int, tape))
    ptr = step = loop = 0

    while 0 <= ptr < len(tape) and step < len(code):
        command = code[step]

        if loop:
            if command == "[":
                loop += 1
            elif command == "]":
                loop -= 1

        elif command == ">":
            ptr += 1
        elif command == "<":
            ptr -= 1
        elif command == "*":
            tape[ptr] ^= 1
        elif command == "[" and tape[ptr] == 0:
            loop += 1
        elif command == "]" and tape[ptr] == 1:
            loop -= 1

        step += 1 if not loop else loop // abs(loop)

    return "".join(map(str, tape))


if __name__ == '__main__':
    print('Test', 'ok' if interpreter('[>*>*[>*>*>*>*>*]>>*<*<]*>*>*>*>[>>>>>*<*<<*]>>>*<*', '00101010101110110010010001110001') == '11011000101110110010010001110001' else 'fail')
    print('Test', 'ok' if interpreter("*", "00101100") == "10101100" else 'fail')
    print('Test', 'ok' if interpreter(">*>*", "00101100") == "01001100" else 'fail')
    print('Test', 'ok' if interpreter("*>*>*>*>*>*>*>*", "00101100") == "11010011" else 'fail')
    print('Test', 'ok' if interpreter("*>*>>*>>>*>*", "00101100") == "11111111" else 'fail')
    print('Test', 'ok' if interpreter(">>>>>*<*<<*", "00101100") == "00000000" else 'fail')
