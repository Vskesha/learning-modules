import test


def simple_assembler(program):
    # return a dictionary with the registers
    registers = {}
    code_pointer = 0
    while code_pointer < len(program):
        line = program[code_pointer].split()
        command = line[0]
        register = line[1]
        if command == 'inc':
            registers[register] += 1
        elif command == 'dec':
            registers[register] -= 1
        elif command == 'mov':
            val = line[2]
            registers[register] = registers[val] if val.isalpha() else int(val)
        elif command == 'jnz' and (registers[register] if register.isalpha() else int(register)):
            code_pointer += int(line[2]) - 1
        code_pointer += 1
    return registers


if __name__ == '__main__':
    code = 'mov a 5\ninc a\ndec a\ndec a\njnz a -1\ninc a'
    test.assert_equals(simple_assembler(code.splitlines()), {'a': 1})

    code = 'mov c 12\nmov b 0\nmov a 200\ndec a\ninc b\njnz a -2\ndec c\nmov a b\njnz c -5\njnz 0 1\nmov c a'''
    test.assert_equals(simple_assembler(code.splitlines()), {'a': 409600, 'c': 409600, 'b': 409600})