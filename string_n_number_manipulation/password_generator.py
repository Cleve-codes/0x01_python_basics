import secrets
import string


# def generate_password(length: int) -> str:
#     alphabet = string.ascii_letters + string.digits + string.punctuation
#     return ''.join(secrets.choice(alphabet) for _ in range(length))

def generate_password(length: int, uppercase: bool = True, lowercase: bool = True, digits: bool = True, special: bool = True) -> str:
    alphabet = ''
    if uppercase:
        alphabet += string.ascii_uppercase
    if lowercase:
        alphabet += string.ascii_lowercase
    if digits:
        alphabet += string.digits
    if special:
        alphabet += string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))


print(generate_password(10))