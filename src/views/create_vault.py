#

""""""

from PySide6.QtWidgets import QDialog, QLineEdit

from src.views.ui.create_vault import Ui_Dialog

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


class CreateWindow(QDialog):
    """"""

    def __init__(self, auth: Optional[AuthController] = None):
        """"""

        super(CreateWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self._auth = auth


        self._setup()

        self.ui.btn_cancel.clicked.connect(self.close_window)
        self.ui.btn_create.clicked.connect(self.create_vault)
        self.ui.le_confirm.textChanged.connect(self.check_password)
        self.ui.le_password.textChanged.connect(self.check_password)

    def _setup(self) -> None:
        """"""

        #

        name = tr.get("create-vault.name")
        title = tr.get("create-vault.title")
        password_entry = tr.get("create-vault.password-entry")
        wait_password = tr.get("create-vault.wait-password")
        password_confirm = tr.get("create-vault.password-confirm")
        wait_confirm = tr.get("create-vault.wait-confirm")
        power = tr.get("create-vault.text-power")

        button_create = tr.get("create-vault.button.create")
        button_cancel = tr.get("create-vault.button.cancel")


        #

        self.setWindowTitle(name)
        self.ui.lbl_title.setText(title)
        self.ui.lbl_master.setText(password_entry)
        self.ui.lbl_confirm.setText(password_confirm)
        self.ui.le_password.setPlaceholderText(wait_password)
        self.ui.le_confirm.setPlaceholderText(wait_confirm)

        self.ui.lbl_power.setText(power)

        self.ui.btn_create.setText(button_create)
        self.ui.btn_cancel.setText(button_cancel)

        self.ui.btn_create.setEnabled(False)
        self.ui.le_confirm.setEchoMode(QLineEdit.Password)


    def close_window(self) -> None:
        self.reject()


    def create_vault(self) -> None:
        try:
            self._auth.delete_vault()
            info("Удаление существуещего хранилища")
        except:
            pass

        password = self.ui.le_password.text()

        self._auth.create_vault(password)

        self.accept()

    def check_password(self) -> None:
        password = self.ui.le_password.text()
        confirm = self.ui.le_confirm.text()


        if password == confirm and not password.replace(" ", "") == "":
            self.ui.btn_create.setEnabled(True)

        else:
            self.ui.btn_create.setEnabled(False)
