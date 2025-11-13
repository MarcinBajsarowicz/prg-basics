arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print("Last value", arr[-1])
print("Last value", arr[len(arr)-2]) 
print("Sum of first and last number is", arr[0] + arr[-1])
print("Middle value", arr[int(len(arr)/2)])
for value in arr:
    print(value, end=" ")