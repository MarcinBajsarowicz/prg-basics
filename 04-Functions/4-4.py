###
# Calculates the sum of the digits in a number
import math

def sum_digits(number):
    number_str = str(number)
    total = sum(int(digit) for digit in number_str)
    return total

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')