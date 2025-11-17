###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # 1. Read the character's code (use ord())
    char_code = ord(char)
    
    # 2. Check if the character is a letter (A-Z or a-z)
    if 'a' <= char <= 'z':
        # Apply shift (add one)
        new_code = char_code + 1
        # Handle wrap-around for lowercase letters ('z' -> 'a')
        if new_code > ord('z'):
            new_code = ord('a')
    elif 'A' <= char <= 'Z':
        # Apply shift (add one)
        new_code = char_code + 1
        # Handle wrap-around for uppercase letters ('Z' -> 'A')
        if new_code > ord('Z'):
            new_code = ord('A')
    else:
        # If it's a space or punctuation, keep the original code
        new_code = char_code

    # 3. Replace new character code with its corresponding character (use chr())
    encrypted_char = chr(new_code)
    
    # 4. Add encrypted character to encrypted text
    encrypted_text += encrypted_char

print(f'Original Text: {plain_text}')
print(f'Encrypted Text: {encrypted_text}')