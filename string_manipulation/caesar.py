def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Brute force attack
def caesar_brute_force(text):
    # Try all possible shifts
    for shift in range(26):
        print(caesar_decrypt(text, shift))

text = "Hello, World!"
shift = 3

encrypted_text = caesar_encrypt(text, shift)
# print(encrypted_text)

decrypted_text = caesar_decrypt(encrypted_text, shift)
# print(decrypted_text)

brute_force_text = caesar_brute_force(text)
print(brute_force_text)


# def main():
#     text = "Hello, World!"
#     shift = 3
#     encrypted_text = caesar_encrypt(text, shift)
#     print(encrypted_text)
#     decrypted_text = caesar_decrypt(encrypted_text, shift)
#     print(decrypted_text)
#     caesar_brute_force(encrypted_text)

# main()