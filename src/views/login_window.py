#

""""""

from PySide6.QtWidgets import QDialog

from src.views.ui.login import Ui_Dialog
from src.views.create_vault import CreateWindow

from typing import Optional

from src.controllers.auth_controller import AuthController
from src.utils.translator import tr
from src.utils.logger import (
    logger,
    debug,
    info,
    warning,
    error,
    critical
)


class LoginWindow(QDialog):
    """"""

    def __init__(self, auth: Optional[AuthController] = None):
        """"""

        super(LoginWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self._auth = auth

        self._setup()

        self.ui.btn_cancel.clicked.connect(self.close_window)
        self.ui.btn_unlock.clicked.connect(self.unlock)
        self.ui.btn_create.clicked.connect(self.create_db)

    def _setup(self) -> None:
        """"""

        #

        name = tr.get("login-window.name")
        title = tr.get("login-window.title")
        subtitle = tr.get("login-window.subtitle")
        wait_text= tr.get("login-window.wait-text")
        button_unlock = tr.get("login-window.button.unlock")
        button_cancel = tr.get("login-window.button.cancel")
        button_create = tr.get("login-window.button.new-vault")

        debug(f"Успешное получение всех данных из языкового файла: {tr.get_current_language()}")


        #

        self.setWindowTitle(name)
        self.ui.lbl_title.setText(title)
        self.ui.lbl_subtitle.setText(subtitle)
        self.ui.le_password.setPlaceholderText(wait_text)
        self.ui.btn_unlock.setText(button_unlock)
        self.ui.btn_cancel.setText(button_cancel)
        self.ui.btn_create.setText(button_create)

        self.setFixedSize(450, 350)

        debug("Настройки окна успешно уставнолены")



    def close_window(self) -> None:
        print("close_window() called - rejecting")
        self.reject()


    def unlock(self) -> None:
        """"""

        auth = self._auth
        password = self.ui.le_password.text()

        result = auth.unlock_vault(password)

        print(result)

        if result:
            info("Успешный вход в хранилише")
            self.accept()

        else:
            warning("Попытка входа в хранилище с неверным паролем")

            self.ui.le_password.clear()
            self.ui.le_password.setFocus()

    def create_db(self) -> None:
        info("Создание нового хранилища")

        window = CreateWindow(self._auth)

        if not window.exec():
            self.close_window()

        else:
            self._auth.lock_vault()
            self.ui.le_password.clear()
            self.ui.le_password.setFocus()
