#

""""""

from PySide6.QtWidgets import QDialog

from src.views.ui.login import Ui_Dialog
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

    def __init__(self, auth: ):
        """"""

        super(LoginWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self._setup_ui()

        self.ui.btn_cancel.clicked.connect(self.close_window)


    def _setup_ui(self) -> None:
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
        """"""

        debug(f"Окно закрыто")
        self.close()


    def unlock(self) -> None:
        """"""

        pass


    def check_first_run(self) -> bool:
        """"""

        pass