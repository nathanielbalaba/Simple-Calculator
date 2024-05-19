while True:
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    operation = input('Enter operation (+, -, *, /): ')

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = 'Error: Division by zero'
    else:
        result = 'Error: Invalid operation'

    print('The result is:', result)

    retry = input("Do you want to try again (Y/N): ")
    if retry.lower() != 'n':
        break
