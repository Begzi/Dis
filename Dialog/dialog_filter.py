
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.insert(0, "C:\py\Dis\Dialog")
sys.path.insert(0, "C:\py\Dis\GUI")
import dialog_window_filter
import dialog_filter_IP


class ClssDialogFilter(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssDialogFilter, self).__init__(parent)

        self.di = dialog_window_filter.Ui_Dialog()
        self.di.setupUi(self)
        self.tmp = 'asdasdaas'

        self.di.addSRCRangeIP.clicked.connect(self.openAddSRC)
        self.di.addDSTRangeIP.clicked.connect(self.openAddDST)

    def openAddSRC(self):

        dialog = dialog_filter_IP.ClssDialogFilterIP(self)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:  # Получаем после закрытия диалогового окна
            print(dialog.tmp)
            print('yes')

    def openAddDST(self):

        dialog = dialog_filter_IP.ClssDialogFilterIP(self)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:  # Получаем после закрытия диалогового окна
            print(dialog.tmp)
            print('yes')


    def btnClosed(self):
        self.accept()