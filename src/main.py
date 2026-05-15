#

""""""

from PySide6.QtWidgets import QApplication

from src.views.login_window import LoginWindow
from src.views.create_vault import CreateWindow
from src.views.main_window import MainWindow

from src.controllers.auth_controller import AuthController

from src.utils.logger import logger, debug, info, warning, error, critical

import sys


def main():
    """"""

    app = QApplication(sys.argv)

    auth = AuthController()

    main_class = KeyKeeper(auth)

    if auth.is_first_run():
        result = main_class.create_vault()

        if not result:
            return


    else:
        main_class.login()

    sys.exit(app.exec())

    return


class KeyKeeper:

    _auth = None

    def __init__(self, auth: AuthController):
        self._auth = auth

    def create_vault(self) -> bool:
        info("Первый запуск - создание хранилища")

        window = CreateWindow(self._auth)

        if not window.exec():
            return False

        self._auth.lock_vault()

        info("Вход в хранилище после создания")

        return self.login()

    def login(self) -> bool:
        window = LoginWindow(self._auth)

        if not window.exec():
            return False

        self.main()

        return True

    def main(self) -> None:
        controller = self._auth.get_password_controller()

        window = MainWindow(password_controller=controller)

        window.lock_vault.connect(lambda: self.block(window))

        window.show()

    def block(self, window) -> None:
        try:
            window.close()
            info("Окно закрыто, хранилище заблокировано.")

        except Exception as e:
            critical(f"Окно не удалось закрыть: {e}")

        self._auth.lock_vault()

        self.login()
