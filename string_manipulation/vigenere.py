# Description: This program implements the Vigenère cipher.
    # The Vigenère cipher is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution.
    # A keyword is used to choose the alphabet to use to encrypt the message.
    # It is a simple form of polyalphabetic substitution.
    # The Vigenère cipher has been reinvented many times. The method was originally described by Giovan Battista Bellaso in his 1553 book La cifra del. Sig. Giovan Battista Bellaso.
    # A variant of the Vigenère cipher, which uses numbers instead of letters to describe the sequence of shifts, is called a Gronsfeld cipher.

    # The Vigenère cipher is essentially a Caesar cipher with a key word. You shift the letters of the message according to the letters of the key word.
    # If the key word is shorter than the message, the key word is repeated. If the key word is longer than the message, the key word is truncated.
    # The key word is not case sensitive. The message is not case sensitive.

    # The Vigenère cipher is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution.
    # A keyword is used to choose the alphabet to use to encrypt the message.
    # It is a simple form of polyalph

def vigenere(text, key):
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

def vigenere_decrypt(text, key):
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

def vigenere_brute_force(text):
    # Try all possible keys
    for key in range(26):
        print(vigenere_decrypt(text, chr(key + 97)))

text = "Hello, World!"
key = "key"

encrypted_text = vigenere(text, key)
print(encrypted_text)

decrypted_text = vigenere_decrypt(encrypted_text, key)
print(decrypted_text)

brute_force_text = vigenere_brute_force(text)
print(brute_force_text)