dogs_age= int(input('Enter your dogs age: '))

if dogs_age <= 2:
    kutaz_dog = dogs_age * 10.5
else:
    kutaz_dog = 2 * 10.5
    kutaz_dog += (dogs_age-2) * 4
print(f'{kutaz_dog}')
