# crypto_utils.py
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.keywrap import aes_key_wrap
import os

def generate_aes_key(key_size=32):
    """Gera uma chave AES de 256 bits (32 bytes)"""
    return os.urandom(key_size)
