# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\py\Dis\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormMain(object):
    def setupUi(self, FormMain):
        FormMain.setObjectName("FormMain")
        FormMain.resize(922, 693)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(FormMain)
        self.verticalLayout_2.setContentsMargins(-1, 50, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(FormMain)
        self.tabWidget.setObjectName("tabWidget")
        self.val = QtWidgets.QWidget()
        self.val.setObjectName("val")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.val)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeViewVul = QtWidgets.QTreeView(self.val)
        self.treeViewVul.setObjectName("treeViewVul")
        self.horizontalLayout.addWidget(self.treeViewVul)
        self.textEdit = QtWidgets.QTextEdit(self.val)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupVal = QtWidgets.QPushButton(self.val)
        self.groupVal.setObjectName("groupVal")
        self.horizontalLayout_2.addWidget(self.groupVal)
        self.openVul = QtWidgets.QPushButton(self.val)
        self.openVul.setObjectName("openVul")
        self.horizontalLayout_2.addWidget(self.openVul)
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.val, "")
        self.firewall = QtWidgets.QWidget()
        self.firewall.setObjectName("firewall")
        self.widget_3 = QtWidgets.QWidget(self.firewall)
        self.widget_3.setGeometry(QtCore.QRect(320, 180, 481, 411))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.nameVul_3 = QtWidgets.QLabel(self.widget_3)
        self.nameVul_3.setObjectName("nameVul_3")
        self.verticalLayout_8.addWidget(self.nameVul_3)
        self.shortDescription_3 = QtWidgets.QLabel(self.widget_3)
        self.shortDescription_3.setObjectName("shortDescription_3")
        self.verticalLayout_8.addWidget(self.shortDescription_3)
        self.shortDescriptionText_3 = QtWidgets.QLabel(self.widget_3)
        self.shortDescriptionText_3.setText("")
        self.shortDescriptionText_3.setObjectName("shortDescriptionText_3")
        self.verticalLayout_8.addWidget(self.shortDescriptionText_3)
        self.description_3 = QtWidgets.QLabel(self.widget_3)
        self.description_3.setObjectName("description_3")
        self.verticalLayout_8.addWidget(self.description_3)
        self.descriptionText_3 = QtWidgets.QLabel(self.widget_3)
        self.descriptionText_3.setObjectName("descriptionText_3")
        self.verticalLayout_8.addWidget(self.descriptionText_3)
        self.solution_3 = QtWidgets.QLabel(self.widget_3)
        self.solution_3.setObjectName("solution_3")
        self.verticalLayout_8.addWidget(self.solution_3)
        self.solutuinText_3 = QtWidgets.QLabel(self.widget_3)
        self.solutuinText_3.setText("")
        self.solutuinText_3.setObjectName("solutuinText_3")
        self.verticalLayout_8.addWidget(self.solutuinText_3)
        self.cvss2_3 = QtWidgets.QLabel(self.widget_3)
        self.cvss2_3.setObjectName("cvss2_3")
        self.verticalLayout_8.addWidget(self.cvss2_3)
        self.cvss2Text_3 = QtWidgets.QLabel(self.widget_3)
        self.cvss2Text_3.setText("")
        self.cvss2Text_3.setObjectName("cvss2Text_3")
        self.verticalLayout_8.addWidget(self.cvss2Text_3)
        self.cvss3_3 = QtWidgets.QLabel(self.widget_3)
        self.cvss3_3.setObjectName("cvss3_3")
        self.verticalLayout_8.addWidget(self.cvss3_3)
        self.cvss3Text_3 = QtWidgets.QLabel(self.widget_3)
        self.cvss3Text_3.setText("")
        self.cvss3Text_3.setObjectName("cvss3Text_3")
        self.verticalLayout_8.addWidget(self.cvss3Text_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.verticalScrollBar_Widget_3 = QtWidgets.QScrollBar(self.widget_3)
        self.verticalScrollBar_Widget_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_Widget_3.setObjectName("verticalScrollBar_Widget_3")
        self.horizontalLayout_4.addWidget(self.verticalScrollBar_Widget_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.firewall, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout_2.addWidget(self.tabWidget)

        self.retranslateUi(FormMain)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FormMain)

    def retranslateUi(self, FormMain):
        _translate = QtCore.QCoreApplication.translate
        FormMain.setWindowTitle(_translate("FormMain", "Form"))
        self.groupVal.setText(_translate("FormMain", "Группировать узлы"))
        self.openVul.setText(_translate("FormMain", "Открыть отчёт сканера"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.val), _translate("FormMain", "Уязвимости"))
        self.nameVul_3.setText(_translate("FormMain", "Название уязвимости"))
        self.shortDescription_3.setText(_translate("FormMain", "Краткое описание:"))
        self.description_3.setText(_translate("FormMain", "Описание"))
        self.descriptionText_3.setText(_translate("FormMain", "layotScretch yWidget надо менять в завимости от текста"))
        self.solution_3.setText(_translate("FormMain", "Решение"))
        self.cvss2_3.setText(_translate("FormMain", "cvss2"))
        self.cvss3_3.setText(_translate("FormMain", "cvss3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.firewall), _translate("FormMain", "Правила МЭ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("FormMain", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("FormMain", "Page"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormMain = QtWidgets.QWidget()
    ui = Ui_FormMain()
    ui.setupUi(FormMain)
    FormMain.show()
    sys.exit(app.exec_())
