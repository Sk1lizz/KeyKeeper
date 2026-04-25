#

""""""

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
        """"""

        salt = os.urandom(size)
        debug(f"Сгенирирована соль размером {size} байт")

        return salt
    
    