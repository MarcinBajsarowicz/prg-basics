def bubblesort(arr):
    n = len(arr) # n to długość listy
    
    # Pętla zewnętrzna: decyduje ile razy musimy przejść przez listę
    # (zazwyczaj n razy)
    for i in range(n): 
        
        # Pętla wewnętrzna: "bąbelek", który idzie przez listę i porównuje sąsiadów.
        # Musi iść od 0 do n-1
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                

            
            # Tutaj na razie tylko wypiszmy sobie pary, żeby zobaczyć czy działa
            # Dostęp do elementu to arr[j] (lewy sąsiad) i arr[j+1] (prawy sąsiad)
             # 'pass' to "nic nie rób", wstawiliśmy to, żeby kod był poprawny składniowo
    
    return arr

print(bubblesort([5,2,8]))