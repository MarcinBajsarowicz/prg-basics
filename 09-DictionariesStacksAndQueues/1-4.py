person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}
print(f'{person["name"]}')
print(f'{person["hobby"]}')

for key,value in person:
    print(f'{key} : {value}')

person['surname'] = 'Nowak'

person['married'] = False


