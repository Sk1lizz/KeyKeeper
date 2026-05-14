#

""""""

from PySide6.QtWidgets import QHeaderView, QMainWindow
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

        self._start()

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

        _table = [
            f"{tr.get("main-window.table.title")}",
            f"{tr.get("main-window.table.username")}",
            f"{tr.get("main-window.table.password")}",
            f"{tr.get("main-window.table.active")}",
        ]

        #

        self.setMinimumSize(900, 600)

        self.setWindowTitle(name)

        self.ui.le_search.setPlaceholderText(search_text)
        self.ui.btn_add.setText(button_add)
        self.ui.btn_delete.setText(button_delete)
        self.ui.btn_block.setText(button_lock)
        self.ui.btn_block_2.setText(button_lock_full)

        self.ui.lbl_status.setText(status)

        #

        table = self.ui.table
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(
            _table
        )

        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)

    def _setup_menu(self) -> None:
        pass

    def _start(self) -> None:
        """"""

        if self.password_controller is None:
            error(f"Не передан PasswordController!")
            return None

        controller = self.password_controller

        data = controller.get_all_entries()

        for entry in data:
            self.add_entry_to_table(entry.to_dict())

    def add_entry_to_table(self, entry) -> None:
        pass

    def _add_new_entry(self) -> None:
        pass

    def _delete(self, row: int | None) -> None:
        pass

    def _block_app(self) -> None:
        pass

    def _edit_entry(self, row: int) -> None:
        pass

    def _copy_entry(self, row: int) -> None:
        pass
