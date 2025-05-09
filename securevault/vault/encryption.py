from cryptography.fernet import Fernet

def make_key():
    return Fernet.generate_key()

print(make_key())