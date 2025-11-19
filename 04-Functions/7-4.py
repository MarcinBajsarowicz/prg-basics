def cal(s):
    sum = 0
    for char in s:
        if char == 'e':
            sum += 1
    return sum

print(cal('You never get a second chance to make a first impression'))