import string

# Normal alphabet
alphabet = string.ascii_lowercase

# Substitution key (26 unique letters)
key = "qwertyuiopasdfghjklzxcvbnm"

# Create dictionaries
encrypt_dict = {}
decrypt_dict = {}

for i in range(26):
    encrypt_dict[alphabet[i]] = key[i]
    decrypt_dict[key[i]] = alphabet[i]


def encrypt(text):
    result = ""
    for char in text.lower():
        if char in encrypt_dict:
            result += encrypt_dict[char]
        else:
            result += char
    return result


def decrypt(text):
    result = ""
    for char in text.lower():
        if char in decrypt_dict:
            result += decrypt_dict[char]
        else:
            result += char
    return result


# Main Program
choice = input("Enter E to Encrypt or D to Decrypt: ").lower()
message = input("Enter your message: ")

if choice == 'e':
    print("Encrypted Text:", encrypt(message))

elif choice == 'd':
    print("Decrypted Text:", decrypt(message))

else:
    print("Invalid choice! Please enter E or D.")
