#

""""""

from PySide6.QtWidgets import QDialog

from src.views.ui.add_entry import Ui_Dialog

from src.utils.translator import tr
from src.utils.logger import logger, debug, info, warning, error, critical


class EntryAdd(QDialog):
    """"""

    def __init__(self, controller=None):
        super(EntryAdd, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self._controller = controller

        self._setup()
        self._connect()


    def _setup(self) -> None:
        """"""

        #

        name = tr.get("add-entry.name")
        main = tr.get("add-entry.main-title")

        title = tr.get("add-entry.title.text")
        title_wait = tr.get("add-entry.title.wait")

        username = tr.get("add-entry.username.text")
        username_wait = tr.get("add-entry.username.wait")

        password = tr.get("add-entry.password.text")
        password_wait = tr.get("add-entry.password.wait")

        url = tr.get("add-entry.url.text")
        url_wait = tr.get("add-entry.url.wait")

        notes = tr.get("add-entry.notes.text")
        notes_wait = tr.get("add-entry.notes.wait")

        category_wait = tr.get("add-entry.category")

        btn_create = tr.get("add-entry.button.create")
        btn_cancel = tr.get("add-entry.button.cancel")

        #

        self.setWindowTitle(name)
        self.ui.lbl_main.setText(main)

        self.ui.lbl_title.setText(title)
        self.ui.le_title.setFocus()
        self.ui.le_title.setPlaceholderText(title_wait)

        self.ui.lbl_username.setText(username)
        self.ui.le_username.setPlaceholderText(username_wait)

        self.ui.lbl_password.setText(password)
        self.ui.le_password.setPlaceholderText(password_wait)

        self.ui.lbl_url.setText(url)
        self.ui.le_url.setPlaceholderText(url_wait)

        self.ui.lbl_notes.setText(notes)
        self.ui.le_notes.setPlaceholderText(notes_wait)

        self.ui.cb_category.setPlaceholderText(category_wait)

        self.ui.btn_create.setText(btn_create)
        self.ui.btn_create.setEnabled(False)
        self.ui.btn_cancel.setText(btn_cancel)


    def _connect(self) -> None:
        """"""

        self.ui.btn_cancel.clicked.connect(self._close)
        self.ui.btn_create.clicked.connect(self._add_entry)
        self.ui.le_title.textChanged.connect(self._checker)
        self.ui.le_username.textChanged.connect(self._checker)
        self.ui.le_password.textChanged.connect(self._checker)


    def _close(self):
        """"""

        self.reject()


    def _add_entry(self) -> None:
        """"""

        if not self._checker():
            warning("Не заполнены необходимые поля.")
            return

        title = self.ui.le_title.text()
        username = self.ui.le_username.text()
        password = self.ui.le_password.text()
        url = self.ui.le_url.text()
        notes = self.ui.le_notes.text()

        controller = self._controller

        controller.add_entry(
            title=title,
            username=username,
            password=password,
            url=url,
            notes=notes,
        )

        self.accept()


    def _checker(self) -> bool:
        """"""

        title = False if self.ui.le_title.text().replace(" ", "") == "" else True
        username = False if self.ui.le_username.text().replace(" ", "") == "" else True
        password = False if self.ui.le_password.text().replace(" ", "") == "" else True

        all_filled = title and username and password


        self.ui.btn_create.setEnabled(all_filled)

        return all_filled
