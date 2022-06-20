import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.insert(0, "C:\py\Dis\GUI")
import dialog_window_IP

class ClssDialogGroup(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssDialogGroup, self).__init__(parent)
        self.di = dialog_window_IP.Ui_DialogGroup()
        self.di.setupUi(self)
        self.nodes = []
        self.di.comboBox.view().pressed.connect(self.inputEndIp)
        self.indexClickedAdd = -1
        self.indexClickedDelete = -1
        self.di.nodeAdd.clicked.connect(self.nodeAddtoChosen)
        self.di.nodeDelete.clicked.connect(self.nodeAddfromChosentoAll)
        self.setWindowTitle('Функциональная группировка узлов')

    def setNodes(self, nodes):
        model = QtGui.QStandardItemModel()
        self.di.listNodesAll.setModel(model)

        for node in nodes:
            child = QtGui.QStandardItem(node)
            model.appendRow(child)


        self.di.listNodesAll.clicked.connect(self.allowAdd)
        self.di.listNodesChosen.clicked.connect(self.allowDelete)

    def allowAdd(self, index):
        self.di.nodeAdd.setEnabled(True)
        self.indexClickedAdd = index.row()

    def allowDelete(self, index):
        self.di.nodeDelete.setEnabled(True)
        self.indexClickedDelete = index.row()

    def nodeAddtoChosen(self):

        model_chosen = self.di.listNodesChosen.model()
        if (model_chosen == None):
            model_chosen = QtGui.QStandardItemModel()
            self.di.listNodesChosen.setModel(model_chosen)

        model_nodes = self.di.listNodesAll.model()
        chosen = ((model_nodes.item(self.indexClickedAdd).text()))

        model_chosen.appendRow(QtGui.QStandardItem(chosen))
        model_nodes.removeRows(self.indexClickedAdd, 1)
        self.di.nodeAdd.setEnabled(False)

    def nodeAddfromChosentoAll(self):
        model_nodes = self.di.listNodesAll.model()
        if (model_nodes == None):
            model_nodes = QtGui.QStandardItemModel()
            self.di.listNodesAll.setModel(model_nodes)

        model_chosen = self.di.listNodesChosen.model()
        chosen = ((model_chosen.item(self.indexClickedDelete).text()))

        model_nodes.appendRow(QtGui.QStandardItem(chosen))
        model_chosen.removeRows(self.indexClickedDelete, 1)
        self.di.nodeDelete.setEnabled(False)
    def inputEndIp(self, index):
        if index.row() != 0:
            self.di.lineEditEndIP.setEnabled(False)
            self.di.lineEditStartIP.setText('0.0.0.0/0')
        else:
            self.di.lineEditEndIP.setEnabled(True)
            self.di.lineEditStartIP.setText('0.0.0.0')

    def btnClosed(self):

        self.accept()