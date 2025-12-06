arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]


name = " "
for i in arr:
    if len(name) < len(i):
        name = i
print(name)