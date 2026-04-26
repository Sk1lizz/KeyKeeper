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


    
