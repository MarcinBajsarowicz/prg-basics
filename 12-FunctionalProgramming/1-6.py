n1 = int(input("Enter your distance: "))
n2 = int(input("Enter time travel in hours: "))
n3 = int(input("Enter time travel in minutes: "))


avg_speed = lambda distance,hours,minutes: round(distance / (hours + (minutes / 60)), 2)


result = avg_speed(n1,n2,n3)
print(f'Average speed: {result} km/h ')
