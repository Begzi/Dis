
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


    def chooseSRCAll(self):
        self.di.lineSRCPorts1.setEnabled(False)
        self.di.lineSRCPorts2.setEnabled(False)
        self.di.lineSRCPort.setEnabled(False)

    def chooseSRCPort(self):
        self.di.lineSRCPorts1.setEnabled(False)
        self.di.lineSRCPorts2.setEnabled(False)
        self.di.lineSRCPort.setEnabled(True)

    def chooseSRCPorts(self):
        self.di.lineSRCPorts1.setEnabled(True)
        self.di.lineSRCPorts2.setEnabled(True)
        self.di.lineSRCPort.setEnabled(False)

    def chooseDSTAll(self):
        self.di.lineDSTPorts1.setEnabled(False)
        self.di.lineDSTPorts2.setEnabled(False)
        self.di.lineDSTPort.setEnabled(False)

    def chooseDSTPort(self):
        self.di.lineDSTPorts1.setEnabled(False)
        self.di.lineDSTPorts2.setEnabled(False)
        self.di.lineDSTPort.setEnabled(True)

    def chooseDSTPorts(self):
        self.di.lineDSTPorts1.setEnabled(True)
        self.di.lineDSTPorts2.setEnabled(True)
        self.di.lineDSTPort.setEnabled(False)

    def btnClosed(self):
        self.accept()