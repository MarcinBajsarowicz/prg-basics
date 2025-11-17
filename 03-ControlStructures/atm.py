###
# ATM (cash machine) simulator - WERSJA Z WERYFIKACJĄ PINU
#
balance = 1000.0  # Początkowe saldo
current_pin = '1111' # Aktualny 4-cyfrowy PIN
MAX_ATTEMPTS = 3

# --- WERYFIKACJA PIN-u PRZY STARCI ---
pin_entered_successfully = False

for attempt in range(MAX_ATTEMPTS):
    entered_pin = input("PROSZĘ WPROWADZIĆ PIN (4 cyfry): ")
    
    # Walidacja, czy PIN ma 4 cyfry i składa się tylko z cyfr
    if not (len(entered_pin) == 4 and entered_pin.isdigit()):
        print("Niepoprawny format. PIN musi mieć dokładnie 4 cyfry.")
        continue # Przechodzi do następnej próby

    if entered_pin == current_pin:
        pin_entered_successfully = True
        print("\nPIN poprawny. Witamy!")
        break
    else:
        attempts_left = MAX_ATTEMPTS - 1 - attempt
        if attempts_left > 0:
            print(f"Niepoprawny PIN. Pozostało prób: {attempts_left}")
        else:
            print("Karta zablokowana. Przekroczono liczbę prób.")
            
if not pin_entered_successfully:
    exit() # Zakończenie programu, jeśli weryfikacja PIN-u się nie powiodła

# --- GŁÓWNA PĘTLA MENU ATM ---
while True:
    print("\n" + "="*20)
    print("ATM Menu:")
    print("1. Sprawdź saldo")
    print("2. Wpłać")
    print("3. Wypłać")
    print("4. Zmień PIN")
    print("5. Wyjdź")
    print("="*20)

    choice = input("Wybierz opcję (1-5): ")
    print()

    if choice == '1':
        print(f"Twoje obecne saldo wynosi: €{balance:.2f}")

    elif choice == '2':
        try:
            amount = float(input("Wprowadź kwotę wpłaty: "))
            if amount > 0:
                balance += amount
                print(f"Wpłacono €{amount:.2f}. Nowe saldo: €{balance:.2f}")
            else:
                print("Kwota wpłaty musi być dodatnia.")
        except ValueError:
            print("Niepoprawna kwota.")
            
    elif choice == '3':
        try:
            amount = float(input("Wprowadź kwotę wypłaty: "))
            if amount <= 0:
                 print("Kwota wypłaty musi być dodatnia.")
            elif amount <= balance:
                balance -= amount
                print(f"Wypłacono €{amount:.2f}. Nowe saldo: €{balance:.2f}")
            else:
                print("Niewystarczające saldo.")
        except ValueError:
            print("Niepoprawna kwota.")

    elif choice == "4":
        old_pin = input("Wprowadź aktualny PIN: ")
        if old_pin == current_pin:
            new_pin = input("Wprowadź nowy 4-cyfrowy PIN: ")
            # Użycie isdigit() i sprawdzenie długości
            if len(new_pin) == 4 and new_pin.isdigit():
                current_pin = new_pin
                print("PIN został pomyślnie zmieniony.")
            else:
                print("Niepoprawny nowy PIN. Musi składać się z 4 cyfr.")
        else:
            print("Aktualny PIN jest niepoprawny. Zmiana nieudana.")
            
    elif choice == '5':
        print("Wyjście... Dziękujemy za skorzystanie z bankomatu!")
        break   
        
    else:
        print("Niepoprawna opcja. Spróbuj ponownie (1-5).")