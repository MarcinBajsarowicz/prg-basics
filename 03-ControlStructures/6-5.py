###
# Program that simulates the operation of an electronic thermometer.
#
temperature = -2
if temperature >= 35:
    print("It is extermely hot")
elif temperature >= 30:
    print("It is hot") 
elif temperature > 15:
    print(f"Its warm for a temperature at least {temperature}")
elif temperature >= 0: 
    print("It is cold outside")
elif temperature < 0:
    print("Warining frost")