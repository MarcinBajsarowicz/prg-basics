def f(number1,number2,operator):
    
    if operator == '+':
        actions = number1 + number2
    elif operator == '%':
        actions = number1 % number2
    elif operator == '**':
        actions = number1 ** number2
    elif operator == '*':
        actions = number1 * number2
    elif operator == '-':
        actions = number1 - number2
    return actions

print(f(2,3,'-'))