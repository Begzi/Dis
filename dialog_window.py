# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\py\Dis\dialog_window.ui'
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
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(DialogGroup)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.lineEdit = QtWidgets.QLineEdit(DialogGroup)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(DialogGroup)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(DialogGroup)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit_3 = QtWidgets.QLineEdit(DialogGroup)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogGroup)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.retranslateUi(DialogGroup)
        self.buttonBox.accepted.connect(DialogGroup.accept)
        self.buttonBox.rejected.connect(DialogGroup.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogGroup)

    def retranslateUi(self, DialogGroup):
        _translate = QtCore.QCoreApplication.translate
        DialogGroup.setWindowTitle(_translate("DialogGroup", "Dialog"))
        self.comboBox.setItemText(0, _translate("DialogGroup", "Диапазон"))
        self.comboBox.setItemText(1, _translate("DialogGroup", "IP/маска сети"))
        self.label.setText(_translate("DialogGroup", "Название группы:"))

