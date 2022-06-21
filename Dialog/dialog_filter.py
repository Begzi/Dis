
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.insert(0, "C:\py\Dis\Dialog")
sys.path.insert(0, "C:\py\Dis\GUI")
import dialog_window_filter
import dialog_filter_IP
import tmp


class ClssDialogFilter(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssDialogFilter, self).__init__(parent)

        self.di = dialog_window_filter.Ui_Dialog()
        self.di.setupUi(self)
        self.tmp = 'asdasdaas'

        model = QtGui.QStandardItemModel()
        qitem = QtGui.QStandardItem("Все")
        model.appendRow(qitem)
        self.di.listSRCIP.setModel(model)
        self.di.listDSTIP.setModel(model)
        self.di.listViewPort.setModel(model)
        self.di.listSRCIP.setEnabled(False)
        self.di.listDSTIP.setEnabled(False)
        self.di.listViewPort.setEnabled(False)

        self.di.addSRCRangeIP.clicked.connect(self.openAddSRC)
        self.di.addDSTRangeIP.clicked.connect(self.openAddDST)
        self.di.addPort.clicked.connect(self.openAddPort)

        self.di.pushCancel.clicked.connect(self.close)

    def openAddSRC(self):

        dialog = dialog_filter_IP.ClssDialogFilterIP(self)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:  # Получаем после закрытия диалогового окна

            self.di.listSRCIP.setEnabled(True)   # Если данные введены корректно, сверху такую првоерку сделать!
            model = self.di.listSRCIP.model()

            if (model.rowCount() == 1 and model.item(0).text() == 'Все'):
                model.removeRow(0)
            pass


    def openAddDST(self):
        self.di.listDSTIP.setEnabled(True)

        dialog = dialog_filter_IP.ClssDialogFilterIP(self)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:  # Получаем после закрытия диалогового окна

            self.di.addDSTRangeIP.setEnabled(True)   # Если данные введены корректно, сверху такую првоерку сделать!
            model = self.di.addDSTRangeIP.model()

            if (model.rowCount() == 1 and model.item(0).text() == 'Все'):
                model.removeRow(0)
            pass

    def openAddPort(self):
        self.di.listViewPort.setEnabled(True)

        dialog = tmp.ClssDialogFilterPort(self)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:  # Получаем после закрытия диалогового окна
            self.di.addPort.setEnabled(True)   # Если данные введены корректно, сверху такую првоерку сделать!
            model = self.di.addPort.model()

            if (model.rowCount() == 1 and model.item(0).text() == 'Все'):
                model.removeRow(0)
            pass

    def btnClosed(self):
        self.accept()