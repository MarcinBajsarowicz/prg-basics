def compare(array1, array2):
    
    if len(array1) != len(array2):
        return  False
    
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    return True
                    
print(compare(array1=["Water", "Book", "Sky"], array2=["Water", "Book", "Sky"]))

