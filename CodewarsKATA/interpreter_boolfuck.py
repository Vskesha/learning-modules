import test
from collections import defaultdict


def boolfuck(code, input=""):
    inp = iter([int(b) for c in input for b in reversed(f'{ord(c):0>8b}')])
    data, out = defaultdict(int), []
    cp = dp = lp = 0
    while cp < len(code):
        c = code[cp]
        if lp:
            if c == '[':        lp += 1
            elif c == ']':      lp -= 1
        elif c == '+':          data[dp] ^= 1
        elif c == ',':          data[dp] = next(inp, 0)
        elif c == ';':          out.append(data[dp])
        elif c == '<':          dp -= 1
        elif c == '>':          dp += 1
        elif c == '[' and not data[dp]: lp += 1
        elif c == ']' and data[dp]:     lp -= 1
        cp += lp // abs(lp) if lp else 1
    return ''.join(chr(sum(el * 2**j for j, el in enumerate(out[i:i+8]))) for i in range(0, len(out), 8))


def brainfuck_to_boolfuck(code: str) -> str:
    # I am proud of mine because I've written this map by myself
    command_map = {'+': '>[>]+<[+<]>>>>>>>>>[+]<<<<<<<<<',
                   '-': '>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+]<<<<<<<<<',
                   '<': '<<<<<<<<<',
                   '>': '>>>>>>>>>',
                   ',': '>,>,>,>,>,>,>,>,<<<<<<<<',
                   '.': '>;>;>;>;>;>;>;>;<<<<<<<<',
                   '[': '>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]',
                   ']': '>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]'}
    code = ''.join(command_map[c] for c in code)
    for seq in ('<>', '><', '++'):
        while seq in code:
            code = code.replace(seq, '')
    return code


if __name__ == '__main__':
    test.describe("Empty tests")
    test.assert_equals(boolfuck("", ""), "")
    test.assert_equals(boolfuck(brainfuck_to_boolfuck(""), ""), "")

    test.describe("Single command tests")
    test.assert_equals(boolfuck("<"), "")
    test.assert_equals(boolfuck(">"), "")
    test.assert_equals(boolfuck("+"), "")
    test.assert_equals(boolfuck("."), "")
    test.assert_equals(boolfuck(";"), "\u0000")

    test.describe("I/O tests")
    test.assert_equals(boolfuck(brainfuck_to_boolfuck(",."), "*"), "*")

    test.describe("Hello World test")
    test.assert_equals(boolfuck(
        ";;;+;+;;+;+;+;+;+;+;;+;;+;;;+;;+;+;;+;;;+;;+;+;;+;+;;;;+;+;;+;;;+;;+;+;+;;;;;;;+;+;;+;;;+;+;;;+;+;;;;+;+;;+;;+;+;;+;;;+;;;+;;+;+;;+;;;+;+;;+;;+;+;+;;;;+;+;;;+;+;+;",
        ""), "Hello, world!\n")

    test.describe("Basic tests")
    test.assert_equals(boolfuck(
        ">,>,>,>,>,>,>,>,<<<<<<<[>]+<[+<]>>>>>>>>>[+]+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+]<<<<<<<<;>;>;>;>;>;>;>;<<<<<<<,>,>,>,>,>,>,>,<<<<<<<[>]+<[+<]>>>>>>>>>[+]+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]",
        "Codewars\u00ff"), "Codewars")
    test.assert_equals(boolfuck(
        ">,>,>,>,>,>,>,>,>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]>;>;>;>;>;>;>;>;>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+]+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]>,>,>,>,>,>,>,>,>+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]",
        "Codewars"), "Codewars")
    test.assert_equals(boolfuck(
        ">,>,>,>,>,>,>,>,>>,>,>,>,>,>,>,>,<<<<<<<<+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]>>>>>>>>>>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+]>[>]+<[+<]>>>>>>>>>[+]>[>]+<[+<]>>>>>>>>>[+]<<<<<<<<<<<<<<<<<<+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]>>>>>>>>>>>>>>>>>>>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+]<<<<<<<<<<<<<<<<<<<<<<<<<<[>]+<[+<]>>>>>>>>>[+]>>>>>>>>>>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]<<<<<<<<<<<<<<<<<<+<<<<<<<<+[>+]<[<]>>>>>>>>>[+]+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]>>>>>>>>>>>>>>>>>>>;>;>;>;>;>;>;>;<<<<<<<<",
        "\u0008\u0009"), "\u0048")

    print(boolfuck('>,>,>,>,>,>,>,>,<<<<<<<<>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]>>>>>>>>>>,>,>,>,>,>,>,>,<<<<<<<<>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]<<<<<<<<<>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]>;>;>;>;>;>;>;>;<<<<<<<<<<<<<<<<<>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]', 'VsKesha'))
    print(boolfuck('>,>,>,>,>,>,>,>,>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]>>>>>>>>>>,>,>,>,>,>,>,>,>+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]>;>;>;>;>;>;>;>;<<<<<<<<+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]', 'VsKesha'))

    test.assert_equals(boolfuck(brainfuck_to_boolfuck(',+[-.,+]'), 'Codewars' + chr(255)), 'Codewars')

    test.assert_equals(boolfuck(brainfuck_to_boolfuck(',[.[-],]'), 'Codewars' + chr(0)), 'Codewars')

    test.assert_equals(boolfuck(brainfuck_to_boolfuck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.'), chr(8) + chr(9)), chr(72))

    test.assert_equals(boolfuck(brainfuck_to_boolfuck(',[>,]<[.<]'), 'VsKesha'), 'ahseKsV')
