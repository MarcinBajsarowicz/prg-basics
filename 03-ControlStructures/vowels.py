###
# Counts vowels in the text using a while loop
#
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0
i = 0 # Inicjalizacja indeksu

# Count vowels in the text
# Warunek pętli: Kontynuuj, dopóki indeks 'i' jest mniejszy niż długość tekstu
while i < len(text):
    # Pobierz znak na aktualnej pozycji 'i'
    char = text[i] 
    
    # Sprawdź, czy znak jest samogłoską
    if char in vowels:
        vowel_count += 1
        
    # KOREKTA: Przejdź do następnego znaku (zwiększ indeks)
    # Ta linia musi być poza 'if', aby pętla się nie zawieszała.
    i += 1 

print(f"The number of vowels in the text is: {vowel_count}")
