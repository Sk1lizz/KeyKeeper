# src\crypto\crypto.py

""" Все функции для шифровки пароля пользователя """

import os
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

from src.utils.logger import (
    logger,
    debug,
    info,
    warning,
    error,
    critical
)

class CryptoManager:

    @staticmethod
    def generate_salt(size: int = 16) -> bytes:
        """ Генерация соли """

        salt = os.urandom(size)
        debug(f"Сгенирирована соль размером {size} байт.")

        return salt
    
    @staticmethod
    def derive_key(password: str, salt: bytes, iterations: int = 100000) -> bytes:
        """ Генерация ключа шифрования из соли и мастер пароля """

        debug("Генерация ключа шифрования.")

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256,
            length=32,
            salt=salt,
            iterations=iterations
        )

        key = base64.urlsafe_b64decode(kdf.derive(password.encode()))

        debug("Ключ сгенирирован.")

        return key
    
    @staticmethod
    def encrypt(data: str, key: bytes) -> str:
        """ Зашифровка пароля """

        f = Fernet(key)
        encrypted = f.encrypt(data.encode()).decode()
        debug("Данные зашифрованы.")

        return encrypted
    
    @staticmethod
    def encrypt(data: str, key: bytes) -> str:
        """ Расшифровка пароля """

        f = Fernet(key)
        encrypted = f.decrypt(data.encode()).decode()
        debug("Данные расшифрованы.")

        return encrypted