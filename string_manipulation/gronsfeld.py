# Description: Gronsfeld cipher implementation

# The Gronsfeld cipher is a variant of the Vigenère cipher that uses numbers instead of letters to describe the sequence of shifts.
# The key is a sequence of numbers that is used to shift the letters of the message.
# If the key is shorter than the message, the key is repeated. If the key is longer than the message, the key is truncated.
# The key is not case sensitive. The message is not case sensitive.


def gronsfeld(text, key):
    encrypted_text = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index].lower()) - 97
            if char.islower():
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
            key_index = (key_index + 1) % len(key)
        else:
            encrypted_text += char
    return encrypted_text

def gronsfeld_decrypt(text, key):
    decrypted_text = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index].lower()) - 97
            if char.islower():
                decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97)
            else:
                decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)
            key_index = (key_index + 1) % len(key)
        else:
            decrypted_text += char
    return decrypted_text

def gronsfeld_brute_force(text):
    # Try all possible keys
    for key in range(26):
        print(gronsfeld_decrypt(text, chr(key + 97)))

text = "Hello, World!"
key = "key"

encrypted_text = gronsfeld(text, key)
print(encrypted_text)

decrypted_text = gronsfeld_decrypt(encrypted_text, key)
print(decrypted_text)

brute_force_text = gronsfeld_brute_force(text)
print(brute_force_text)