def f(x,y):
    
    sum = 0

    for i in range(x,y):        #Dla i w przedziale (x,y)
        if i % 2 == 0 and i < 0:  # jezeli i jest parzyste i mniejsze od zera
            sum += 1

    return sum        
        
print(f(-7,8))
