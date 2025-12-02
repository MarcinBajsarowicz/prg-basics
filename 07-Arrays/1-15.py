###
# Bubble sort
#
def bubble_sort(arr):
    n = len(arr) # dlugosc tablicy
    for i in range(n-1): #zmniejszenie zakresu o 1
        for j in range(n-i-1):      # n - 0 - 1, 
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    return arr
    
    
qutaz = [ 8,1,3,2,5,5,6,4]    

print(bubble_sort(qutaz))
 

   



