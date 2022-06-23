import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.insert(0, "C:\py\Dis\GUI")
sys.path.insert(0, "C:\py\Dis\Dialog")
import dialog_group
import main_window
import dialog_choose_vul
import dialog_filter
import dialog_op_add
import ipaddress
import function
import sqlite3
from sqlite3 import Error






class MyWin(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = main_window.Ui_BonsVul()  # Экземпляр класса Ui_MainWindow, в нем конструктор всего GUI.
        self.ui.setupUi(self)  # Инициализация GUI
        self.dialog = 0
        self.all_vul = {}
        self.conn = None
        self.textEdit = ''
        self.ui.saveTextEdit.setHidden(True)
        self.ui.cancelTextEdit.setHidden(True)
        self.ui.widgetVulnerability.setHidden(True)
        self.ui.widgetPort.setHidden(True)
        self.ui.widgetNode.setHidden(True)
        self.ui.widgetGroup.setHidden(True)

        self.ui.labelVulLVL.setHidden(True)
        self.ui.lineVulLVL.setHidden(True)

        self.ui.openVul.clicked.connect(self.openDialogOpenVul)# это кнопка должна стать анализировать!
        self.ui.groupVal.clicked.connect(self.openDialogGroup)   # Открыть новое диалогое окно для группировки узлов
        self.ui.editTextEdit.clicked.connect(self.editText)  # Изменение данных уязвимостей
        self.ui.saveTextEdit.clicked.connect(self.saveEditText)  # Сохранение данных уязвимостей
        self.ui.cancelTextEdit.clicked.connect( self.cancelEditText)  # Отмена изменение данных уязвимостей
        self.ui.chooseVulnaribilityBtn.clicked.connect(self.openDialogChooseVulnaribilityCVSS)# Открыть новое диалговое окно изменение всех уязвимостей

        self.setWindowTitle('BonsVul')
        self.createMenuBar()

        self.ui.addLocalRule.clicked.connect(self.openDialogAddLocalRule)
        self.ui.addForwardRule.clicked.connect(self.openDialogAddForwardRule)
        self.ui.addUserPO.clicked.connect(self.openDialogAddPO)

        self.ui.lvl11Btn.clicked.connect(self.chooseGroupVul)

        self.infoAboutNetworkDefault()

    def infoAboutNetworkDefault(self):

        self.ui.editUserPO.setHidden(True)
        self.ui.saveUserPO.setHidden(True)
        self.ui.cancelUserPO.setHidden(True)
        self.ui.deleteUserPO.setHidden(True)

        self.ui.editForwardRule.setHidden(True)
        self.ui.saveForwardRule.setHidden(True)
        self.ui.cancelForwardRule.setHidden(True)
        self.ui.deleteForwardRule.setHidden(True)
        self.ui.deleteForwardRule.setHidden(True)
        self.ui.pushForwardDown.setHidden(True)
        self.ui.pushForwardUp.setHidden(True)

        self.ui.editLocalRule.setHidden(True)
        self.ui.saveLocalRule.setHidden(True)
        self.ui.cancelLocalRule.setHidden(True)
        self.ui.deleteLocalRule.setHidden(True)
        self.ui.pushLocalDown.setHidden(True)
        self.ui.pushLocalUp.setHidden(True)


        model_default = QtGui.QStandardItemModel()
        qitem = QtGui.QStandardItem()
        qitem.setCheckState(QtCore.Qt.Checked)
        qitem.setText('Действие: Разрешенно | Источники: Все | Назначение: Все | Порты: Все')
        model_default.appendRow(qitem)

        model_default_PO = QtGui.QStandardItemModel()
        qitem = QtGui.QStandardItem()
        qitem.setText('Неизвестные: Все ')
        model_default_PO.appendRow(qitem)

        self.ui.listViewLocalRule.setModel(model_default)
        self.ui.listViewForwardRule.setModel(model_default)
        self.ui.listViewUserPO.setModel(model_default_PO)
        self.ui.listViewLocalRule.setEnabled(False)
        self.ui.listViewForwardRule.setEnabled(False)
        self.ui.listViewUserPO.setEnabled(False)

    def createMenuBar(self):
        self.menuBar = QtWidgets.QMenuBar(self)
        self.setMenuBar(self.menuBar)

        fileMenu = QtWidgets.QMenu('&Файл', self)
        self.menuBar.addMenu(fileMenu)

        fileMenu.addAction('Открыть отчёты об уязвимостях', self.openDialogOpenVul)
        fileMenu.addSeparator()
        fileMenu.addAction('Открыть проект', self.action_save_clicked)
        fileMenu.addAction('Сохранить проект', self.action_save_clicked)

    @QtCore.pyqtSlot() #аннотация обработки нажатия в меню
    def action_save_clicked(self):
        self.fname = QtWidgets.QFileDialog.getOpenFileName(self, '', '', ('xml File(*.xml)'))[0]  # выбирать 1ый файл из всей выборки, если даже пользователь выберетм ного файлов /получаю путь до файла



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
                    # cur.execute(
                    #     'SELECT * FROM report_cvss2 WHERE report_cvss2.id = ' + str(
                    #         result_vul[5]) + ';')
                    # cvss2 = cur.fetchone()
                    # cur.execute(
                    #     'SELECT * FROM report_cvss3 WHERE report_cvss3.id = ' + str(
                    #         result_vul[6]) + ';')
                    # cvss3 = cur.fetchone()
                    vulnerubility = {'name': result_vul[1], 'shortdescription': result_vul[2],
                                     'description': result_vul[3],
                                     'solution': result_vul[4], 'cvss2': result_vul[5] + " Score:" + result_vul[7], 'cvss3': result_vul[6]+ " Score:" + result_vul[8], 'id': result_vul[0]}
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

    def treeFunction(self, index):  # 4 разных ситуаций нужно описать.


        parent_parent_parent_parent_row = index.parent().parent().parent().parent().row()
        parent_parent_parent_row = index.parent().parent().parent().row()
        parent_parent_row = index.parent().parent().row()
        parent_row = index.parent().row()
        row = index.row()

        self.ui.editTextEdit.setEnabled(False)
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
                item = function.firstLvlTree(row, self.all_vul)
                self.ui.widgetVulnerability.setHidden(True)
                self.ui.widgetPort.setHidden(True)
                self.ui.widgetNode.setHidden(False)
                self.ui.widgetGroup.setHidden(True)
            except:
                item = function.firstLvlTreeGroup(row, self.all_vul)
                self.ui.widgetVulnerability.setHidden(True)
                self.ui.widgetPort.setHidden(True)
                self.ui.widgetNode.setHidden(True)
                self.ui.widgetGroup.setHidden(False)
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
                item = function.secondLvlTree(row, parent_row, self.all_vul)
                self.ui.widgetVulnerability.setHidden(True)
                self.ui.widgetPort.setHidden(False)
                self.ui.widgetNode.setHidden(True)
                self.ui.widgetGroup.setHidden(True)
                for key in item:
                    print(item[key])
            except:
                item = function.secondLvlTreeGroup(row, parent_row, self.all_vul)
                self.ui.widgetVulnerability.setHidden(True)
                self.ui.widgetVulnerability.setHidden(True)
                self.ui.widgetPort.setHidden(False)
                self.ui.widgetNode.setHidden(True)
                self.ui.widgetGroup.setHidden(True)
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
                item = function.thirdLvlTree(row, parent_row, parent_parent_row, self.all_vul)
                self.ui.widgetVulnerability.setHidden(False)
                self.ui.widgetPort.setHidden(True)
                self.ui.widgetNode.setHidden(True)
                self.ui.widgetGroup.setHidden(True)
                self.ui.editTextEdit.setEnabled(True)
            except:
                item = function.thirdLvlTreeGroup(row, parent_row, parent_parent_row, self.all_vul)
        elif parent_parent_parent_parent_row == -1:
            print('4')
            item = function.fourthLvlTreeGroup(row, parent_row, parent_parent_row, parent_parent_parent_row, self.all_vul)
            self.ui.widgetVulnerability.setHidden(False)
            self.ui.widgetPort.setHidden(True)
            self.ui.widgetNode.setHidden(True)
            self.ui.widgetGroup.setHidden(True)
            self.ui.editTextEdit.setEnabled(True)
        else:
            self.errorMessange('Какая-то ошибка с treeView!')

        #Вывод данных, которые ты получил
        if self.ui.widgetVulnerability.isHidden() == False:
            for key in item:
                if key != 'id':
                    if self.ui.lineNameVulEdit.objectName().lower().find(str(key)) != -1:
                        self.ui.lineNameVulEdit.setText(item[key])
                    elif self.ui.textDescriptionEdit.objectName().lower().find(str(key)) != -1:
                        self.ui.textDescriptionEdit.setText(item[key])
                        tmp_check_len = 0
                        if (len(item[key])) > 400:
                            print(len(item[key]))
                            tmp_check_len += (len(item[key]) - 400) //100
                        if (item[key].find('\n') != -1):
                            tmp_check_len += item[key].count('\n')
                        print(tmp_check_len)
                        self.ui.textDescriptionEdit.setMinimumSize(QtCore.QSize(0, 70 + tmp_check_len * 20))
                    elif self.ui.textShortDescriptionEdit.objectName().lower().find(str(key)) != -1:
                        self.ui.textShortDescriptionEdit.setText(item[key])
                    elif self.ui.textSolutionEdit.objectName().lower().find(str(key)) != -1:
                        self.ui.textSolutionEdit.setText(item[key])
                        if (len(item[key])) > 400:
                            tmp_check_len = (len(item[key]) - 400) //100
                            self.ui.textSolutionEdit.setMinimumSize(QtCore.QSize(0, self.ui.textSolutionEdit.size().height() + tmp_check_len * 20))
                    elif self.ui.lineCVSS2Edit.objectName().lower().find(str(key)) != -1:
                        self.ui.lineCVSS2Edit.setText(item[key])
                    elif self.ui.lineCVSS3Edit.objectName().lower().find(str(key)) != -1:
                        self.ui.lineCVSS3Edit.setText(item[key])

        #Вывод данных, которые ты получил
        if self.ui.widgetGroup.isHidden() == False:
            self.ui.labelVulLVL.setText('Среднее значение уровеня опасности')
            self.ui.label11lvlVulnaribility.setText('1224')
            self.ui.label11lvlNode.setText('12')
            self.ui.label11lvlPort.setText('97')
            pass
        self.ui.labelVulLVL.setHidden(False)
        self.ui.lineVulLVL.setHidden(False)
        self.ui.openVul.setEnabled(True)

    def editText(self):
        if self.ui.widgetVulnerability.isHidden() == False:
            self.ui.lineCVSS3Edit.setReadOnly(False)
            self.ui.lineCVSS2Edit.setReadOnly(False)
            self.ui.textSolutionEdit.setReadOnly(False)
            self.ui.textDescriptionEdit.setReadOnly(False)
            self.ui.textShortDescriptionEdit.setReadOnly(False)
            self.ui.lineNameVulEdit.setReadOnly(False)

        self.ui.saveTextEdit.setHidden(False)
        self.ui.cancelTextEdit.setHidden(False)
        self.ui.editTextEdit.setEnabled(False)
        self.ui.editTextEdit.setHidden(True)

    def saveEditText(self):
        parent_parent_parent_parent_row = self.ui.treeViewVul.currentIndex().parent().parent().parent().parent().row()
        parent_parent_parent_row = self.ui.treeViewVul.currentIndex().parent().parent().parent().row()
        parent_parent_row = self.ui.treeViewVul.currentIndex().parent().parent().row()
        parent_row = self.ui.treeViewVul.currentIndex().parent().row()
        row = self.ui.treeViewVul.currentIndex().row()
        if self.ui.widgetVulnerability.isHidden() == False:
            vul = {'name':  self.ui.lineNameVulEdit.text(), 'shortdescription': self.ui.textShortDescriptionEdit.toPlainText(),
                             'description': self.ui.textDescriptionEdit.toPlainText(),
                             'solution': self.ui.textSolutionEdit.toPlainText(), 'cvss2': self.ui.lineCVSS2Edit.text(),
                   'cvss3': self.ui.lineCVSS3Edit.text()}

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
                item = function.firstLvlTree(row, self.all_vul)
                #Тут писать то что изменили, ввод в БД данные
            except:
                item = function.firstLvlTreeGroup(row, self.all_vul)
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
                item = function.secondLvlTree(row, parent_row, self.all_vul)
                #Тут писать то что изменили, ввод в БД данные
            except:
                item = function.secondLvlTreeGroup(row, parent_row, self.all_vul)
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
                item = function.thirdLvlTree(row, parent_row, parent_parent_row, self.all_vul)

                function.updateVulSavebtn(item, vul, self.conn)
            except:
                item = function.thirdLvlTreeGroup(row, parent_row, parent_parent_row, self.all_vul)
                #Тут писать то что изменили, ввод в БД данные
        elif parent_parent_parent_parent_row == -1:
            print('4')
            item = function.fourthLvlTreeGroup(row, parent_row, parent_parent_row, parent_parent_parent_row, self.all_vul)
            function.updateVulSavebtn(item, vul, self.conn)
        else:
            self.errorMessange('Какая-то ошибка с treeView!')

        if self.ui.widgetVulnerability.isHidden() == False:
            for key in item:
                if key != 'id':
                    if self.ui.lineNameVulEdit.objectName().lower().find(str(key)) != -1:
                        self.ui.lineNameVulEdit.setText(item[key])
                    elif self.ui.textDescriptionEdit.objectName().lower().find(str(key)) != -1:
                        self.ui.textDescriptionEdit.setText(item[key])
                        if (len(item[key])) > 400:
                            tmp_check_len = (len(item[key]) - 400) // 100
                            self.ui.textDescriptionEdit.setMinimumSize(
                                QtCore.QSize(0, self.ui.textDescriptionEdit.size().height() + tmp_check_len * 20))
                    elif self.ui.textShortDescriptionEdit.objectName().lower().find(str(key)) != -1:
                        self.ui.textShortDescriptionEdit.setText(item[key])
                    elif self.ui.textSolutionEdit.objectName().lower().find(str(key)) != -1:
                        self.ui.textSolutionEdit.setText(item[key])
                        if (len(item[key])) > 400:
                            tmp_check_len = (len(item[key]) - 400) // 100
                            self.ui.textSolutionEdit.setMinimumSize(
                                QtCore.QSize(0, self.ui.textSolutionEdit.size().height() + tmp_check_len * 20))
                    elif self.ui.lineCVSS2Edit.objectName().lower().find(str(key)) != -1:
                        self.ui.lineCVSS2Edit.setText(item[key])
                    elif self.ui.lineCVSS3Edit.objectName().lower().find(str(key)) != -1:
                        self.ui.lineCVSS3Edit.setText(item[key])
        self.cancelEditText()

    def cancelEditText(self):

        self.ui.saveTextEdit.setHidden(True)
        self.ui.cancelTextEdit.setHidden(True)
        self.ui.editTextEdit.setHidden(False)
        self.ui.editTextEdit.setEnabled(True)
        if self.ui.widgetVulnerability.isHidden() == False:
            self.ui.lineCVSS3Edit.setReadOnly(True)
            self.ui.lineCVSS2Edit.setReadOnly(True)
            self.ui.textSolutionEdit.setReadOnly(True)
            self.ui.textDescriptionEdit.setReadOnly(True)
            self.ui.textShortDescriptionEdit.setReadOnly(True)
            self.ui.lineNameVulEdit.setReadOnly(True)

    def chooseGroupVul(self):
        self.ui.labelVulLVL.setText('Уровень опасности')
        self.ui.widgetVulnerability.setHidden(False)
        pass

#####################################################Group
    def openDialogGroup(self):
        model_nodes = self.ui.treeViewVul.model()
        nodes = []
        for i in range(0, model_nodes.rowCount()):

            try:
                ipaddress.ip_address(model_nodes.item(i).text())
                nodes.append(model_nodes.item(i).text())
            except:
                print(model_nodes.item(i).text())
        dialog = dialog_group.ClssDialogGroup(self)
        dialog.setNodes(nodes)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:  # Получаем после закрытия диалогового окна
            keys = list(self.all_vul.keys())

            # print(dialog.di.listNodesChosen.model().item(0).text())
            if len(dialog.di.lineEditNameGroup.text()) == 0:
                self.errorMessange('Вы не ввели название гурппы')
                return 0
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
                if (dialog.di.lineEditStartIP.text() == '0.0.0.0'):  #Выброчная группировка

                    model_nodes = dialog.di.listNodesChosen.model()
                    if (model_nodes != None):
                        for i in range(0, model_nodes.rowCount()):
                            need_nodes.append(ipaddress.ip_address(model_nodes.item(i).text()))

                else: #Диапозон
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
#####################################################Group
#####################################################cvss
    def openDialogChooseVulnaribilityCVSS(self):
        self.ui.calcVulnaribilityBtn.setEnabled(True)
        dialog = dialog_choose_vul.ClssDialogChooseVul(self)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:  # Получаем после закрытия диалогового окна
            print(dialog.cvss_current)
            print(QtWidgets.QPushButton)
            print(self.ui.horizontalLayout_8.findChildren(self, QtWidgets.QPushButton))
            pass
#####################################################cvss
#####################################################filter
    def openDialogAddLocalRule(self):
        self.ui.saveLocalRule.setEnabled(True)
        self.ui.cancelLocalRule.setEnabled(True)
        dialog = dialog_filter.ClssDialogFilter(self)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:  # Получаем после закрытия диалогового окна
            pass
#####################################################filter
#####################################################filter
    def openDialogAddForwardRule(self):

        self.ui.saveForwardRule.setEnabled(True)
        self.ui.cancelForwardRule.setEnabled(True)
        dialog = dialog_filter.ClssDialogFilter(self)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:  # Получаем после закрытия диалогового окна

            modelDSTIP = dialog.di.listDSTIP.model()
            modelSRCIP = dialog.di.listSRCIP.model()
            modelPort = dialog.di.listViewPort.model()
            srcIP = ''
            dstIP = ''
            port = ''
            for i in range(0, modelSRCIP.rowCount()):
                srcIP += modelSRCIP.item(i).text() + '; '
            for i in range(0, modelDSTIP.rowCount()):
                dstIP += modelDSTIP.item(i).text() + '; '
            for i in range(0, modelPort.rowCount()):
                port += modelPort.item(i).text() + '; '

            nameRule = dialog.di.lineEdit.text()
            if dialog.di.radioBlock.isChecked():
                action = 'Блокировать'
            else:
                action = 'Разешено'
            turnOn = dialog.di.checkBox.isChecked()

            model = self.ui.listViewForwardRule.model()

            if (model.rowCount() == 1 and model.item(0).text() == 'Все'):
                self.ui.listViewForwardRule.setEnabled(True)
                model.removeRow(0)
                model = QtGui.QStandardItemModel()
                self.ui.listViewForwardRule.setModel(model)
            item = QtGui.QStandardItem(str(turnOn) + ' ' + str(nameRule) + ' ' + str(action) + ' ' + str(srcIP) + ' ' + str(dstIP) + ' ' + str(port))
            model.appendRow(item)

#####################################################filter
#####################################################PO
    def openDialogAddPO(self):

        self.ui.saveUserPO.setEnabled(True)
        self.ui.cancelUserPO.setEnabled(True)
        dialog = dialog_op_add.ClssDialogOPAdd(self)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:  # Получаем после закрытия диалогового окна
            pass

#####################################################PO

    def errorMessange(self, text):
        error = QtWidgets.QMessageBox()
        error.setWindowTitle("Ошибка")
        error.setText(text)
        error.setIcon(QtWidgets.QMessageBox.Warning)
        error.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

        error.exec_()

    def resizeEvent(self, *args, **kwargs):
        self.ui.verticalLayout_13.setGeometry(QtCore.QRect(0, 0, self.width(), self.height()))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWin()
    window.show()
    sys.exit(app.exec_())
