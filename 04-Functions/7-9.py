def f(number, even):
    number_s = str(number) 
    # Zmieniamy liczbe na stringa aby w petli swobodnie poruszac sie po kazdym char  
    sum = 0 # Jezeli nie dam 0 to bedzie nie prawdziwy wynik
    
    if even == True: #Sprawdza czy drugi argument  funkcji jest parzysty czy nieparzysty
        for char in range(len(number_s)):   # Dla znaku w moim slowie 
            digit = int(number_s[char])     # Zmiana stringa spowrotem na liczbe. Znak na jakiejs pozycji
            if digit % 2 == 0:      # Sprawdzamy czy liczba jest parzysta
                sum += digit        # Dodaje do siebie liczby parzyste 
    elif even == False:             #Sprawdzamy dla liczb nieparzystych
        for char in range(len(number_s)):
            digit = int(number_s[char])
            if digit % 2 != 0:
                sum += digit
    
    return sum

print(f(3124, True))
print(f(3124, False))