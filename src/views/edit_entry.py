#

""""""

from PySide6.QtWidgets import QDialog

from src.views.ui.add_edit_entry import Ui_Dialog

from src.utils.translator import tr
from src.utils.logger import logger, debug, info, warning, error, critical


class EntryEdit(QDialog):
    """"""

    def __init__(self, controller=None, id: int = 0):
        super(EntryEdit, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        if id == 0:
            error("Не передан id")
            self._close()

        self._id = id
        self._controller = controller

        self._setup()
        self._connect()

    def _setup(self) -> None:
        """"""

        #

        name = tr.get("edit-entry.name")

        title = tr.get("edit-entry.title.text")
        title_wait = tr.get("edit-entry.title.wait")

        username = tr.get("edit-entry.username.text")
        username_wait = tr.get("edit-entry.username.wait")

        password = tr.get("edit-entry.password.text")
        password_wait = tr.get("edit-entry.password.wait")

        url = tr.get("edit-entry.url.text")
        url_wait = tr.get("edit-entry.url.wait")

        notes = tr.get("edit-entry.notes.text")
        notes_wait = tr.get("edit-entry.notes.wait")

        category_wait = tr.get("edit-entry.category")

        btn_save = tr.get("edit-entry.button.save")
        btn_cancel = tr.get("edit-entry.button.cancel")

        #

        self.setWindowTitle(name)

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

        self.ui.btn_create.setText(btn_save)
        self.ui.btn_cancel.setText(btn_cancel)

        self._add_text()


    def _connect(self) -> None:
        """"""

        self.ui.btn_cancel.clicked.connect(self._close)
        self.ui.btn_create.clicked.connect(self._edit_entry)
        self.ui.le_title.textChanged.connect(self._checker)
        self.ui.le_username.textChanged.connect(self._checker)
        self.ui.le_password.textChanged.connect(self._checker)


    def _close(self):
        """"""

        self.reject()


    def _checker(self) -> bool:
        """"""

        title = False if self.ui.le_title.text().replace(" ", "") == "" else True
        username = False if self.ui.le_username.text().replace(" ", "") == "" else True
        password = False if self.ui.le_password.text().replace(" ", "") == "" else True

        all_filled = title and username and password

        self.ui.btn_create.setEnabled(all_filled)

        return all_filled


    def _edit_entry(self) -> None:
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

        controller.update_entry(
            entry_id=self._id,
            title=title,
            username=username,
            password=password,
            url=url,
            notes=notes,
        )

        self.accept()


    def _add_text(self) -> None:
        data = self._controller.get_entry_by_id(self._id)

        dict_data = data.to_dict()

        title = dict_data["title"]
        username = dict_data["username"]
        password = dict_data["password"]
        url = dict_data["url"]
        notes = dict_data["notes"]

        self.ui.le_title.setText(title)
        self.ui.le_username.setText(username)
        self.ui.le_password.setText(password)
        self.ui.le_url.setText(url)
        self.ui.le_notes.setText(notes)

        main = tr.get("edit-entry.main-title", title=title, id=self._id)
        self.ui.lbl_main.setText(main)

        self._checker()
