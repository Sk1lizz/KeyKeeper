#

""""""


from PySide6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QPushButton
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QIcon, QCursor


class PasswordLineEdit(QWidget):
    """"""

    textChanged = Signal(str)
    returnPressed = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

        self.line_edit = QLineEdit()
        self.line_edit.setEchoMode(QLineEdit.Password)
        self.line_edit.textChanged.connect(self.textChanged.emit)
        self.line_edit.returnPressed.connect(self.returnPressed.emit)
        layout.addWidget(self.line_edit)


        self.toggle_btn = QPushButton()
        self.toggle_btn.setText("👁")
        self.toggle_btn.setFixedWidth(30)
        self.toggle_btn.setFixedHeight(25)
        self.toggle_btn.setCheckable(True)
        self.toggle_btn.clicked.connect(self._toggle_visibility)
        self.toggle_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        layout.addWidget(self.toggle_btn)


    def _toggle_visibility(self, checked):
        """"""

        if checked:
            self.line_edit.setEchoMode(QLineEdit.Normal)
            self.toggle_btn.setText("🔒")

        else:
            self.line_edit.setEchoMode(QLineEdit.Password)
            self.toggle_btn.setText("👁")


    def text(self) -> str:
        return self.line_edit.text()

    def setText(self, text: str):
        self.line_edit.setText(text)

    def clear(self):
        self.line_edit.clear()

    def setPlaceholderText(self, text: str):
        self.line_edit.setPlaceholderText(text)

    def setEnabled(self, enabled: bool):
        super().setEnabled(enabled)
        self.line_edit.setEnabled(enabled)
        self.toggle_btn.setEnabled(enabled)

    def setReadOnly(self, readonly: bool):
        self.line_edit.setReadOnly(readonly)

    def isReadOnly(self) -> bool:
        return self.line_edit.isReadOnly()

    def setFocus(self):
        self.line_edit.setFocus()

    def echoMode(self):
        self.line_edit.echoMode()

    def setEchoMode(self, mode):
        self.line_edit.setEchoMode(mode)
