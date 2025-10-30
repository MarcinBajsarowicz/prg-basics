###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = input("Enter a number")
number2 = input("Enter another number")
operator = input("Choose which operation you would like to use")
number1 = float(number1)
number2 = float(number2)

if operator == "+" :
    result = number1 + number2 
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    result = number1 / number2

# print result
print(f'{number1} {operator} {number2} = {result}')