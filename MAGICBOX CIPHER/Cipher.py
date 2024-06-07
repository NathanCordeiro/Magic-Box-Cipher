import numpy as np

def create_magic_table(keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    table = np.zeros((5, 5), dtype=str)
    used_chars = set()
    # Fill the table with the keyword
    row, col = 0, 0
    for char in keyword.upper():
        if char not in used_chars and char in alphabet:
            table[row, col] = char
            used_chars.add(char)
            col += 1
            if col == 5:
                col = 0
                row += 1
                if row == 5:
                    break
    # Fill the remaining table with the remaining alphabet
    for char in alphabet:
        if char not in used_chars:
            table[row, col] = char
            used_chars.add(char)
            col += 1
            if col == 5:
                col = 0
                row += 1
                if row == 5:
                    break
    return table

def find_char_position(table, char):
    char = char.upper()
    for i in range(5):
        for j in range(5):
            if table[i, j] == char:
                return i, j
    return None, None  # Return None, None if character is not found

def encrypt_message(message, keyword):
    words = message.split()
    table = create_magic_table(keyword)
    encrypted_message = ""
    for word in words:
        encrypted_word = ""
        for char in word:
            if char.isalpha():
                row, col = find_char_position(table, char)
                if row is not None and col is not None:  # Check if position was found
                    encrypted_char = table[(row + 1) % 5, col]
                    if char.islower():
                        encrypted_char = encrypted_char.lower()
                    encrypted_word += encrypted_char
                else:
                    encrypted_word += char  # Leave non-alphabetic characters unchanged
            else:
                encrypted_word += char  # Leave non-alphabetic characters unchanged
        encrypted_message += encrypted_word + " "
    return encrypted_message.strip()

def decrypt_message(encrypted_message, keyword):
    words = encrypted_message.split()
    table = create_magic_table(keyword)
    decrypted_message = ""
    for word in words:
        decrypted_word = ""
        for char in word:
            if char.isalpha():
                row, col = find_char_position(table, char)
                if row is not None and col is not None:  # Check if position was found
                    decrypted_char = table[(row - 1) % 5, col]
                    if char.islower():
                        decrypted_char = decrypted_char.lower()
                    decrypted_word += decrypted_char
                else:
                    decrypted_word += char  # Leave non-alphabetic characters unchanged
            else:
                decrypted_word += char  # Leave non-alphabetic characters unchanged
        decrypted_message += decrypted_word + " "
    return decrypted_message.strip()

# Prompt the user to choose encryption or decryption
choice = input("Do you want to encrypt (E) or decrypt (D) a message? ").upper()

if choice == "E":
    message = input("Enter a message to encrypt: ")
    keyword = input("Enter a keyword: ")
    encrypted_message = encrypt_message(message, keyword)
    print("Encrypted Message:", encrypted_message)
elif choice == "D":
    encrypted_message = input("Enter a message to decrypt: ")
    keyword = input("Enter a keyword: ")
    decrypted_message = decrypt_message(encrypted_message, keyword)
    print("Decrypted Message:", decrypted_message)
else:
    print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")
