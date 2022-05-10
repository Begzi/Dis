import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import main_window
import dialog_window
import ipaddress
import pandas as pd
import sqlite3
from sqlite3 import Error

class ClssDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssDialog, self).__init__(parent)

        self.di = dialog_window.Ui_DialogGroup()
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


class MyWin(QtWidgets.QMainWindow):


    def __init__(self):
        super().__init__()

        self.ui = main_window.Ui_FormMain() # Экземпляр класса Ui_MainWindow, в нем конструктор всего GUI.
        self.ui.setupUi(self)     # Инициализация GUI
        self.dialog = 0
        self.all_vul = {}
        self.conn = None

        self.ui.openVul.clicked.connect(self.openDialogOpenVul) # Открыть новую форму
        self.ui.groupVal.clicked.connect(self.openDialogGroupVal) # Открыть новую форму

    def openDialogOpenVul(self):

        try:
            self.conn = sqlite3.connect('db.sqlite3')
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        cur = self.conn.cursor()
        # cur.execute(
        #     '''CREATE TABLE tasks (taskid INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, notes TEXT, taskcust INTEGER, FOREIGN KEY(taskcust) REFERENCES customer(custid))''')
        cur.execute('SELECT * FROM report_node;')
        all_results = cur.fetchall()  #Картежи!
        print(all_results)
        for i in all_results:
            print(i[1])
            cur.execute(
                'SELECT * FROM report_group_vulnerability WHERE report_group_vulnerability.node_id = '+ str(i[0]) +';')
            all_results1 = cur.fetchall()
            print(all_results1)
        cur.execute('SELECT * FROM report_group_vulnerability, report_node WHERE report_group_vulnerability.node_id = report_node.id;')
        all_results = cur.fetchall()
        print(all_results)


        vul1 = { 'name': 'Разглашение информации (SWEET32)', 'shortdescription': 'Атака Sweet32 позволяет расшифровать данные HTTPS-соединения, если используется шифр 3DES.',
                 'description': 'Уязвимость позволяет в ходе атаки по принципу "человек посередине" (MITM),',
                 'solution':'Необходимо отключить поддержку шифров 3DES. Если ваша система поддерживает только DES-шифрование, необходимо установить обновление, поддерживающее более надежное шифрование.',
                 'cvss2': 'Базовая оценка: 5 (AV:N/AC:L/Au:N/C:P/I:N/A:N)'}
        vul2 = { 'name': 'Некорректная цепочка сертификатов', 'shortdescription': '-',
                 'description': 'При проверке цепочки доверия сертификата данного сервиса были обнаружены следующие ошибки\n1. Цепочка сертификатов не полная',
                 'solutuin': 'Необходимо установить корректный сертификат для данного сервиса.',
                 'cvss2':'Базовая оценка: 5 (AV:N/AC:L/Au:N/C:P/I:N/A:N)'}
        vul3 = { 'name': 'Разглашение информации', 'shortdescription': 'Уязвимость позволяет атакующему восстановить зашифрованные данные.',
                 'description': 'язвимость существует в алгоритме RC4,',
                 'solution':'еобходимо отключить поддержку RC4 для протоколов SSL3 и TLS1',
                 'cvss2':'Базовая оценка: 5 (AV:N/AC:L/Au:N/C:P/I:N/A:N)'}
        vul4 = { 'name': 'Рекурсия', 'shortdescription': '-',
                 'description': 'DNS-сервер поддерживает рекурсию запросов. При определенных обстоятельствах злоумышленник может вызвать на сервере отказ в обслуживании.',
                 'solution':'Разрешите рекурсию только для доверенных адресов.',
                 'cvss2':'Базовая оценка: 4.3 (AV:N/AC:M/Au:N/C:N/I:N/A:P)'}

        self.all_vul['192.168.88.220'] = {'53-udp/dns':[vul4], '389-tcp/LDAP':[vul3], '443-tcp/HTTP SSL':[vul2]}
        self.all_vul['192.168.88.248'] = {'5061-tcp/ssl': [vul1, vul2, vul3], '443-tcp/HTTP SSL':[vul2]}

        model = QtGui.QStandardItemModel()
        self.ui.treeViewVul.setHeaderHidden(True)
        self.ui.treeViewVul.setModel(model)
        i = 0
        for key in self.all_vul:
            parent = QtGui.QStandardItem(key)
            for name in self.all_vul[key]:
                child = QtGui.QStandardItem(name)
                for vul in self.all_vul[key][name]:
                    child_child = QtGui.QStandardItem(vul['name'])
                    child.appendRow(child_child)
                parent.appendRow(child)
            model.appendRow(parent)

        self.ui.treeViewVul.clicked.connect(self.treeFunction)
        self.ui.groupVal.setEnabled(True)

    def treeFunction(self, index): #4 разных ситуаций нужно описать.

        print(index.parent().parent().row())
        print(index.parent().row())
        print(index.row())


        parent_parent_parent_parent_row=index.parent().parent().parent().parent().row()
        parent_parent_parent_row=index.parent().parent().parent().row()
        parent_parent_row=index.parent().parent().row()
        parent_row=index.parent().row()
        row = index.row()


        item = {}
        if parent_row == -1:
            print('1')
            check_first_lvl_is_group = ''
            i = 0
            for key in self.all_vul:
                if i == row:
                    check_first_lvl_is_group = key
                    break
                i += 1
            try:
                check_first_lvl_is_group = ipaddress.ip_address(check_first_lvl_is_group)
                item = self.firstLvlTree(row)
            except:
                item = self.firstLvlTreeGroup(row)
        elif parent_parent_row == -1:
            print('2')
            check_first_lvl_is_group = ''
            i = 0
            for key in self.all_vul:
                if i == parent_row:
                    check_first_lvl_is_group = key
                    break
                i += 1
            try:
                check_first_lvl_is_group = ipaddress.ip_address(check_first_lvl_is_group)
                item = self.secondLvlTree(row, parent_row)
            except:
                item = self.secondLvlTreeGroup(row, parent_row)
        elif parent_parent_parent_row == -1:
            print('3')
            check_first_lvl_is_group = ''
            i = 0
            for key in self.all_vul:
                if i == parent_parent_row:
                    check_first_lvl_is_group = key
                    break
                i += 1
            try:
                check_first_lvl_is_group = ipaddress.ip_address(check_first_lvl_is_group)
                item = self.thirdLvlTree(row, parent_row, parent_parent_row)
            except:
                item = self.thirdLvlTreeGroup(row, parent_row, parent_parent_row)
        elif parent_parent_parent_parent_row == -1:
            print('4')
            item = self.fourthLvlTreeGroup(row, parent_row, parent_parent_row, parent_parent_parent_row)
        else:
            self.errorMessange('Какая-то ошибка с treeView!')

        text = ''
        for key in item:
            text += str(key) + '\n' + '\t' + str(item[key]) + '\n'
        self.ui.textEdit.setText(text)

    def firstLvlTreeGroup(self, row):
        item = {}
        item['Краткое описание'] = 'Будут записи о группах. Нужн подумать какую информацию выводить'
        return item

    def firstLvlTree(self, row):
        item = {}
        item['Краткое описание'] = 'Будут записи о узлах, количеств уязмиостей и их среднее значение'

        check = pd.DataFrame.from_dict(self.all_vul)
        print(check)
        print('check')
        print(check.columns[0])
        print('check')
        print(check.index[0])
        # print(check['DefaultName']['192.168.88.220'])
        return item

    def secondLvlTreeGroup(self, row, parent_row):
        item ={}
        l = 0
        item = {}
        for group in self.all_vul:
            if l == parent_row:
                item = self.firstLvlTree( row)
            l += 1
        return item

    def secondLvlTree(self, row, parent_row):
        item = {}
        i = 0
        j = 0
        for key in self.all_vul:
            if i == parent_row:
                for name in self.all_vul[key]:
                    if j == row:
                        ip_key = key
                        port_name = name
                        break
                    j += 1
            i += 1
        item['Количество уязвимостей'] = len(self.all_vul[ip_key][port_name])
        print((self.all_vul[ip_key][port_name]))
        item['Краткое описание'] = 'Будут записи о уязвимостяй в порте и названия протокола'
        return item

    def thirdLvlTreeGroup(self, row, parent_row, parent_parent_row):
        item ={}
        l = 0
        item = {}
        for group in self.all_vul:
            if l == parent_parent_row:
                item = self.secondLvlTree( row, parent_row)
            l += 1
        return item

    def thirdLvlTree(self, row, parent_row, parent_parent_row):
        i = 0
        j = 0
        k = 0
        item = {}
        for key in self.all_vul:
            if i == parent_parent_row:
                for name in self.all_vul[key]:
                    if j == parent_row:
                        for vul in self.all_vul[key][name]:
                            if k == row:
                                item = vul
                                break
                            k += 1
                    j += 1

            i+=1

        return item


    def fourthLvlTreeGroup(self, row, parent_row, parent_parent_row, parent_parent_parent_row):
        l = 0
        item = {}
        for group in self.all_vul:
            if l == parent_parent_parent_row:
                item = self.thirdLvlTree(row, parent_row, parent_parent_row)
            l += 1
        return item

    def openDialogGroupVal(self):
        dialog = ClssDialog(self)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:    #Получаем после закрытия диалогового окна
            keys = list(self.all_vul.keys())
            if dialog.di.lineEditNameGroup.text() in keys:
                self.errorMessange('Группа с таким названием есть, выберите другое!')
                return 0
            try:
                model = self.ui.treeViewVul.model()
                x = 0
                all_nodes = []                             #Все узлы созданные при открытии отчёта
                while(model.item(x, 0) != None):
                    try:
                        all_nodes.append(ipaddress.ip_address(model.item(x, 0).text()))
                    except:
                        pass
                    x += 1
                if len(all_nodes) == 0:
                    self.errorMessange('Нет узлов, которые можно группировать')
                    return 0
                need_nodes = []                            #Нужные узлы, которые выбрали в диалоговом окне

                if (dialog.di.comboBox.currentIndex() == 0):
                    start_IP =ipaddress.ip_address(dialog.di.lineEditStartIP.text())
                    end_IP =ipaddress.ip_address(dialog.di.lineEditEndIP.text())

                    for i in range(0, len(all_nodes)):
                        if start_IP < all_nodes[i] < end_IP:
                            need_nodes.append(all_nodes[i])

                else:
                    subnet = ipaddress.ip_network(dialog.di.lineEditStartIP.text())
                    for i in range(0, len(all_nodes)):
                        if all_nodes[i] in subnet:
                            need_nodes.append(all_nodes[i])
                if len(need_nodes) == 0:
                    self.errorMessange('Таких узлов нет, либо эти узлы в группе')
                    return 0
                tmp_vul = {}
                tmp_nodes = {}
                for i in range(0,  len(need_nodes)):      #Собираем в группу узлы

                    for key in self.all_vul:
                        if key == str(need_nodes[i]):
                            tmp_nodes[key] = self.all_vul[key]

                keys = tmp_nodes.keys()

                for key in self.all_vul:  #Сохраняем не выбранные узлы
                    if key in list(keys):
                        pass
                    else:
                        tmp_vul[key] = self.all_vul[key]

                tmp_vul[dialog.di.lineEditNameGroup.text()] = tmp_nodes
                self.all_vul = tmp_vul


                model = QtGui.QStandardItemModel()
                self.ui.treeViewVul.setHeaderHidden(True)
                self.ui.treeViewVul.setModel(model)
                i = 0
                for key in self.all_vul:
                    # if ipaddress.ip_address(key)
                    try:
                        ipaddress.ip_address(key)

                        parent = QtGui.QStandardItem(key)
                        for name in self.all_vul[key]:
                            child = QtGui.QStandardItem(name)
                            for vul in self.all_vul[key][name]:
                                child_child = QtGui.QStandardItem(vul['name'])
                                child.appendRow(child_child)
                            parent.appendRow(child)
                        model.appendRow(parent)
                    except:
                        parent = QtGui.QStandardItem(key)
                        for node in self.all_vul[key]:
                            child = QtGui.QStandardItem(node)
                            for name in self.all_vul[key][node]:
                                child_child = QtGui.QStandardItem(name)
                                for vul in self.all_vul[key][node][name]:
                                    child_child_child = QtGui.QStandardItem(vul['name'])
                                    child_child.appendRow(child_child_child)
                                child.appendRow(child_child)
                            parent.appendRow(child)
                        model.appendRow(parent)
            except:
                self.errorMessange('Вы ввели не корректные данные')


    def errorMessange(self, text):
        error = QtWidgets.QMessageBox()
        error.setWindowTitle("Ошибка")
        error.setText(text)
        error.setIcon(QtWidgets.QMessageBox.Warning)
        error.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

        error.exec_()
    def resizeEvent(self, *args, **kwargs):
        self.ui.verticalLayout_2.setGeometry(QtCore.QRect(0, 0, self.width(), self.height()))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWin()
    window.show()
    sys.exit(app.exec_())