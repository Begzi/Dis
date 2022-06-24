
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.insert(0, "C:\py\Dis\Dialog")
sys.path.insert(0, "C:\py\Dis\GUI")
import dialog_window_OP_add


class ClssDialogOPAdd(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssDialogOPAdd, self).__init__(parent)

        self.di = dialog_window_OP_add.Ui_Dialog()
        self.di.setupUi(self)
        self.setWindowTitle('Добавление IT-актива')

        self.di.radioSRCALL.clicked.connect(self.chooseSRCAll)
        self.di.radioSRCPort.clicked.connect(self.chooseSRCPort)
        self.di.radioSRCPorts.clicked.connect(self.chooseSRCPorts)

        self.di.radioDSTALL.clicked.connect(self.chooseDSTAll)
        self.di.radioDSTPort.clicked.connect(self.chooseDSTPort)
        self.di.radioDSTPorts.clicked.connect(self.chooseDSTPorts)

        self.di.pushCancel.clicked.connect(self.close)
        self.di.pushAdd.clicked.connect(self.btnClosed)

    def chooseSRCAll(self):
        self.di.lineSRCPorts1.setEnabled(False)
        self.di.lineSRCPorts2.setEnabled(False)
        self.di.lineSRCPort.setEnabled(False)

        self.di.lineSRCPorts1.setText('')
        self.di.lineSRCPorts2.setText('')
        self.di.lineSRCPort.setText('')

    def chooseSRCPort(self):
        self.di.lineSRCPorts1.setEnabled(False)
        self.di.lineSRCPorts2.setEnabled(False)
        self.di.lineSRCPort.setEnabled(True)

        self.di.lineSRCPorts1.setText('')
        self.di.lineSRCPorts2.setText('')

    def chooseSRCPorts(self):
        self.di.lineSRCPorts1.setEnabled(True)
        self.di.lineSRCPorts2.setEnabled(True)
        self.di.lineSRCPort.setEnabled(False)

        self.di.lineSRCPort.setText('')

    def chooseDSTAll(self):
        self.di.lineDSTPorts1.setEnabled(False)
        self.di.lineDSTPorts2.setEnabled(False)
        self.di.lineDSTPort.setEnabled(False)

        self.di.lineDSTPorts1.setText('')
        self.di.lineDSTPorts2.setText('')
        self.di.lineDSTPort.setText('')

    def chooseDSTPort(self):
        self.di.lineDSTPorts1.setEnabled(False)
        self.di.lineDSTPorts2.setEnabled(False)
        self.di.lineDSTPort.setEnabled(True)

        self.di.lineDSTPorts1.setText('')
        self.di.lineDSTPorts2.setText('')

    def chooseDSTPorts(self):
        self.di.lineDSTPorts1.setEnabled(True)
        self.di.lineDSTPorts2.setEnabled(True)
        self.di.lineDSTPort.setEnabled(False)

        self.di.lineDSTPort.setText('')

    def btnClosed(self):
        self.accept()