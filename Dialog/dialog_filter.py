
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.insert(0, "C:\py\Dis\Dialog")
sys.path.insert(0, "C:\py\Dis\GUI")
import dialog_window_filter
import dialog_filter_IP
import tmp
import ipaddress, copy

class ClssDialogFilter(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssDialogFilter, self).__init__(parent)

        self.di = dialog_window_filter.Ui_Dialog()
        self.di.setupUi(self)
        self.setWindowTitle('Добавление правил')
        self.srcIpAddress=''
        self.dstIpAddress=''
        self.port=''

        modelSRC = QtGui.QStandardItemModel()
        modelDST = QtGui.QStandardItemModel()
        modelPORT = QtGui.QStandardItemModel()
        qitem = QtGui.QStandardItem("Все")
        modelSRC.appendRow(qitem)
        qitem = QtGui.QStandardItem("Все")
        modelDST.appendRow(qitem)
        qitem = QtGui.QStandardItem("Все")
        modelPORT.appendRow(qitem)
        self.di.listSRCIP.setModel(modelSRC)
        self.di.listDSTIP.setModel(modelDST)
        self.di.listViewPort.setModel(modelPORT)
        self.di.listSRCIP.setEnabled(False)
        self.di.listDSTIP.setEnabled(False)
        self.di.listViewPort.setEnabled(False)

        self.di.addSRCRangeIP.clicked.connect(self.openAddSRC)
        self.di.addDSTRangeIP.clicked.connect(self.openAddDST)
        self.di.addPort.clicked.connect(self.openAddPort)

        self.di.pushCancel.clicked.connect(self.close)
        self.di.pushAdd.clicked.connect(self.btnClosed)

    def openAddSRC(self):

        dialog = dialog_filter_IP.ClssDialogFilterIP(self)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:  # Получаем после закрытия диалогового окна
            if dialog.di.radioIP.isChecked():
                try:
                    self.srcIpAddress = str(ipaddress.ip_address(dialog.di.lineEdit.text()))
                except:
                    self.errorMessange('Не корректно ведён IP-адрес')
                    return 0
            elif dialog.di.radioRange.isChecked():
                try:
                    start_IP = ipaddress.ip_address(dialog.di.lineEdit_4.text())
                    end_IP = ipaddress.ip_address(dialog.di.lineEdit_5.text())
                    self.srcIpAddress = str(start_IP) + '-' + str(end_IP)
                except:
                    self.errorMessange('Не корректно ведён диапозон IP-адресов')
                    return 0

            model = self.di.listSRCIP.model()

            if (model.rowCount() == 1 and model.item(0).text() == 'Все'):
                self.di.listSRCIP.setEnabled(True)
                model.removeRow(0)
                model = QtGui.QStandardItemModel()
                self.di.listSRCIP.setModel(model)
                self.di.listSRCIP.clicked.connect(self.enabledSrcDelete)
            item = QtGui.QStandardItem(self.srcIpAddress)
            model.appendRow(item)


    def openAddDST(self):

        dialog = dialog_filter_IP.ClssDialogFilterIP(self)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:  # Получаем после закрытия диалогового окна

            if dialog.di.radioIP.isChecked():
                try:
                    self.dstIpAddress = str(ipaddress.ip_address(dialog.di.lineEdit.text()))
                except:
                    self.errorMessange('Не корректно ведён IP-адрес')
                    return 0
            elif dialog.di.radioRange.isChecked():
                try:
                    start_IP = ipaddress.ip_address(dialog.di.lineEdit_4.text())
                    end_IP = ipaddress.ip_address(dialog.di.lineEdit_5.text())
                    self.dstIpAddress = str(start_IP) + '-' + str(end_IP)
                except:
                    self.errorMessange('Не корректно ведён диапозон IP-адресов')
                    return 0

            model = self.di.listDSTIP.model()

            if (model.rowCount() == 1 and model.item(0).text() == 'Все'):
                self.di.listDSTIP.setEnabled(True)
                model.removeRow(0)
                model = QtGui.QStandardItemModel()
                self.di.listDSTIP.setModel(model)
                self.di.listDSTIP.clicked.connect(self.enabledDstDelete)

            item = QtGui.QStandardItem(self.dstIpAddress)
            model.appendRow(item)

    def openAddPort(self):

        dialog = tmp.ClssDialogFilterPort(self)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:  # Получаем после закрытия диалогового окна

            if dialog.di.radioTCP.isChecked():
                protocol = 'TCP'
            else:
                protocol = 'UDP'

            if dialog.di.radioSRCALL.isChecked():
                srcProts = 'Все'
            elif dialog.di.radioSRCPort.isChecked():
                try:
                    srcProts = str(int(dialog.di.lineSRCPort.text()))
                except:
                    self.errorMessange('Порт источника введён не корректно, разрешается только цифры')
            elif dialog.di.radioSRCPorts.isChecked():
                try:
                    srcProts = str(int(dialog.di.lineSRCPorts1.text())) + '-' + str(int(dialog.di.lineSRCPorts2.text()))
                except:
                    self.errorMessange('Порты источника введены не корректно, разрешается только цифры')

            if dialog.di.radioDSTALL.isChecked():
                dstProts = 'Все'
            elif dialog.di.radioDSTPort.isChecked():
                try:
                    dstProts = str(int(dialog.di.lineDSTPort.text()))
                except:
                    self.errorMessange('Порт источника введён не корректно, разрешается только цифры')
            elif dialog.di.radioDSTPorts.isChecked():
                try:
                    dstProts = str(int(dialog.di.lineDSTPorts1.text())) + '-' + str(int(dialog.di.lineDSTPorts2.text()))
                except:
                    self.errorMessange('Порты источника введены не корректно, разрешается только цифры')


            self.port = "от " + srcProts + ' до ' + dstProts + ' :' + protocol

            model = self.di.listViewPort.model()

            if (model.rowCount() == 1 and model.item(0).text() == 'Все'):
                self.di.listViewPort.setEnabled(True)
                model.removeRow(0)
                model = QtGui.QStandardItemModel()
                self.di.listViewPort.setModel(model)
                self.di.listViewPort.clicked.connect(self.enabledPortDelete)

            item = QtGui.QStandardItem(self.port)
            model.appendRow(item)

    def enabledPortDelete(self):
        self.di.deletePort.setEnabled(True)
    def enabledSrcDelete(self):
        self.di.deleteSRCRangeIP.setEnabled(True)
    def enabledDstDelete(self):
        self.di.deleteDSTRangeIP.setEnabled(True)

    def btnClosed(self):
        self.accept()

    def errorMessange(self, text):
        error = QtWidgets.QMessageBox()
        error.setWindowTitle("Ошибка")
        error.setText(text)
        error.setIcon(QtWidgets.QMessageBox.Warning)
        error.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

        error.exec_()