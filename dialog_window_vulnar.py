# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dis\dialog_window_vulnaer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialogChooseVulnaribility(object):
    def setupUi(self, dialogChooseVulnaribility):
        dialogChooseVulnaribility.setObjectName("dialogChooseVulnaribility")
        dialogChooseVulnaribility.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(dialogChooseVulnaribility)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listView = QtWidgets.QListView(dialogChooseVulnaribility)
        self.listView.setObjectName("listView")
        self.horizontalLayout.addWidget(self.listView)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialogChooseVulnaribility)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)

        self.retranslateUi(dialogChooseVulnaribility)
        self.buttonBox.accepted.connect(dialogChooseVulnaribility.accept)
        self.buttonBox.rejected.connect(dialogChooseVulnaribility.reject)
        QtCore.QMetaObject.connectSlotsByName(dialogChooseVulnaribility)

    def retranslateUi(self, dialogChooseVulnaribility):
        _translate = QtCore.QCoreApplication.translate
        dialogChooseVulnaribility.setWindowTitle(_translate("dialogChooseVulnaribility", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialogChooseVulnaribility = QtWidgets.QDialog()
    ui = Ui_dialogChooseVulnaribility()
    ui.setupUi(dialogChooseVulnaribility)
    dialogChooseVulnaribility.show()
    sys.exit(app.exec_())