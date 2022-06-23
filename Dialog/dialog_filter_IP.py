
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.insert(0, "C:\py\Dis\GUI")
import dialog_window_filter_IP


class ClssDialogFilterIP(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssDialogFilterIP, self).__init__(parent)

        self.di = dialog_window_filter_IP.Ui_Dialog()
        self.di.setupUi(self)
        self.setWindowTitle('Добавление адрессов')
        self.di.radioIP.clicked.connect(self.chooseIP)
        self.di.radioMask.clicked.connect(self.chooseMask)
        self.di.radioRange.clicked.connect(self.chooseRange)


        self.di.pushAdd.clicked.connect(self.btnClosed)
        self.di.pushCancel.clicked.connect(self.close)

    def chooseIP(self):
        self.di.lineEdit.setEnabled(True)
        self.di.lineEdit_2.setEnabled(False)
        self.di.lineEdit_3.setEnabled(False)
        self.di.lineEdit_4.setEnabled(False)
        self.di.lineEdit_5.setEnabled(False)

        self.di.lineEdit_2.setText('')
        self.di.lineEdit_3.setText('')
        self.di.lineEdit_4.setText('')
        self.di.lineEdit_5.setText('')

    def chooseMask(self):
        self.di.lineEdit.setEnabled(False)
        self.di.lineEdit_2.setEnabled(True)
        self.di.lineEdit_3.setEnabled(True)
        self.di.lineEdit_4.setEnabled(False)
        self.di.lineEdit_5.setEnabled(False)

        self.di.lineEdit.setText('')
        self.di.lineEdit_4.setText('')
        self.di.lineEdit_5.setText('')

    def chooseRange(self):
        self.di.lineEdit.setEnabled(False)
        self.di.lineEdit_2.setEnabled(False)
        self.di.lineEdit_3.setEnabled(False)
        self.di.lineEdit_4.setEnabled(True)
        self.di.lineEdit_5.setEnabled(True)

        self.di.lineEdit.setText('')
        self.di.lineEdit_2.setText('')
        self.di.lineEdit_3.setText('')

    def btnClosed(self):
        self.accept()