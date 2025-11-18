age = int(input("How old are you? "))

if age < 13:
    print("You are a Child")
elif age in range(13,19):
    print('You are a Teen')
elif age in range(20,65):
    print('You are a Adult')
elif age >= 65:
    print('You are a Senior')