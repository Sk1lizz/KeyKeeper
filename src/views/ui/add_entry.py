from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from src.widgets.password_line_edit import PasswordLineEdit



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 550)
        Dialog.setMaximumSize(QSize(600, 550))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.lbl_main = QLabel(Dialog)
        self.lbl_main.setObjectName(u"lbl_main")
        self.lbl_main.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_main)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.le_password = PasswordLineEdit(Dialog)
        self.le_password.setObjectName(u"le_password")

        self.gridLayout.addWidget(self.le_password, 7, 1, 1, 3)

        self.le_title = QLineEdit(Dialog)
        self.le_title.setObjectName(u"le_title")

        self.gridLayout.addWidget(self.le_title, 1, 1, 1, 3)

        self.lbl_notes = QLabel(Dialog)
        self.lbl_notes.setObjectName(u"lbl_notes")
        self.lbl_notes.setMaximumSize(QSize(16777215, 16777215))
        self.lbl_notes.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lbl_notes, 9, 3, 1, 1)

        self.lbl_username = QLabel(Dialog)
        self.lbl_username.setObjectName(u"lbl_username")
        self.lbl_username.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lbl_username, 3, 1, 1, 3)

        self.le_url = QLineEdit(Dialog)
        self.le_url.setObjectName(u"le_url")

        self.gridLayout.addWidget(self.le_url, 10, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_5, 2, 1, 1, 3)

        self.le_notes = QLineEdit(Dialog)
        self.le_notes.setObjectName(u"le_notes")

        self.gridLayout.addWidget(self.le_notes, 10, 3, 1, 1)

        self.le_username = QLineEdit(Dialog)
        self.le_username.setObjectName(u"le_username")

        self.gridLayout.addWidget(self.le_username, 4, 1, 1, 3)

        self.lbl_url = QLabel(Dialog)
        self.lbl_url.setObjectName(u"lbl_url")
        self.lbl_url.setMaximumSize(QSize(16777215, 16777215))
        self.lbl_url.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lbl_url, 9, 1, 1, 1)

        self.lbl_password = QLabel(Dialog)
        self.lbl_password.setObjectName(u"lbl_password")
        self.lbl_password.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lbl_password, 6, 1, 1, 3)

        self.horizontalSpacer_6 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 9, 2, 2, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_7, 8, 1, 1, 3)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_6, 5, 1, 1, 3)

        self.verticalSpacer_8 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_8, 11, 1, 1, 3)

        self.lbl_title = QLabel(Dialog)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lbl_title, 0, 1, 1, 3)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 0, 13, 1)

        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 0, 4, 13, 1)

        self.cb_category = QComboBox(Dialog)
        self.cb_category.setObjectName(u"cb_category")

        self.gridLayout.addWidget(self.cb_category, 12, 1, 1, 3)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer_4 = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_create = QPushButton(Dialog)
        self.btn_create.setObjectName(u"btn_create")

        self.horizontalLayout.addWidget(self.btn_create)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.btn_cancel = QPushButton(Dialog)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_main.setText("")
        self.lbl_notes.setText("")
        self.lbl_username.setText("")
        self.lbl_url.setText("")
        self.lbl_password.setText("")
        self.lbl_title.setText("")
        self.btn_create.setText("")
        self.btn_cancel.setText("")
    # retranslateUi

