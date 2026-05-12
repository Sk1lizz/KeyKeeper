#

""""""

from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt, Signal
from src.views.ui.main_window import Ui_MainWindow

from src.utils.translator import tr
from src.utils.logger import (
    logger,
    debug,
    info,
    warning,
    error,
    critical
)



class MainWindow(QMainWindow):
    """"""

    lock_vault = Signal()

    def __init__(self, password_controller=None):
        super().__init__()
        self.password_controller = password_controller

        self._setup()
        self._setup_menu()


    def _setup(self) -> None:
        pass


    def _setup_menu(self) -> None:
        pass
