from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTableView,
    QTableWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setMinimumSize(QSize(900, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(
            20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum
        )

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalSpacer_3 = QSpacerItem(
            20, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.verticalSpacer_3)

        self.le_search = QLineEdit(self.centralwidget)
        self.le_search.setObjectName("le_search")

        self.horizontalLayout.addWidget(self.le_search)

        self.verticalSpacer_5 = QSpacerItem(
            15, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.verticalSpacer_5)

        self.btn_add = QPushButton(self.centralwidget)
        self.btn_add.setObjectName("btn_add")
        self.btn_add.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_add)

        self.verticalSpacer_6 = QSpacerItem(
            15, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.verticalSpacer_6)

        self.btn_delete = QPushButton(self.centralwidget)
        self.btn_delete.setObjectName("btn_delete")
        self.btn_delete.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_delete)

        self.verticalSpacer_7 = QSpacerItem(
            15, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.verticalSpacer_7)

        self.btn_block = QPushButton(self.centralwidget)
        self.btn_block.setObjectName("btn_block")
        self.btn_block.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_block)

        self.verticalSpacer_4 = QSpacerItem(
            20, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.verticalSpacer_4)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_8 = QSpacerItem(
            20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum
        )

        self.verticalLayout.addItem(self.verticalSpacer_8)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalSpacer_9 = QSpacerItem(
            20, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.verticalSpacer_9)

        self.table = QTableWidget(self.centralwidget)
        self.table.setObjectName("table")

        self.horizontalLayout_2.addWidget(self.table)

        self.verticalSpacer_10 = QSpacerItem(
            20, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.verticalSpacer_10)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_11 = QSpacerItem(
            20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum
        )

        self.verticalLayout.addItem(self.verticalSpacer_11)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalSpacer_12 = QSpacerItem(
            20, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_3.addItem(self.verticalSpacer_12)

        self.lbl_status = QLabel(self.centralwidget)
        self.lbl_status.setObjectName("lbl_status")

        self.horizontalLayout_3.addWidget(self.lbl_status)

        self.verticalSpacer_14 = QSpacerItem(
            150, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_3.addItem(self.verticalSpacer_14)

        self.btn_block_2 = QPushButton(self.centralwidget)
        self.btn_block_2.setObjectName("btn_block_2")
        self.btn_block_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.btn_block_2)

        self.verticalSpacer_13 = QSpacerItem(
            20, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_3.addItem(self.verticalSpacer_13)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_15 = QSpacerItem(
            20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum
        )

        self.verticalLayout.addItem(self.verticalSpacer_15)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName("menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 900, 23))
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.btn_add.setText("")
        self.btn_delete.setText("")
        self.btn_block.setText("")
        self.lbl_status.setText("")
        self.btn_block_2.setText("")

    # retranslateUi
