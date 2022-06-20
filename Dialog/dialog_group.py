
class ClssDialogGroup(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssDialogGroup, self).__init__(parent)

        self.di = dialog_window_IP.Ui_DialogGroup()
        self.di.setupUi(self)

        self.di.comboBox.view().pressed.connect(self.inputEndIp)

    def inputEndIp(self, index):
        if index.row() != 0:
            self.di.lineEditEndIP.setEnabled(False)
            self.di.lineEditStartIP.setText('0.0.0.0/0')
        else:
            self.di.lineEditEndIP.setEnabled(True)
            self.di.lineEditStartIP.setText('0.0.0.0')

    def btnClosed(self):

        self.accept()