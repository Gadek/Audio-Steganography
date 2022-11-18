import os

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

iv = bytes('wavsteganography', 'utf-8')
salt = b'/\x10\x99\xb5\x17$\x86\x01\xe1\xa9\xc3\x04}9}!'
BLOCK_SIZE = 16

def kdf(key: str) -> bytes:
    keyBytes = bytes(key, 'utf-8')

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    
    return kdf.derive(keyBytes)

# def pad(message: str|bytes) -> bytes:
def pad(message) -> bytes:
    if isinstance(message, str):
        message = bytes(message, 'utf-8')
    
    padder = padding.PKCS7(128).padder()

    return padder.update(message) + padder.finalize()

# def unpad(padded_data: bytes, returnAsString: bool = False) -> bytes|str:
def unpad(padded_data: bytes, returnAsString: bool = False):
    unpadder = padding.PKCS7(128).unpadder()
    
    unpadded_data = unpadder.update(padded_data) + unpadder.finalize()

    if returnAsString:
        return unpadded_data.decode('utf-8')
    
    return unpadded_data


# def encrypt(message: str|bytes, key: str|bytes, returnAsString: bool = False) -> str|bytes:
# def encrypt(message: str|bytes, key: str|bytes, returnAsString: bool = False):
def encrypt(message, key, returnAsString: bool = False):
    if isinstance(key, str):
        key = kdf(key)
    
    if isinstance(message, str):
        message = bytes(message, 'utf-8')
    
    message = pad(message)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    
    ct = encryptor.update(message) + encryptor.finalize()
    
    if returnAsString:
        return ct.decode('utf-8')

    return ct

# def decrypt(ct: bytes, key: str|bytes) -> str:
def decrypt(ct: bytes, key) -> str:
    if isinstance(key, str):
        key = kdf(key)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    decryptet_message = decryptor.update(ct) + decryptor.finalize()

    decryptet_message_str = unpad(decryptet_message, True)
    
    return decryptet_message_str
