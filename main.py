import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import main_window
import dialog_window


class ClssDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssDialog, self).__init__(parent)

        self.di = dialog_window.Ui_DialogGroup()
        self.di.setupUi(self)
        self.val = 0

    def btnClosed(self):
        self.val += 1
        self.accept()


class MyWin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = main_window.Ui_FormMain() # Экземпляр класса Ui_MainWindow, в нем конструктор всего GUI.
        self.ui.setupUi(self)     # Инициализация GUI
        self.dialog = 0

        self.ui.openVul.clicked.connect(self.openDialog1) # Открыть новую форму
        self.ui.groupVal.clicked.connect(self.openDialog) # Открыть новую форму

    def openDialog1(self):
        text = 'asd\nasd'
        for i in range(0, 100):
            text += 'asd\nasd'
        self.ui.textEdit.setText(text)


    def openDialog(self):
        print('check')
        dialog = ClssDialog(self)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            print(dialog.val)

    def resizeEvent(self, *args, **kwargs):
        self.ui.verticalLayout_2.setGeometry(QtCore.QRect(0, 0, self.width(), self.height()))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWin()
    window.show()
    sys.exit(app.exec_())