if __name__ == '__main__':
    result = None
    operand = None
    operator = None
    wait_for_number = True

    while True:
        if wait_for_number:
            num = input('Enter number: ')
            try:
                operand = float(num)
            except ValueError:
                print(f"'{num}' is not a number. Try again")
                continue
            else:
                wait_for_number = not wait_for_number
            if result == None:
                result = operand
            elif operator == '+':
                result += operand
            elif operator == '-':
                result -= operand
            elif operator == '*':
                result *= operand
            elif operator == '/':
                result /= operand
        else:
            operator = input('Enter operator: ')
            if operator in ('+', '-', '*', '/'):
                wait_for_number = not wait_for_number
            elif operator == '=':
                print(result)
                break
            else:
                print(f"{operator} is not '+' or '-' or '/' or '*'. Try again")
                continue

    # ["10", "+", "5", "6", "/", "3", "-", "a", "2", "*", "6", "= "]   ===  18.0
    # ["2", "3", "-", "1", "+", "10", "*", "2", "="] === 22.0
