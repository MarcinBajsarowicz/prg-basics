def occurs(number, array):
    for i in array:
        if i == number:
            print(array)
            print('The number appears in array', number)
            return True
    return False
    
    

print(occurs(23,[15, 38, 7, 23, 14]))