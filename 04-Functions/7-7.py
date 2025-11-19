def f(binary_number):
    for i in binary_number:
        if i!='1' and i!='0':
            return False
        else: 
            return True
print(f("10110101"))