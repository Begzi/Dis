# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dis\dialog_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogGroup(object):
    def setupUi(self, DialogGroup):
        DialogGroup.setObjectName("DialogGroup")
        DialogGroup.resize(549, 365)
        self.gridLayout = QtWidgets.QGridLayout(DialogGroup)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(-1, 30, 9, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(DialogGroup)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEditNameGroup = QtWidgets.QLineEdit(DialogGroup)
        self.lineEditNameGroup.setObjectName("lineEditNameGroup")
        self.horizontalLayout_2.addWidget(self.lineEditNameGroup)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogGroup)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(DialogGroup)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.lineEditStartIP = QtWidgets.QLineEdit(DialogGroup)
        self.lineEditStartIP.setObjectName("lineEditStartIP")
        self.horizontalLayout.addWidget(self.lineEditStartIP)
        self.lineEditEndIP = QtWidgets.QLineEdit(DialogGroup)
        self.lineEditEndIP.setEnabled(True)
        self.lineEditEndIP.setObjectName("lineEditEndIP")
        self.horizontalLayout.addWidget(self.lineEditEndIP)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(DialogGroup)
        self.buttonBox.accepted.connect(DialogGroup.accept)
        self.buttonBox.rejected.connect(DialogGroup.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogGroup)

    def retranslateUi(self, DialogGroup):
        _translate = QtCore.QCoreApplication.translate
        DialogGroup.setWindowTitle(_translate("DialogGroup", "Dialog"))
        self.label.setText(_translate("DialogGroup", "Название группы:"))
        self.lineEditNameGroup.setText(_translate("DialogGroup", "DefaultName"))
        self.comboBox.setItemText(0, _translate("DialogGroup", "Диапазон"))
        self.comboBox.setItemText(1, _translate("DialogGroup", "IP/маска сети"))
        self.comboBox.setItemText(2, _translate("DialogGroup", "Выбрать узлы"))
        self.lineEditStartIP.setText(_translate("DialogGroup", "0.0.0.0"))
        self.lineEditEndIP.setText(_translate("DialogGroup", "0.0.0.0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogGroup = QtWidgets.QDialog()
    ui = Ui_DialogGroup()
    ui.setupUi(DialogGroup)
    DialogGroup.show()
    sys.exit(app.exec_())
