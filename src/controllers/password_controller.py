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
    

    def update_entry(self, entry_id: int, title: str = None, 
                    username: str = None, password: str = None, 
                    url: str = None, notes: str = None,
                    category: str = None, favorite: bool = None) -> bool:
        """"""

        existing = self.db.get_entry_by_id(entry_id)

        if not existing:
            warning(f"Запись с ID {entry_id} не найдена")
            return False

        new_title = title if title is not None else existing.title
        new_username = username if username is not None else existing.username
        new_url = url if url is not None else existing.url
        new_notes = notes if notes is not None else existing.notes
        new_category = category if category is not None else existing.category
        new_favorite = favorite if favorite is not None else existing.favorite

        if password is not None:
            new_password = self.crypto.encrypt(password, self.key)

        else:
            new_password = existing.password

        update_entry = EntryPassword(
            id=entry_id,
            username=new_username,
            password=new_password,
            url=new_url,
            notes=new_notes,
            category=new_category,
            favorite=new_favorite,
        )

        result = self.db.update_entry(update_entry)

        if result:
            info(f"Запись '{new_title}' (ID: {entry_id}) обновлена")

        return result
    

    def delete_entry(self, entry_id: int) -> bool:
        """"""

        result = self.db.delete_entry(entry_id)
        if result:
            debug(f"Запись с ID {entry_id} удалена")

        return result
    

    def delete_all_entries(self) -> int:
        """"""

        count = self.db.delete_all_entries()
        info(f"Удалено {count} записей")

        return count
    

    def search_entries(self, query: str) -> List[EntryPassword]:
        """"""

        all_entries = self.get_all_entries()
        query_lower = query.lower()

        results = [
            entry for entry in all_entries
            if query_lower in entry.title.lower()
            or query_lower in entry.username.lower()
        ]

        debug(f"Поиск '{query}': найдено {len(results)} записей")

        return results   
    
    
    def get_entries_by_category(self, category: str) -> List[EntryPassword]:
        """"""

        all_entries = self.get_all_entries()
        category_lower = category.lower()

        results = [
            entry for entry in all_entries
            if category_lower == entry.category.lower()
        ] 

        debug(f"Категория {category}: {len(results)} записей")

        return results
    


    def close(self) -> None:
        """"""

        self.db.close()
        info("PasswordController закрыт")