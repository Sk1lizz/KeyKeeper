# 

"""  """

import os
from pathlib import Path
from typing import Optional

from src.crypto.crypto import CryptoManager
from src.database.db_manager import DatabaseManager
from src.controllers.password_controller import PasswordController
from src.utils.paths import get_salt_path, get_database_path
from src.utils.logger import (
    logger,
    debug,
    info,
    warning,
    error,
    critical
)

class AuthController:
    """"""

    def __init__(self):
        ""

        self.crypto = CryptoManager()
        self.key: Optional[bytes] = None
        self.password_controller: Optional[PasswordController] = None
        self.salt_path = get_salt_path()
        self.db_path = get_database_path()

    
    def is_first_run(self) -> bool:
        """"""

        return not self.db_path.exists() or not self.salt_path.exists()
    

    def is_unlock(self) -> bool:
        """"""

        return self.key is not None or self.password_controller is not None
    

    def create_vault(self, master_password: str) -> bool:
        """"""

        try:
            salt = self.crypto.generate_salt()

            with open(self.salt_path, "wb") as file:
                file.write(salt)
            info(f"Соль сохранена: {self.salt_path}")

            key = self.crypto.derive_key(password=master_password, salt=salt)
            self.key = key

            db_manager = DatabaseManager(self.db_path)

            self.password_controller = PasswordController(self.db_path, self.key)

            self.password_controller.add_entry(
                title="__system__",
                username="__system__",
                password="__test-password__",
                notes="SYSTEM DONT DELETE",
            )

            db_manager.close()

            info("Хранилище создано")

            return True

        except Exception as e:
            error(f"Ошибка создания хранилища: {e}")

            return False


    def unlock_vault(self, master_password: str) -> bool:
        """"""

        try:
            if not self.salt_path.exists():
                error("Файл соли не найден")
                return False
            
            with open(self.salt_path, "rb") as file:
                salt = file.read()

            key = self.crypto.derive_key(master_password, salt)

            self.password_controller = PasswordController(self.db_path, key)

            password_entry = self.password_controller.get_entry_by_id(1)

            if password_entry is None:
                error("Тестовая запись не найдена")
                return False
            
            _ = password_entry

            self.key = key

            info("Хранилище успешно разблокировано")
            return True

        except Exception as e:
            warning(f"Мастер неверный или хранилище повреждено: {e}")
            self.key = None
            self.password_controller = None
            return False
        
    
    def lock_vault(self) -> None:
        """"""

        if self.password_controller:
            self.password_controller.close()

        self.password_controller = None
        self.key = None

        info("Хранилище заблокировано")

    
    def get_password_controller(self) -> Optional[PasswordController]:
        """"""

        if not self.is_unlock():
            warning("Попытка получения контроллера без разблокировки")
            return None
        
        return self.password_controller
    

    def delete_vault(self) -> bool:
        """"""

        try:
            self.lock_vault()
            
            deleted = False

            if self.db_path.exists():
                os.remove(self.db_path)
                info(f"Удалена база данных: {self.db_path}")
                deleted = True

            if self.salt_path.exists():
                os.remove(self.salt_path)
                info(f"Удалена соль: {self.salt_path}")
                deleted = True

            return deleted
        
        except Exception as e:
            error(f"Ошибка удаления хранилища: {e}")
            return False
        
        