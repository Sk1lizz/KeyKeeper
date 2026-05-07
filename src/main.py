#

""""""

from PySide6.QtWidgets import QApplication

from src.views.login_window import LoginWindow
from src.views.create_vault import CreateWindow

from src.controllers.auth_controller import AuthController

from src.utils.logger import (
    logger,
    debug,
    info,
    warning,
    error,
    critical
)

import sys


def main():
    """"""

    app = QApplication(sys.argv)

    auth = AuthController()

    if auth.is_first_run():
        info("Первый запуск - создание хранилища")
        
        window = CreateWindow(auth)

        if not window.exec():
            return
        
        auth.lock_vault()
        
        info("Вход в хранилище после создания")

        window = LoginWindow(auth)

        if not window.exec():
            return

    else:
        info("Вход в хранилище")

        window = LoginWindow(auth)

        if not window.exec():
            return
        
    controller = auth.get_password_controller()


        
    sys.exit(app.exec())

    