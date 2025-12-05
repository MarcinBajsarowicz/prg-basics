arr = [34, 7, 19, 4, 21, 8]

count = 0
i = 0

while i < len(arr):
    digit = arr[i]

    if digit % 2 == 0:
        count += 1

    i += 1

print(count)