n1 = int(input("Enter your speed: "))


speed_ms = lambda ms: ms * 3.6

result = speed_ms(n1)

print(f'{n1} m/s = {result} km/h')