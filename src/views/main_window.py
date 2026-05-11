#

""""""

from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt, Signal
from src.views.ui.main_window import Ui_MainWindow

from src.utils.translator import tr
from src.utils.logger import logger, debug, info, warning, error, critical


class MainWindow(QMainWindow):
    """"""

    lock_vault = Signal()

    def __init__(self, password_controller=None):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.password_controller = password_controller

        self._setup()
        self._setup_menu()

    def _setup(self) -> None:
        """"""

        #
        name = tr.get("main-window.name")

        self._menu_name = {
            "file": f"{tr.get("main-window.menu.file")}",
            "view": f"{tr.get("main-window.menu.view")}",
            "info": f"{tr.get("main-window.menu.info")}",
        }

        search_text = tr.get("main-window.search")

        button_add = tr.get("main-window.button.add_entry")
        button_delete = tr.get("main-window.button.delete_entry")
        button_lock = tr.get("main-window.button.lock")
        button_lock_full = tr.get("main-window.button.lock_window")

        status = tr.get("main-window.status", count="0")

        self._btn = {
            "copy": f"{tr.get("main-window.button.copy")}",
            "edit": f"{tr.get("main-window.button.edit")}",
            "delete": f"{tr.get("main-window.button.delete")}",
        }

        #

        self.setMinimumSize(900, 600)

        self.setWindowTitle(name)

        self.ui.le_search.setPlaceholderText(search_text)
        self.ui.btn_add.setText(button_add)
        self.ui.btn_delete.setText(button_delete)
        self.ui.btn_block.setText(button_lock)
        self.ui.btn_block_2.setText(button_lock_full)

        self.ui.lbl_status.setText(status)

    def _setup_menu(self) -> None:
        pass
