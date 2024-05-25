import secrets
import string


def generate_password(length: int) -> str:
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))


print(generate_password(10))