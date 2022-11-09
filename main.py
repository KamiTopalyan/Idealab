import sys

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                          QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                         QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                         QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
import DatabaseManager

win = None


class CreateNewEntry(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def changeWindow(self):
        self.win = DisplayDatabase()
        self.win.show()
        self.close()

    def submit(self):
        ID = int(self.textEdit.toPlainText())
        name = self.textEdit_2.toPlainText()
        count = int(self.textEdit_3.toPlainText())
        date = "11/9/2022"
        DatabaseManager.Insert(ID, name, count, date)

    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(764, 532)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(290, 250, 151, 61))
        self.pushButton.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setAutoDefault(False)
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 120, 221, 71))
        self.textEdit_2 = QTextEdit(Form)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(270, 120, 221, 71))
        self.textEdit_3 = QTextEdit(Form)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(510, 120, 221, 71))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 70, 41, 51))
        font1 = QFont()
        font1.setPointSize(30)
        self.label.setFont(font1)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(320, 70, 111, 51))
        self.label_2.setFont(font1)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(570, 70, 111, 51))
        self.label_3.setFont(font1)
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(250, 410, 231, 61))
        self.pushButton_2.setSizeIncrement(QSize(0, 0))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setAutoDefault(False)

        self.pushButton_2.clicked.connect(self.changeWindow)

        self.pushButton.clicked.connect(self.submit)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
        self.show()

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Submit", None))
        self.label.setText(QCoreApplication.translate("Form", u"ID", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Count", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Load Database", None))
    # retranslateUi

class DisplayDatabase(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def changeWindow(self):
        self.cams = CreateNewEntry()
        self.cams.show()
        self.close()

    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(541, 533)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(Form)
        self.tableWidget.setObjectName(u"tableWidget_2")

        self.verticalLayout.addWidget(self.tableWidget)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setAutoDefault(False)

        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

        result = DatabaseManager.getColumn()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(4)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.changeWindow)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Add New Entry", None))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = CreateNewEntry()
    sys.exit(app.exec())
