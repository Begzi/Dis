
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.insert(0, "C:\py\Dis\Dialog")
sys.path.insert(0, "C:\py\Dis\GUI")
import dialog_window_OP
import dialog_op_add
import tmp


class ClssDialogOP(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssDialogOP, self).__init__(parent)

        self.di = dialog_window_OP.Ui_Dialog()
        self.di.setupUi(self)
        self.setWindowTitle('Добавление IT-актива')


    def btnClosed(self):
        self.accept()