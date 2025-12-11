def ms_to_kmh(ms):
    result = ms * 3.6
    return result

n1 = int(input("Enter your speed: "))

result = ms_to_kmh(n1)

print(f'{n1} m/s = {result} km/h')