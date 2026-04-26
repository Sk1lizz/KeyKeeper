# 

""""""

from typing import List, Optional
from pathlib import Path

from src.models.password_entry import EntryPassword
from src.database.db_manager import DatabaseManager
from src.crypto.crypto import CryptoManager
from src.utils.logger import (
    logger,
    debug,
    info,
    warning,
    error,
    critical
)


class PasswordController:
    """"""

    def __init__(self, db_path: Path, key: bytes):
        """"""

        self.db = DatabaseManager(db_path)
        self.key = key
        self.crypto = CryptoManager()
        
        info("PasswordController инициализирован")


    def add_entry(self, title: str, username: str, password: str,
                url: str = "", notes: str = "", category: str = "Другое") -> int:
        """"""

        encrypted_password = self.crypto.encrypt(password, self.key)

        entry = EntryPassword(
            title=title,
            username=username,
            password=encrypted_password,
            url=url,
            notes=notes,
            category=category
        )

        entry_id = self.db.add_entry(entry)
        info(f"Добавлена запись '{title}' (ID: {entry_id})")

        return entry_id


    def get_all_entries(self) -> List[EntryPassword]:
        """"""

        entries = self.db.get_all_entries()

        for entry in entries:
            try:
                decrypted = self.crypto.decrypt(entry.password, self.key)
                entry.password = decrypted

            except Exception as e:
                error(f"Ошибка расшифровки записи {entry.id}: {e}")
                entry.password = "[Ошибка расшифровки]"

        debug(f"Загружено {len(entries)} записей")

        return entries
    
    def get_entry_by_id(self, entry_id: int) -> EntryPassword:
        """"""

        entry = self.db.get_entry_by_id(entry_id)

        try:
            decrypted = self.crypto.decrypt(entry.password, self.key)
            entry.password = decrypted

        except Exception as e:
            error(f"Ошибка расшифровки записи {entry_id}: {e}")
            entry.password = "[Ошибка расшифровки]"

        return entry