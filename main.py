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

        self.ui = main_window.Ui_FormMain()  # Экземпляр класса Ui_MainWindow, в нем конструктор всего GUI.
        self.ui.setupUi(self)  # Инициализация GUI
        self.dialog = 0
        self.all_vul = {}
        self.conn = None
        self.textEdit = ''
        self.ui.saveTextEdit.setHidden(True)
        self.ui.cancelTextEdit.setHidden(True)

        self.ui.openVul.clicked.connect(self.openDialogOpenVul)
        self.ui.groupVal.clicked.connect(self.openDialogGroupVal)  # Открыть новую форму
        self.ui.editTextEdit.clicked.connect(self.editText)  # Открыть новую форму
        self.ui.saveTextEdit.clicked.connect(self.saveEditText)  # Открыть новую форму
        self.ui.cancelTextEdit.clicked.connect(self.cancelEditText)  # Открыть новую форму

    def openDialogOpenVul(self):
        if not self.ui.cancelTextEdit.isHidden():
            self.cancelEditText()
        self.all_vul = {}
        try:
            self.conn = sqlite3.connect('db.sqlite3')
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        cur = self.conn.cursor()
        # cur.execute(
        #     '''CREATE TABLE tasks (taskid INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, notes TEXT, taskcust INTEGER, FOREIGN KEY(taskcust) REFERENCES customer(custid))''')
        cur.execute('SELECT * FROM report_node;')
        all_results = cur.fetchall()  # Картежи!
        for node in all_results:  # Потом как нибудь проверку на то что есть ли данные с бд. Если данные плохие то вызвать функцию ошибки

            cur.execute(
                'SELECT * FROM report_group_vulnerability WHERE report_group_vulnerability.node_id = ' + str(
                    node[0]) + ';')
            all_results_port = cur.fetchall()
            tmp_port_dict = {}
            for port in all_results_port:
                cur.execute(
                    'SELECT * FROM report_group_vulnerability_vulnerability WHERE report_group_vulnerability_vulnerability.group_vulnerability_id = ' + str(
                        port[0]) + ';')
                all_results_group_vul = cur.fetchall()
                tmp_all_vul = []
                for group_vul in all_results_group_vul:
                    cur.execute(
                        'SELECT * FROM report_vulnerability WHERE report_vulnerability.id = ' + str(
                            group_vul[2]) + ';')
                    result_vul = cur.fetchone()
                    cur.execute(
                        'SELECT * FROM report_cvss2 WHERE report_cvss2.id = ' + str(
                            result_vul[5]) + ';')
                    cvss2 = cur.fetchone()
                    cur.execute(
                        'SELECT * FROM report_cvss3 WHERE report_cvss3.id = ' + str(
                            result_vul[6]) + ';')
                    cvss3 = cur.fetchone()
                    vulnerubility = {'name': result_vul[1], 'shortdescription': result_vul[2],
                                     'description': result_vul[3],
                                     'solution': result_vul[4], 'cvss2': cvss2[1], 'cvss3': cvss3[1]}
                    tmp_all_vul.append(vulnerubility)

                tmp_port_dict[str(port[1]) + '-' + str(port[2]) + '/' + str(port[3])] = tmp_all_vul
            self.all_vul[node[1]] = tmp_port_dict

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
        self.ui.editTextEdit.setEnabled(True)

    def treeFunction(self, index):  # 4 разных ситуаций нужно описать.

        print(index.parent().parent().row())
        print(index.parent().row())
        print(index.row())

        parent_parent_parent_parent_row = index.parent().parent().parent().parent().row()
        parent_parent_parent_row = index.parent().parent().parent().row()
        parent_parent_row = index.parent().parent().row()
        parent_row = index.parent().row()
        row = index.row()

        if not self.ui.cancelTextEdit.isHidden():
            self.textEdit = ''
            self.cancelEditText()
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
                item = self.firstLvlTree(row, self.all_vul)
            except:
                item = self.firstLvlTreeGroup(row, self.all_vul)
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
                item = self.secondLvlTree(row, parent_row, self.all_vul)
            except:
                item = self.secondLvlTreeGroup(row, parent_row, self.all_vul)
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
                item = self.thirdLvlTree(row, parent_row, parent_parent_row, self.all_vul)
            except:
                item = self.thirdLvlTreeGroup(row, parent_row, parent_parent_row, self.all_vul)
        elif parent_parent_parent_parent_row == -1:
            print('4')
            item = self.fourthLvlTreeGroup(row, parent_row, parent_parent_row, parent_parent_parent_row, self.all_vul)
        else:
            self.errorMessange('Какая-то ошибка с treeView!')

        text = ''
        for key in item:
            text += str(key) + '\n' + '\t' + str(item[key]) + '\n'
        self.ui.textEdit.setText(text)

    def firstLvlTreeGroup(self, row, all_vul):
        item = {}
        item['Краткое описание'] = 'Будут записи о группах. Нужн подумать какую информацию выводить'
        return item

    def firstLvlTree(self, row, all_vul):

        item = {}
        item['Краткое описание'] = 'Будут записи о узлах, количеств уязмиостей и их среднее значение'

        check = pd.DataFrame.from_dict(self.all_vul)
        print(check)
        print('check')
        print(check.columns[0])
        print('check')
        print(check.index[0])
        return item

    def secondLvlTreeGroup(self, row, parent_row, all_vul):
        l = 0
        item = {}
        for group in self.all_vul:
            if l == parent_row:
                item = self.firstLvlTree(row, all_vul)
            l += 1
        return item

    def secondLvlTree(self, row, parent_row, all_vul):
        item = {}
        i = 0
        j = 0
        for key in all_vul:
            if i == parent_row:
                for name in all_vul[key]:
                    if j == row:
                        ip_key = key
                        port_name = name
                        break
                    j += 1
            i += 1
        item['Количество уязвимостей'] = len(all_vul[ip_key][port_name])
        print((all_vul[ip_key][port_name]))
        item['Краткое описание'] = 'Будут записи о уязвимостяй в порте и названия протокола'
        return item

    def thirdLvlTreeGroup(self, row, parent_row, parent_parent_row, all_vul):
        l = 0
        item = {}
        for group in all_vul:
            if l == parent_parent_row:
                item = self.secondLvlTree(row, parent_row, all_vul[group])
            l += 1
        return item

    def thirdLvlTree(self, row, parent_row, parent_parent_row, all_vul):
        i = 0
        j = 0
        k = 0
        item = {}
        for key in all_vul:
            if i == parent_parent_row:
                for name in all_vul[key]:
                    if j == parent_row:
                        for vul in all_vul[key][name]:
                            if k == row:
                                item = vul
                                break
                            k += 1
                    j += 1

            i += 1

        return item

    def fourthLvlTreeGroup(self, row, parent_row, parent_parent_row, parent_parent_parent_row, all_vul):
        l = 0
        item = {}
        for group in all_vul:
            print(group)
            if l == parent_parent_parent_row:
                item = self.thirdLvlTree(row, parent_row, parent_parent_row, all_vul[group])
            l += 1
        return item

    def openDialogGroupVal(self):
        dialog = ClssDialog(self)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:  # Получаем после закрытия диалогового окна
            keys = list(self.all_vul.keys())
            if dialog.di.lineEditNameGroup.text() in keys:
                self.errorMessange('Группа с таким названием есть, выберите другое!')
                return 0
            try:
                model = self.ui.treeViewVul.model()
                x = 0
                all_nodes = []  # Все узлы созданные при открытии отчёта
                while (model.item(x, 0) != None):
                    try:
                        all_nodes.append(ipaddress.ip_address(model.item(x, 0).text()))
                    except:
                        pass
                    x += 1
                if len(all_nodes) == 0:
                    self.errorMessange('Нет узлов, которые можно группировать')
                    return 0
                need_nodes = []  # Нужные узлы, которые выбрали в диалоговом окне

                if (dialog.di.comboBox.currentIndex() == 0):
                    start_IP = ipaddress.ip_address(dialog.di.lineEditStartIP.text())
                    end_IP = ipaddress.ip_address(dialog.di.lineEditEndIP.text())

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
                for i in range(0, len(need_nodes)):  # Собираем в группу узлы

                    for key in self.all_vul:
                        if key == str(need_nodes[i]):
                            tmp_nodes[key] = self.all_vul[key]

                keys = tmp_nodes.keys()

                for key in self.all_vul:  # Сохраняем не выбранные узлы
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

    def editText(self):
        self.textEdit = self.ui.textEdit.toPlainText()
        self.ui.textEdit.setReadOnly(False)
        text = self.ui.textEdit.toPlainText()
        num_n_1 = num_t_1 = sum_num = 0
        start_ignore_str = '<<<<<<<<<<\n\t'
        end_ignore_str = '>>>>>>>>>\n\t'
        while (num_n_1 != -1) and (num_t_1 != -1):   #3 подхода чтобы убрать записи
            num_n_1 = text[sum_num :].find('\n')
            sum_num += num_n_1 + 1
            num_t_1 = text[sum_num :].find('\t')
            sum_num += num_t_1 + 1
            text = text[:sum_num] + start_ignore_str + text[sum_num:]
            sum_num += len(start_ignore_str) + 1
            num_n_2 = text[sum_num :].find('\n')
            sum_num += num_n_2 + 1
            text = text[:sum_num] + end_ignore_str + text[sum_num:]
            sum_num += len(end_ignore_str) + 1
        self.ui.textEdit.setText(text)
        self.ui.saveTextEdit.setHidden(False)
        self.ui.cancelTextEdit.setHidden(False)
        self.ui.editTextEdit.setHidden(True)

    def cancelEditText(self):
        print(self.ui.treeViewVul.currentIndex().row())
        if self.textEdit != '':
            self.ui.textEdit.setText(self.textEdit)
        self.ui.saveTextEdit.setHidden(True)
        self.ui.cancelTextEdit.setHidden(True)
        self.ui.editTextEdit.setHidden(False)
        self.ui.textEdit.setReadOnly(True)

    def saveEditText(self):
        parent_parent_parent_parent_row = self.ui.treeViewVul.currentIndex().parent().parent().parent().parent().row()
        parent_parent_parent_row = self.ui.treeViewVul.currentIndex().parent().parent().parent().row()
        parent_parent_row = self.ui.treeViewVul.currentIndex().parent().parent().row()
        parent_row = self.ui.treeViewVul.currentIndex().parent().row()
        row = self.ui.treeViewVul.currentIndex().row()


        text = self.ui.textEdit.toPlainText()

        vul = []
        num_1 = num_2 = 0
        print('check')
        while num_1 != -1 and num_2 != -1: # На одну больше чем есть!
            num_1 = text.find('<<<<<<<<')
            num_2 = text.find('>>>>>>>>')
            name = text[num_1 + 10: num_2]
            text = text[num_2 + 11:]
            print(name)
            vul.append(name)

        try:
            self.conn = sqlite3.connect('db.sqlite3')
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        cur = self.conn.cursor()
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
                item = self.firstLvlTree(row, self.all_vul)
                #Тут писать то что изменили, ввод в БД данные
            except:
                item = self.firstLvlTreeGroup(row, self.all_vul)
                #Тут писать то что изменили, ввод в БД данные
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
                item = self.secondLvlTree(row, parent_row, self.all_vul)
                #Тут писать то что изменили, ввод в БД данные
            except:
                item = self.secondLvlTreeGroup(row, parent_row, self.all_vul)
                #Тут писать то что изменили, ввод в БД данные
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
                item = self.thirdLvlTree(row, parent_row, parent_parent_row, self.all_vul)
                #Тут писать то что изменили, ввод в БД данные

                print('checl' + str(vul[0]))
                # cur.execute(
                #     '''CREATE TABLE tasks (taskid INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, notes TEXT, taskcust INTEGER, FOREIGN KEY(taskcust) REFERENCES customer(custid))''')
                cur.execute('Update report_vulnerability set "name" = '+str(vul[0])+' where "name" = '+str(vul[0])+';')
                cur.commit()

            except:
                item = self.thirdLvlTreeGroup(row, parent_row, parent_parent_row, self.all_vul)
                #Тут писать то что изменили, ввод в БД данные
        elif parent_parent_parent_parent_row == -1:
            print('4')
            item = self.fourthLvlTreeGroup(row, parent_row, parent_parent_row, parent_parent_parent_row, self.all_vul)
                #Тут писать то что изменили, ввод в БД данные
        else:
            self.errorMessange('Какая-то ошибка с treeView!')


        self.cancelEditText()

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
