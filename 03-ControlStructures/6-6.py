hours = int(input('Enter time of car parked: '))
if hours in range(1,2):
    print("Insert 5 pln")
elif hours in range(3,6):
    print("Insert 15 pln")
elif hours > 6:
    print(" Insert 20 pln")
elif hours == 0:
    print("Invalid time of hours")