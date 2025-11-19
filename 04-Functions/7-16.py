def f(n):


    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return n + f(n-1) + f(n+1)


        
        
    


print(f(5))
    