def f(n1, n2, n3):

    flag = True


    if n1 >= 0 and n2 >= 0 and n3 >= 0:
        flag = False
    else:
        flag = True
    
    return flag

print(f(1,4,6))   