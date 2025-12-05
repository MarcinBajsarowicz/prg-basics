arr = [-15, 8, -31, 47, -2, 19]

largest = arr[0]
smallest = arr[0]
for i in arr:
    if i > largest:
        largest = i
    
    if i < smallest:
        smallest = i

print(smallest, largest)