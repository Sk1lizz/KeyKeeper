# 

"""  """

import sqlite3
from pathlib import Path
from typing import List, Optional

from src.utils.logger import (
    logger,
    debug,
    info,
    warning,
    error,
    critical
)
from src.models.password_entry import EntryPassword


class DatabaseManager:
    """"""

    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.conection = None
        self._init_db()


    def _init_db(self) -> None:
        """"""

        self.conection = sqlite3.connect(self.db_path)

        self.conection.row_factory = sqlite3.Row

        self._create_tables()

        info(f"База данных инициализирована: {self.db_path}")

    def _create_tables(self) -> None:
        """"""

        cursor = self.conection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                url TEXT,
                notes TEXT,
                category TEXT DEFAULT 'Другое',
                favorite INTEGER DEFAULT 0,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS settings (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL
            )
        """)

        self.conection.commit()

        debug("Таблица entries создана/проверена.")


    def add_entry(self, entry: EntryPassword) -> int:
        """"""

        cursor = self.conection.cursor()
        
        cursor.execute("""
            INSERT INTO entries (title, username, password, url, notes, category, favorite)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            entry.title,
            entry.username,
            entry.password,
            entry.url,
            entry.notes,
            entry.category,
            entry.favorite,
        ))

        self.conection.commit()

        entry_id = cursor.lastrowid

        debug(f"Запись '{entry.title}' добавлена (ID: {entry_id})")

        return entry_id
    
    
    def get_all_entries(self) -> List[EntryPassword]:
        """"""

        cursor = self.conection.cursor()

        cursor.execute("SELECT * FROM entryes ORDER BY title")

        rows = cursor.fetchall()

        
        entryes = []
        for row in rows:
            entry = EntryPassword(
                id=row["id"],
                title=row["title"],
                username=row["username"],
                password=row["password"],
                url=row["url"] or "",
                notes=row["notes"] or "",
                category=row["category"],
                favorite=row["favorite"],
                created_at=row["created_at"],
                updated_at=row["updated_at"]
            )

            entryes.append(entry)

        debug(f"Загруджено {len(entryes)} записей.")

        return entryes
    

    def get_entry_by_id(self, entry_id: int) -> Optional[EntryPassword]:
        """"""

        cursor = self.conection.cursor()
        cursor.execute(f"SELECT * FROM entryes WHERE id = ?", (entry_id))
        
        row = cursor.fetchone()

        if not row:
            warning(f"Запись с ID {entry_id} не найдена")
            return None
        
        return EntryPassword(
            id=row["id"],
            title=row["title"],
            username=row["username"],
            password=row["password"],
            url=row["url"] or "",
            notes=row["notes"] or "",
            category=row["category"],
            favorite=row["favorite"],
            created_at=row["created_at"],
            updated_at=row["updated_at"]
        )
    
    
    def update_entry(self, entry: EntryPassword) -> bool:
        """"""

        cursor = self.conection.cursor()
        cursor.execute("""
            UPDATE entries 
            SET title = ?, username = ?, password = ?, url = ?, notes = ?, 
                category = ?, favorite = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (
            entry.title,
            entry.username,
            entry.password,
            entry.url,
            entry.notes,
            entry.category,
            entry.favorite,
            entry.id,
        ))

        self.conection.commit()

        updated = cursor.rowcount > 0

        if updated:
            debug(f"Запись '{entry.title}' обновлена (ID {entry.id})")
        
        else:
            warning(f"Запись с ID {entry.id} не найдена")

        return updated
    
    
    def delete_entry(self, entry_id: int) -> bool:
        """"""

        cursor = self.conection.cursor()
        cursor.execute("DELETE FROM entries WHERE id = ?", (entry_id))

        self.conection.commit()

        deleted = cursor.rowcount > 0

        if deleted:
            debug(f"Запись с ID {entry_id} уделена")

        else:
            warning(f"Запись с ID {entry_id} не найдена")

        
        return deleted
    

    def delete_all_entries(self) -> int:
        """"""

        cursor = self.conection.cursor()
        cursor.execute("DELETE FROM entries")
        self.conection.commit()

        count = cursor.rowcount
        info(f"Удалено {count} записей")

        return count
    

    