def interpreter(code, iterations, width, height):
    grid = [[0]*width for _ in range(height)]
    looping, horizontal_pointer, vertical_pointer, code_position = 0, 0, 0, 0
    while iterations and code_position < len(code):
        command = code[code_position]
        if looping:
            if command == '[':
                looping += 1
            elif command == ']':
                looping -= 1
        else:
            if command in 'swen*[]':
                iterations -= 1
            if command == 'e':
                horizontal_pointer = (horizontal_pointer + 1) % width
            elif command == 'w':
                horizontal_pointer = (horizontal_pointer - 1) % width
            elif command == 's':
                vertical_pointer = (vertical_pointer + 1) % height
            elif command == 'n':
                vertical_pointer = (vertical_pointer - 1) % height
            elif command == '*':
                grid[vertical_pointer][horizontal_pointer] ^= 1
            elif command == '[' and not grid[vertical_pointer][horizontal_pointer]:
                looping += 1
            elif command == ']' and grid[vertical_pointer][horizontal_pointer]:
                looping -= 1
        code_position += looping // abs(looping) if looping else 1
    return '\r\n'.join(''.join(str(n) for n in row) for row in grid)


if __name__ == '__main__':
    print(interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 0, 6, 9) == "000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000")
    print(interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 7, 6, 9) == "111100\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000")
    print(interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 19, 6, 9) == "111100\r\n000010\r\n000001\r\n000010\r\n000100\r\n000000\r\n000000\r\n000000\r\n000000")
    print(interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 42, 6, 9) == "111100\r\n100010\r\n100001\r\n100010\r\n111100\r\n100000\r\n100000\r\n100000\r\n100000")
    print(interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 100, 6, 9) == "111100\r\n100010\r\n100001\r\n100010\r\n111100\r\n100000\r\n100000\r\n100000\r\n100000")
