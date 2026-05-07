from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(450, 525)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.lbl_title = QLabel(Dialog)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setStyleSheet(u"font-size: 20pt; font-weight: bold;")
        self.lbl_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_title)

        self.verticalSpacer_3 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_master = QLabel(Dialog)
        self.lbl_master.setObjectName(u"lbl_master")
        self.lbl_master.setStyleSheet(u"")

        self.gridLayout.addWidget(self.lbl_master, 0, 1, 1, 1)

        self.le_password = QLineEdit(Dialog)
        self.le_password.setObjectName(u"le_password")

        self.gridLayout.addWidget(self.le_password, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 2, 1)

        self.horizontalSpacer_2 = QSpacerItem(25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 2, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lbl_confirm = QLabel(Dialog)
        self.lbl_confirm.setObjectName(u"lbl_confirm")
        self.lbl_confirm.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.lbl_confirm, 0, 1, 1, 1)

        self.le_confirm = QLineEdit(Dialog)
        self.le_confirm.setObjectName(u"le_confirm")

        self.gridLayout_2.addWidget(self.le_confirm, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 0, 2, 1)

        self.horizontalSpacer_4 = QSpacerItem(25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 0, 2, 2, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lbl_power = QLabel(Dialog)
        self.lbl_power.setObjectName(u"lbl_power")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.lbl_power.sizePolicy().hasHeightForWidth())
        self.lbl_power.setSizePolicy(sizePolicy)
        self.lbl_power.setStyleSheet(u"\\")

        self.gridLayout_3.addWidget(self.lbl_power, 2, 2, 1, 1)

        self.pb_power = QProgressBar(Dialog)
        self.pb_power.setObjectName(u"pb_power")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(10)
        sizePolicy1.setHeightForWidth(self.pb_power.sizePolicy().hasHeightForWidth())
        self.pb_power.setSizePolicy(sizePolicy1)
        self.pb_power.setValue(0)
        self.pb_power.setTextVisible(False)

        self.gridLayout_3.addWidget(self.pb_power, 3, 2, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_9, 2, 3, 2, 1)

        self.horizontalSpacer_8 = QSpacerItem(25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_8, 2, 0, 2, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 140, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_7 = QSpacerItem(25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.btn_create = QPushButton(Dialog)
        self.btn_create.setObjectName(u"btn_create")

        self.horizontalLayout.addWidget(self.btn_create)

        self.horizontalSpacer_6 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.btn_cancel = QPushButton(Dialog)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.horizontalSpacer_5 = QSpacerItem(25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_5 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_5)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_title.setText("")
        self.lbl_master.setText("")
        self.lbl_confirm.setText("")
        self.lbl_power.setText("")
        self.pb_power.setFormat("")
        self.btn_create.setText("")
        self.btn_cancel.setText("")
    # retranslateUi

