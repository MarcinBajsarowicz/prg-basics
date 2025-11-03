###
# A program that calculates the number of characters
# of your name, surname and full name
#
name = 'Marcin'   # replace Anna with your name
surname = 'Bajsarowicz' # replace May with your surname
characters_in_name = len(name)
characters_in_surname = len(surname) 
characters_in_full_name = len( name + surname + " ")
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has  {characters_in_surname} letters ')
print(f'Your full name has {characters_in_full_name}') # with a space between name and surname