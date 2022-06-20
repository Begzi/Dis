
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.insert(0, "C:\py\Dis\GUI")
import dialog_window_vulnar
import sqlite3
from sqlite3 import Error


class ClssDialogChooseVul(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssDialogChooseVul, self).__init__(parent)

        self.di_2 = dialog_window_vulnar.Ui_dialogChooseVulnaribility()
        self.di_2.setupUi(self)
        self.cvss_list = []
        self.cvss_current = 0

        self.setWindowTitle('Выбрать уязвимость')

        try:
            self.conn = sqlite3.connect('db.sqlite3')
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        cur = self.conn.cursor()
        cur.execute('SELECT * FROM report_vulnerability;')
        all_results = cur.fetchall()  # Картежи!
        model = QtGui.QStandardItemModel()
        self.di_2.listView.setModel(model)

        for value in all_results:
            if (value[6] != 0 and value[6] != 'null') or (value[5] != 0 and value[5] != 'null'):
                vul_name = str( value[1])
                vul_id = str( value[0])
                if value[6] != 0 or value[6] != 'null':
                    cur.execute('SELECT * FROM report_cvss3 where "id" = ' + str(value[6]) + ' ;')
                    cvss = cur.fetchone()  # Картежи!
                else:
                    cur.execute('SELECT * FROM report_cvss2 where "id" = ' + str(value[5]) + ' ;')
                    cvss = cur.fetchone()  # Картежи!
                self.cvss_list.append(cvss)
                stroka = vul_id  +')' +vul_name + str(cvss[1])
                qitem = QtGui.QStandardItem(stroka)
                model.appendRow(qitem)
        self.di_2.listView.clicked.connect(self.listChoosen)

    def listChoosen(self, index):
        self.cvss_current = self.cvss_list[index.row()]
        print(self.cvss_current)


    def btnClosed(self):

        self.accept()