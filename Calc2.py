expression = 'blank'

while expression != 'end':
    print('')
    expression = input('Input your expression: ')
    if expression[len(expression) - 1].isdigit():
        print('= ', eval(expression))
    elif expression == 'end':
        print('Shutting down... ')
    else:
        print('Enter with only digits and operators!')