###
# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ')
last = input('Enter last letter: ')
first_letter_code = ord(first)
second_letter_code = ord(last)
number_of_letters = second_letter_code - first_letter_code - 1
print(f'Number of letters between {first} and {last} is {number_of_letters}')
print(f'Between {first} and {last} is {number_of_letters} letters')