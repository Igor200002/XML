from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QInputDialog, QLineEdit, QMessageBox
from PyQt5.QtGui import QColor
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import xml.etree.ElementTree as ET
import sys
import re
import random as ran
from testallproject import Ui_MainWindow


file_opened = False
#parser = ET.XMLParser(encoding="utf-8")
#tree_char = ET.parse('ShablonPawn.xml', parser=parser)
#root_char = tree_char.getroot()
rel = []
input_all = []
arr_all_id_chars = []
input_dialog = []
input_answer = []
input_str_ans = []
quest_person = "true"
quest_robot = "true"
gender = "М"
flag_answer = False
flag_module = True
flag_search_house = True
flag_append_house = True
item_build_dict = {}
class Xml_perevod(QtWidgets.QMainWindow):

    def __init__(self):
        super(Xml_perevod, self).__init__()
        self.base = Ui_MainWindow()
        self.base.setupUi(self)
        self.base.name_ext.setVisible(False)
        self.base.exit.setVisible(False)
        self.visibleAnswer(False)
        self.visible_edit_house_off(False)
        self.base.open_file_dialog.setVisible(False)
        self.base.save_all.clicked.connect(self.enterHuman)
        self.base.save_rel.clicked.connect(self.enterRel)
        self.base.comboGenger.activated[str].connect(self.onChangedGender)
        self.base.comboQuest.activated[str].connect(self.onChangedQuest_Man)
        self.base.save_all_robot.clicked.connect(self.enterRobot)
        self.base.comboQuest_robot.activated[str].connect(self.onChangedQuest_robot)
        self.base.clean_button.clicked.connect(self.clearAll)
        self.base.clean_button_robot.clicked.connect(self.clearAll)
        self.base.open_file.clicked.connect(self.openFileChar)
        self.base.delete_char.clicked.connect(self.removeRecordChar)
        self.base.create_file_dialog.clicked.connect(self.createXml)
        self.base.answers_button.clicked.connect(self.haveAnswer)
        self.base.save_answer.clicked.connect(self.save_one_answer)
        self.base.save_all_dialog.clicked.connect(self.enter_full_dialog)
        self.base.open_house_file.clicked.connect(self.open_xml_house)
        self.base.all_house.itemClicked.connect(self.choose_item)
        self.base.find_house.clicked.connect(self.active_search_house)
        self.base.pushButton_search_id_house.clicked.connect(lambda: self.search_house(self.base.search_id_house.text()))
        self.base.append_house.clicked.connect(self.active_house_panel)
        self.base.pushButton_save_house.clicked.connect(self.append_house)
        self.base.delete_house.clicked.connect(self.remove_house)
        self.base.append_module.clicked.connect(self.visible_modules)
        self.base.comboBox_TypeOFModule.currentTextChanged.connect(self.type_module)
        #self.base.comboBox_label_Shab_Or_Hand.currentTextChanged.connect(lambda: self.shop_and_workplace(False))
        self.base.random_flat.clicked.connect(self.rand_flat)
        global grey_color
        grey_color = QColor()
        grey_color.setRgb(240, 240, 240)

    def rand_flat(self):
        self.base.Kolvo_rab.setText(str(ran.randint(1,100)))

    def append_module(self):
        str_module = f"<Module> <DescriptionModule>{self.base.Description.text()}</DescriptionModule>"
        module_type = self.base.comboBox_TypeOFModule.currentText()
        match module_type:
            case "FlatModule":
                if self.base.Kolvo_rab.text() == "":
                    str_module += f"<FlatNumber>{str(ran.randint(1,100))}</FlatNumber>"
                else:
                    str_module += f"<FlatNumber>{self.base.Kolvo_rab.text()}</FlatNumber>"
            case "ShopModule":
                str_module +=f"<Work><Place>{self.base.Kolvo_rab.text()}</Place><WorkShift><Shift><Workers>"
                shab_or_hand = self.base.comboBox_label_Shab_Or_Hand.currentText()
                if shab_or_hand == "Шаблон":
                    str_module+=f"<TypeOfWorkers>{self.base.comboBox_Shablon.currentText()}"
                else:
                    str_module += f""

            case "WorkPlaceModule":
                self.shop_and_workplace(True)

    '''
    def workers(self):
        global workers
        workers = {}

    def append_worker(self,text1,text2):
        global workers
        if int(self.base.Kolvo_rab.text()) >= len(workers):
            msg = QMessageBox()
            msg.setText("Слишком много рабочих")
            msg.exec_()
        workers = {}
        workers[text1] = text2

    def append_workers_L(self):
        global workers
        if int(self.base.Kolvo_rab.text()) >= len(workers):
            msg = QMessageBox()
            msg.setText("Слишком много рабочих")
            msg.exec_()
        workers = {}
        workers[self.base.label_Lider.text()] = self.base.comboBox_Lider.currentText()

    def append_workers_S(self):
        global workers
        if int(self.base.Kolvo_rab.text()) >= len(workers):
            msg = QMessageBox()
            msg.setText("Слишком много рабочих")
            msg.exec_()
        workers = {}
        workers[self.base.label_Lider.text()] = self.base.comboBox_Lider.currentText()

    def append_workers_W(self):
        global workers
        if int(self.base.Kolvo_rab.text()) >= len(workers):
            msg = QMessageBox()
            msg.setText("Слишком много рабочих")
            msg.exec_()
        workers = {}
        workers[self.base.label_Lider.text()] = self.base.comboBox_Lider.currentText()
    '''

    def type_module(self):
        self.visible_modul(False)
        module_type = self.base.comboBox_TypeOFModule.currentText()
        match module_type:
            case "FlatModule":
                self.flat_module(True)
            case "ShopModule":
                self.shop_and_workplace(True)
            case "WorkPlaceModule":
                self.shop_and_workplace(True)


    def shop_and_workplace(self, flag):
        self.visible_modul(False)
        self.base.label_Kolvo_rab.setVisible(flag)
        self.base.Kolvo_rab.setVisible(flag)
        self.base.label_Shab_Or_Hand.setVisible(flag)
        self.base.comboBox_label_Shab_Or_Hand.setVisible(flag)
        self.base.label_Kolvo_rab.setText("Количество рабочих")
        shab_or_hand = self.base.comboBox_label_Shab_Or_Hand.currentText()
        if shab_or_hand == "Шаблон":
            self.base.label_Start_work.setVisible(flag)
            self.base.Start_work.setVisible(flag)
            self.base.label_Shablon.setVisible(flag)
            self.base.comboBox_Shablon.setVisible(flag)
            self.base.label_shift_duration.setVisible(flag)
            self.base.shift_duration.setVisible(flag)
        else:
            self.base.label_Start_work.setVisible(flag)
            self.base.Start_work.setVisible(flag)
            self.base.label_Shablon.setVisible(flag)
            self.base.comboBox_Shablon.setVisible(flag)
            self.base.label_shift_duration.setVisible(flag)
            self.base.shift_duration.setVisible(flag)
            self.base.label_Lider.setVisible(flag)
            self.base.comboBox_Lider.setVisible(flag)
            self.base.label_Specialist.setVisible(flag)
            self.base.comboBox_Specialist.setVisible(flag)
            self.base.label_Workman.setVisible(flag)
            self.base.comboBox_Workman.setVisible(flag)
            self.base.pushButton_save_rab.setVisible(flag)
    def flat_module(self, flag):
        self.base.label_Kolvo_rab.setVisible(flag)
        self.base.Kolvo_rab.setVisible(flag)
        self.base.random_flat.setVisible(flag)
        self.base.label_Kolvo_rab.setText("Номер квартиры")

    def remove_house(self):
        #print(self.base.all_house.currentRow())
        if self.base.all_house.currentRow() == -1:
            msg = QMessageBox()
            msg.setText("Сначала выбери здание ебанько, потом удаляй.")
            msg.exec_()
            return
        global item_build_dict
        global root_house
        elem_remove = item_build_dict[self.base.all_house.item(self.base.all_house.currentRow()).text()]
        question = QMessageBox.question(self, "Удалить здание", "Точно удалить здание?  " + elem_remove,
                                        QMessageBox.Yes | QMessageBox.No)
        if question == QMessageBox.No:
            return
        for elem in root_house.findall('District'):
            for under in elem.findall('Building'):
                if under.get('BuildingID') == elem_remove:
                    elem.remove(under)
                    break

        ET.indent(tree_house, space='  ', level=0)
        tree_house.write(house_file[0], encoding="utf-8")
        item_build_dict.pop(self.base.all_house.item(self.base.all_house.currentRow()).text())
        removed = self.base.all_house.takeItem(self.base.all_house.currentRow())
        if self.base.all_house.currentRow() < self.base.all_house.count():
            self.base.all_house.item(self.base.all_house.currentRow()).setSelected(False)
        self.base.all_module.clear()
        self.base.append_module.setText("Добавить модуль")
        self.base.append_module.setVisible(False)
        self.base.delete_module.setVisible(False)






    def append_house(self):
        global bilding_id
        global bilding_kolvo_indisr
        global item_build_dict
        item_build_dict = {}
        arr_house = []
        arr_house.append(self.base.id_house.text().upper())
        arr_house.append(self.base.house_name.text())
        arr_house.append(self.base.house_desc.text())
        dist_id = ""
        id_h = ""
        flag = False
        for i in range(len(arr_house[0])):
            if flag == True:
                id_h += arr_house[0][i]
            if arr_house[0][i] != "-" and flag == False:
                dist_id += arr_house[0][i]
            else:
                flag = True
        #print(dist_id)
        #print(id_h)
        for i in range(len(bilding_id)):
            if bilding_id[i] == arr_house[0] or arr_house[0] == dist_id:
                question = QMessageBox.question(self, "Этот ID уже занят!" , "Заполнить ли ID автоматически последним элементом в данном районе?",
                                                QMessageBox.Yes | QMessageBox.No)
                if question == QMessageBox.Yes:
                    #print(type(re.findall(r'\b\d+\b', bilding_id[i])))
                    #govno = re.findall(r'\b\d+\b', )
                    for elem in root_house.findall('District'):
                        if elem.get('DistrictID') == dist_id:
                            govno = len(elem.findall('Building'))
                            #print(govno)
                    arr_house[0] = dist_id + "-" + str(govno + 1)
                    #print(arr_house[0])
                    self.base.id_house.setText(arr_house[0])
                    break
                else:
                    return


        dist_id = dist_id.upper()
        house_str = f"<Building> <BuildingName>{arr_house[1]}</BuildingName><Description>{arr_house[2]}</Description><BuildingModule></BuildingModule></Building>"
        house_str_et = ET.fromstring(house_str)
        for elem in house_str_et.iter('Building'):
            elem.set("BuildingID", arr_house[0].upper())
        for elem in root_house.findall('District'):
            if elem.get('DistrictID') == dist_id:
                elem.append(house_str_et)
        ET.indent(tree_house, space='  ', level=0)
        tree_house.write(house_file[0], encoding="utf-8")

        chet = 0
        bilding_kolvo_indisr = []
        bilding_id = []
        self.base.all_house.clear()
        for elem in root_house.findall('District'):
            self.base.all_house.addItems(
                ["Имя дистрикта: " + elem.get('DistrictName') + "; ID = " + elem.get('DistrictID')])
            for underelem in elem.findall('Building'):
                self.base.all_house.addItems(["         ID здания = " + str(underelem.get('BuildingID')) + "; Имя здания: " + str(underelem.find('BuildingName').text)])
                item_build_dict["         ID здания = " + str(underelem.get('BuildingID')) + "; Имя здания: " + str(underelem.find('BuildingName').text)] = str(underelem.get('BuildingID'))
                bilding_id.append(str(underelem.get('BuildingID')))
                chet += 1
            bilding_kolvo_indisr.append(chet)
            chet = 0
        #change = tree_house.find("District/Building/[BuildingName='Ресторан-бар «Рагнарек»']")
        for i in range(self.base.all_house.count()):
            if i % 2 == 0:
                self.base.all_house.item(i).setBackground(grey_color)
        self.search_house(arr_house[0])




    def active_house_panel(self):
        global flag_append_house
        self.base.groupBox_append_house.setVisible(flag_append_house)
        if flag_append_house == True:
            self.base.append_house.setText("Закрыть панель")
        else:
            self.base.append_house.setText("Добавить здание")
        flag_append_house = not flag_append_house

    def search_house(self, _text1):
        id_dom_probel = " "
        id_dom = _text1
        id_dom_probel+=id_dom
        #print(id_dom_probel)
        #label_id_houseprint(id_dom)
        for i in range(self.base.all_house.count()):
            if id_dom_probel.lower() in self.base.all_house.item(i).text().lower() and "здания" in self.base.all_house.item(i).text():
                self.base.all_house.item(i).setSelected(True)
                self.base.all_house.scrollToItem(self.base.all_house.item(i),QAbstractItemView.PositionAtCenter)
                self.choose_item(self.base.all_house.item(i))
                self.base.all_house.setCurrentRow(i)
                return
        for i in range(self.base.all_house.count()):
            if id_dom.lower() in self.base.all_house.item(i).text().lower() and "здания" in self.base.all_house.item(i).text():
                self.base.all_house.item(i).setSelected(True)
                self.base.all_house.scrollToItem(self.base.all_house.item(i), QAbstractItemView.PositionAtCenter)
                self.choose_item(self.base.all_house.item(i))
                self.base.all_house.setCurrentRow(i)
                return


        msg = QMessageBox()
        msg.setText("Здание не было найдено.")
        msg.exec_()


    def active_search_house(self):
        global flag_search_house
        self.base.groupBox_search_house.setVisible(flag_search_house)
        if flag_search_house == True:
            self.base.find_house.setText("Закрыть панель")
        else:
            self.base.find_house.setText("Найти здание")
        flag_search_house = not flag_search_house

    def choose_item(self, item):
        self.base.all_module.clear()
        item_text = item.text()
        id_house = ""
        flag_choose_item = False
        house_info = []
        modul_info = []
        chet_modul = 0
        self.base.all_module.setWordWrap(True)
        if "дистрикт" in item_text:
            msg = QMessageBox()
            msg.setText("Это район, а не здание, ебланчик.\nЭТО ДЛЯ УДОБСТВА!!!\nВЫБЕРИ ЗДАНИЕ, ПОМОЙКА")
            self.base.all_house.item(self.base.all_house.currentRow()).setSelected(False)
            msg.exec_()
            return

        for i in range(len(item_text) - 2):
            if flag_choose_item:
                id_house += item_text[i+1]
            if item_text[i] == "=":
                flag_choose_item = True
            if item_text[i+2] == ";":
                break
        #print(id_house)
        #print(len(id_house))
        global change
        global dict_id_module
        dict_id_module = {}
        change = tree_house.find(f"District/Building/[@BuildingID='{id_house}']")
        house_info.append(change.get('BuildingID'))
        house_info.append(change.find('BuildingName').text)
        house_info.append(change.find('Description').text)
        self.base.all_module.addItems([f"ID дома = {house_info[0]}; Название дома: {house_info[1]}; Описание дома: {house_info[2]}"])
        for upelem in change.findall('BuildingModule'):
            for elem in upelem.findall('Module'):
                chet_modul +=1
                lang = elem.get('TypeOFModule')
                match lang:
                    case "FlatModule":
                        modul_info.append(elem.get('TypeOFModule'))
                        modul_info.append(elem.get('ModuleSequenceID'))
                        modul_info.append(elem.find('DescriptionModule').text)
                        modul_info.append(elem.find('FlatNumber').text)
                        self.base.all_module.addItems([f"{chet_modul}. Тип модуля = {elem.get('TypeOFModule')}; ID модуля = {elem.get('ModuleSequenceID')}; Описание модуля: {elem.find('DescriptionModule').text}; Номер квартиры = {elem.find('FlatNumber').text}"])
                        dict_id_module[f"{chet_modul}. Тип модуля = {elem.get('TypeOFModule')}; ID модуля = {elem.get('ModuleSequenceID')}; Описание модуля: {elem.find('DescriptionModule').text}; Номер квартиры = {elem.find('FlatNumber').text}"] = elem.get('ModuleSequenceID')
                    case "ChillModule":
                        modul_info.append(elem.get('TypeOFModule'))
                        modul_info.append(elem.get('ModuleSequenceID'))
                        modul_info.append(elem.find('DescriptionModule').text)
                        self.base.all_module.addItems([f"{chet_modul}. Тип модуля = {elem.get('TypeOFModule')}; ID модуля = {elem.get('ModuleSequenceID')}; Описание модуля: {elem.find('DescriptionModule').text}"])
                        dict_id_module[
                            f"{chet_modul}. Тип модуля = {elem.get('TypeOFModule')}; ID модуля = {elem.get('ModuleSequenceID')}; Описание модуля: {elem.find('DescriptionModule').text}"] = elem.get(
                            'ModuleSequenceID')
                    case "QuestModule":
                        modul_info.append(elem.get('TypeOFModule'))
                        modul_info.append(elem.get('ModuleSequenceID'))
                        modul_info.append(elem.find('DescriptionModule').text)
                        self.base.all_module.addItems([f"{chet_modul}. Тип модуля = {elem.get('TypeOFModule')}; ID модуля = {elem.get('ModuleSequenceID')}; Описание модуля: {elem.find('DescriptionModule').text}"])
                        dict_id_module[
                            f"{chet_modul}. Тип модуля = {elem.get('TypeOFModule')}; ID модуля = {elem.get('ModuleSequenceID')}; Описание модуля: {elem.find('DescriptionModule').text}"] = elem.get(
                            'ModuleSequenceID')
                    case "ShopModule":
                        modul_info.append(elem.get('TypeOFModule'))
                        modul_info.append(elem.get('ModuleSequenceID'))
                        modul_info.append(elem.find('DescriptionModule').text)
                        modul_info.append(elem.find('Work/Place').text)
                        shift = elem.find('Work/WorkShift/Shift')
                        modul_info.append(shift.get('StartTime'))
                        modul_info.append(shift.get('DurationShift'))
                        modul_info.append(elem.find('Work/WorkShift/Shift/Workers/TypeOfWorkers').text)
                        self.base.all_module.addItems([f"{chet_modul}. Тип модуля = {elem.get('TypeOFModule')}; ID модуля = {elem.get('ModuleSequenceID')}; Описание модуля: {elem.find('DescriptionModule').text};"
                                                       f"Количество рабочих = {elem.find('Work/Place').text}; Время начала смены = {shift.get('StartTime')}; Длительность смены = {shift.get('DurationShift')}; Тип распределения рабочих = {elem.find('Work/WorkShift/Shift/Workers/TypeOfWorkers').text}"])
                        dict_id_module[
                            f"{chet_modul}. Тип модуля = {elem.get('TypeOFModule')}; ID модуля = {elem.get('ModuleSequenceID')}; Описание модуля: {elem.find('DescriptionModule').text};"
                                                       f"Количество рабочих = {elem.find('Work/Place').text}; Время начала смены = {shift.get('StartTime')}; Длительность смены = {shift.get('DurationShift')}; Тип распределения рабочих = {elem.find('Work/WorkShift/Shift/Workers/TypeOfWorkers').text}"] = elem.get(
                            'ModuleSequenceID')
                    case "WorkPlaceModule":
                        modul_info.append(elem.get('TypeOFModule'))
                        modul_info.append(elem.get('ModuleSequenceID'))
                        modul_info.append(elem.find('DescriptionModule').text)
                        modul_info.append(elem.find('Work/Place').text)
                        shift = elem.find('Work/WorkShift/Shift')
                        modul_info.append(shift.get('StartTime'))
                        modul_info.append(shift.get('DurationShift'))
                        modul_info.append(elem.find('Work/WorkShift/Shift/Workers/TypeOfWorkers').text)
                        self.base.all_module.addItems([f"{chet_modul}. Тип модуля = {elem.get('TypeOFModule')}; ID модуля = {elem.get('ModuleSequenceID')}; Описание модуля: {elem.find('DescriptionModule').text};"
                                                       f"Количество рабочих = {elem.find('Work/Place').text}; Время начала смены = {shift.get('StartTime')}; Длительность смены = {shift.get('DurationShift')}; Тип распределения рабочих = {elem.find('Work/WorkShift/Shift/Workers/TypeOfWorkers').text}"])
                        dict_id_module[
                            f"{chet_modul}. Тип модуля = {elem.get('TypeOFModule')}; ID модуля = {elem.get('ModuleSequenceID')}; Описание модуля: {elem.find('DescriptionModule').text};"
                            f"Количество рабочих = {elem.find('Work/Place').text}; Время начала смены = {shift.get('StartTime')}; Длительность смены = {shift.get('DurationShift')}; Тип распределения рабочих = {elem.find('Work/WorkShift/Shift/Workers/TypeOfWorkers').text}"] = elem.get(
                            'ModuleSequenceID')
        #print(modul_info)
        #print(chet_modul)
        #self.base.all_module.setFont(QtGui.QFont("Helvetica", 20))
        for i in range(self.base.all_module.count()):
            if i % 2 == 0:
                self.base.all_module.item(i).setBackground(grey_color)
        self.base.append_module.setVisible(True)
        self.base.delete_module.setVisible(True)


    def open_xml_house(self):
        global house_file
        house_file = QFileDialog.getOpenFileName(self, 'Open File')
        print(house_file)
        global tree_house
        global root_house
        global bilding_id
        global bilding_kolvo_indisr
        global item_build_dict
        item_build_dict = {}
        chet = 0
        bilding_kolvo_indisr = []
        bilding_id =[]
        if house_file[0] == '' or house_file[0].endswith('.xml') == False:
            print("AAAAAAAAAAAAA")
            print(house_file[0].endswith('.xml'))
            msg = QMessageBox()
            msg.setText("Выбери файл типа xml")
            msg.exec_()
            return
        parser = ET.XMLParser(encoding="utf-8")
        tree_house = ET.parse(house_file[0], parser=parser)
        root_house = tree_house.getroot()
        for elem in root_house.findall('District'):
            self.base.all_house.addItems(["Имя дистрикта: " + elem.get('DistrictName') + "; ID = " + elem.get('DistrictID')])
            for underelem in elem.findall('Building'):
                self.base.all_house.addItems(["         ID здания = " + str(underelem.get('BuildingID')) + "; Имя здания: " + str(underelem.find('BuildingName').text)])
                item_build_dict["         ID здания = " + str(underelem.get('BuildingID')) + "; Имя здания: " + str(underelem.find('BuildingName').text)] = str(underelem.get('BuildingID'))
                bilding_id.append(str(underelem.get('BuildingID')))
                chet +=1
            bilding_kolvo_indisr.append(chet)
            chet = 0
        for i in range(self.base.all_house.count()):
            if i % 2 == 0:
                self.base.all_house.item(i).setBackground(grey_color)
        self.base.append_house.setVisible(True)
        self.base.find_house.setVisible(True)
        self.base.delete_house.setVisible(True)
        #print(item_build_dict)
        #self.base.all_house.item(200).setSelected(True)
        #self.base.all_house.scrollToItem(self.base.all_house.item(200),QAbstractItemView.PositionAtTop)
        '''
        for i in range(self.base.all_house.count()):
            if "дистрикт" in str(self.base.all_house.item(i).text()):
                self.base.all_house.item(i).setSelected(False)
       
        change.set('BuildingID', 'Пошел нахуй' )
        for elem in change.findall('BuildingName'):
            elem.text = "говно"


        tree_house.write(house_file[0], encoding="utf-8")
        '''

    def visible_modules(self):
        global flag_module
        self.base.groupBox_moduls.setVisible(flag_module)
        self.base.all_house.setVisible(not flag_module)
        self.base.append_house.setVisible(not flag_module)
        self.base.find_house.setVisible(not flag_module)
        self.base.delete_house.setVisible(not flag_module)
        global flag_search_house
        flag_search_house = False
        global flag_append_house
        flag_append_house = False
        self.active_search_house()
        self.active_house_panel()
        if flag_module == True:
            self.base.append_module.setText("Закрыть панель")
        else:
            self.base.append_module.setText("Добавить модуль")
        flag_module = not flag_module
        self.type_module()

    def visible_modul(self, flag):
        self.base.label_Kolvo_rab.setVisible(flag)
        self.base.Kolvo_rab.setVisible(flag)
        self.base.random_flat.setVisible(flag)
        self.base.label_Shab_Or_Hand.setVisible(flag)
        self.base.comboBox_label_Shab_Or_Hand.setVisible(flag)
        self.base.label_Start_work.setVisible(flag)
        self.base.Start_work.setVisible(flag)
        self.base.label_Shablon.setVisible(flag)
        self.base.comboBox_Shablon.setVisible(flag)
        self.base.label_shift_duration.setVisible(flag)
        self.base.shift_duration.setVisible(flag)
        self.base.label_Lider.setVisible(flag)
        self.base.comboBox_Lider.setVisible(flag)
        self.base.label_Specialist.setVisible(flag)
        self.base.comboBox_Specialist.setVisible(flag)
        self.base.label_Workman.setVisible(flag)
        self.base.comboBox_Workman.setVisible(flag)
        self.base.pushButton_save_rab.setVisible(flag)


    def visible_edit_house_off(self, flag):
        self.base.groupBox_moduls.setVisible(flag)
        self.base.append_module.setVisible(flag)
        self.base.delete_module.setVisible(flag)
        self.base.groupBox_search_house.setVisible(flag)
        self.base.groupBox_append_house.setVisible(flag)
        self.base.append_house.setVisible(flag)
        self.base.find_house.setVisible(flag)
        self.base.delete_house.setVisible(flag)
        self.base.label_Kolvo_rab.setVisible(flag)
        self.base.Kolvo_rab.setVisible(flag)
        self.base.random_flat.setVisible(flag)
        self.base.label_Shab_Or_Hand.setVisible(flag)
        self.base.comboBox_label_Shab_Or_Hand.setVisible(flag)
        self.base.label_Start_work.setVisible(flag)
        self.base.Start_work.setVisible(flag)
        self.base.label_Shablon.setVisible(flag)
        self.base.comboBox_Shablon.setVisible(flag)
        self.base.label_shift_duration.setVisible(flag)
        self.base.shift_duration.setVisible(flag)
        self.base.label_Lider.setVisible(flag)
        self.base.comboBox_Lider.setVisible(flag)
        self.base.label_Specialist.setVisible(flag)
        self.base.comboBox_Specialist.setVisible(flag)
        self.base.label_Workman.setVisible(flag)
        self.base.comboBox_Workman.setVisible(flag)
        self.base.pushButton_save_rab.setVisible(flag)


    def save_one_answer(self):
        input_answer.append(self.base.tonode.text())
        input_answer.append(self.base.actquestA.text())
        input_answer.append(self.base.numquestA.text())
        input_answer.append(self.base.posofquestA.text())
        input_ans = self.base.answer.text()
        answerstr = "<answer> <text>" + input_ans + "</text></answer> "
        input_str_ans.append(answerstr)
        print(len(input_str_ans) + 1)
        self.base.answer_label.setText("Ответ № " + str(len(input_str_ans) + 1))
        self.base.answer.clear()


    def enter_full_dialog(self):
        x = 0
        input_dialog.append(self.base.tochar.text())
        input_dialog.append(self.base.actquest.text())
        input_dialog.append(self.base.numquest.text())
        input_dialog.append(self.base.posofquest.text())
        input_node = self.base.node.text()
        nodestr = "<node>" + "<npctext>" + input_node + "</npctext>"
        if flag_answer ==True:
            nodestr +="<answers>"
            for i in range(len(input_str_ans)):
                nodestr += input_str_ans[i]
            nodestr += "</answers> </node>"
        else:
            nodestr += "</node>"
        print(nodestr)
        str_add = ET.fromstring(nodestr)
        for elem in str_add.iter('node'):
            elem.set('tochar', input_dialog[0])
            elem.set('actquest', input_dialog[1])
            elem.set('numquest', input_dialog[2])
            elem.set('posofquest', input_dialog[3])
        if flag_answer == True:
            for elem in str_add.iter('answer'):
                print(x)
                elem.set('tonode', input_answer[x])
                elem.set('actquestA', input_answer[x+1])
                elem.set('numquestA', input_answer[x+2])
                elem.set('posofquestA', input_answer[x+3])
                x += 4

        self.base.answers_button.setEnabled(True)
        self.visibleAnswer(False)
        root_dialog.append(str_add)
        ET.indent(tree_dialog, space='  ', level=0)
        tree_dialog.write('output.xml', encoding="utf-8")


    def visibleAnswer(self, flag):
        self.base.answer_label.setVisible(flag)
        self.base.answer.setVisible(flag)
        self.base.save_answer.setVisible(flag)
        self.base.tonode_label_2.setVisible(flag)
        self.base.tonode.setVisible(flag)
        self.base.actquestA_label.setVisible(flag)
        self.base.actquestA.setVisible(flag)
        self.base.numquestA_label.setVisible(flag)
        self.base.numquestA.setVisible(flag)
        self.base.posofquestA_label.setVisible(flag)
        self.base.posofquestA.setVisible(flag)

    def haveAnswer(self):
        question = QMessageBox.question(self, "Ответы", "Будет ли диалог повторяться в игре?",
                                        QMessageBox.Yes | QMessageBox.No)
        if question == QMessageBox.Yes:
            self.visibleAnswer(True)
            global flag_answer
            flag_answer = True
        self.base.answers_button.setEnabled(False)



    def createXml(self):
        global root_dialog
        global tree_dialog
        root_dialog = ET.Element("dialogue")

        question = QMessageBox.question(self, "Повторение", "Будет ли диалог повторяться в игре?",
                                        QMessageBox.Yes | QMessageBox.No)
        if question == QMessageBox.Yes:
            root_dialog.set("more", str(1))
        else:
            root_dialog.set("more", str(0))

        tree_dialog = ET.ElementTree(root_dialog)
        ET.indent(tree_dialog, space='  ', level=0)
        with open('output.xml', 'wb') as fh:
            tree_dialog.write(fh)

    def removeRecordChar(self):
        current_index = self.base.listWidget_Char.currentRow()
        print(current_index)
        item = self.base.listWidget_Char.item(current_index)
        if item is None:
            return
        flag = False

        question = QMessageBox.question(self, "Удалить персонажа", "Точно удалить персонажа?" + item.text(), QMessageBox.Yes | QMessageBox.No)
        if question == QMessageBox.Yes:
            for char in root_char.findall('Char'):
                ID = -100000
                if char.get('charID') != '':
                    ID = int(char.get('charID'))
                if ID == int(arr_all_id_chars[current_index]):
                    flag = True
                    root_char.remove(char)

            if flag == False:
                for char in root_char.findall('SyntheticChar'):
                    ID = -100000
                    if char.get('syntID') != '':
                        ID = int(char.get('syntID'))
                    if ID == int(arr_all_id_chars[current_index]):
                        root_char.remove(char)
            arr_all_id_chars.pop(current_index)
            removed = self.base.listWidget_Char.takeItem(self.base.listWidget_Char.currentRow())
            ET.indent(tree_char, space='  ', level=0)
            tree_char.write(res[0], encoding="utf-8")

    def openFileChar(self):
        global res
        res = QFileDialog.getOpenFileName(self, 'Open File')
        print(res)
        global tree_char
        global root_char
        if res[0] == '':
            print("AAAAAAAAAAAAA")
            msg = QMessageBox()
            msg.setText("Выбери файл")
            msg.exec_()
            return
        parser = ET.XMLParser(encoding="utf-8")
        tree_char = ET.parse(res[0], parser=parser)
        root_char = tree_char.getroot()
        output = ""
        for char in root_char.findall('Char'):
            output += "Чел [Id: " + char.get('charID')
            output += " Возраст: " + char.get('age')
            output += " Пол: " + char.find('Gender').text
            output += " Кличка: " + char.find('NickName').text
            output += " Фракция: " + char.find('Fraction').text
            self.base.listWidget_Char.addItems([output])
            output = ""
            arr_all_id_chars.append(int(char.get('charID')))
        for char in root_char.findall('SyntheticChar'):
            output += "Cинтет [Id: " + char.get('syntID')
            output += " Кличка: " + char.find('NickName').text
            output += " Фракция: " + char.find('Fraction').text
            output += " Модель: " + char.find('Model').text
            self.base.listWidget_Char.addItems([output])
            output = ""
            arr_all_id_chars.append(int(char.get('syntID')))
        global file_opened
        file_opened = True
        print(res)

    def onChangedGender(self, text):
        global gender
        gender = text

    def onChangedQuest_Man(self, text):
        global quest_person
        quest_person = text

    def onChangedQuest_robot(self, text):
        global quest_robot
        quest_robot = text

    def enterRel(self):
        rel.append(self.base.rel.text())
        self.base.rel.clear()

    def enterRobot(self):
        if file_opened == False:
            print("AAAAAAAAAAAAA")
            msg = QMessageBox()
            msg.setText("Выбери файл")
            msg.exec_()
            return
        input_id = self.base.id_robot.text()
        input_all.append(self.base.model_robot.text())
        input_all.append(self.base.fraction_robot.text())
        input_all.append(self.base.nikname_robot.text())
        input_all.append(self.base.stats_robot.text())
        input_all.append(quest_robot)
        self.cleatNotAll()
        arr_all_id_chars.append(input_id)
        what_robot = ["Model", "Fraction", "NickName", "Stats", "QuestChar"]
        output = "Cинтет [Id: " + input_id + " Кличка: " + input_all[2] + " Фракция: " + input_all[1] + " Модель: " + input_all[0] + "]"
        strtest = "<SyntheticChar>"
        for i in range(len(what_robot)):
            strtest += "<" + what_robot[i] + ">" + input_all[i] + "</" + what_robot[i] + ">"
        strtest += "</SyntheticChar>"
        self.base.listWidget_Char.addItems([output])
        str_add = ET.fromstring(strtest)
        for elem in str_add.iter('SyntheticChar'):
            elem.set('syntID', input_id)
        root_char.append(str_add)
        ET.indent(tree_char, space='  ', level=0)
        tree_char.write(res[0], encoding="utf-8")
        input_all.clear()


    def enterHuman(self):
        if file_opened == False:
            print("AAAAAAAAAAAAA")
            msg = QMessageBox()
            msg.setText("Выбери файл")
            msg.exec_()
            return
        input_age = self.base.age.text()
        input_id = self.base.id.text()
        input_all.append(gender)
        input_all.append(self.base.race.text())
        input_all.append(self.base.nationality.text())
        input_all.append(self.base.fraction.text())
        input_all.append(self.base.stats.text())
        input_all.append(self.base.surname.text())
        input_all.append(self.base.name.text())
        input_all.append(self.base.nikname.text())
        input_all.append("")
        input_all.append(self.base.adress.text())
        input_all.append(quest_person)
        self.cleatNotAll()
        arr_all_id_chars.append(input_id)
        what = ["Gender", "Race", "Nationality", "Fraction", "Stats", "SurName", "Name", "NickName",
                "Relatives", "HomeLocation", "QuestChar", ]
        output = "Чел [Id: " + input_id + " Возраст: " + input_age + " Пол: " + gender + " Кличка: " + input_all[7] + " Фракция: " + input_all[3] + "]"
        strtest = "<Char>"
        for i in range(len(what)):
            if what[i] != 'Relatives':
                strtest += "<" + what[i] + ">" + input_all[i] + "</" + what[i] + ">"
            else:
                strtest += "<" + what[i] + ">"
                for j in range(len(rel)):
                    strtest += "<rel>" + rel[j] + "</rel>"

                strtest += "</" + what[i] + "> "
        strtest += "</Char>"
        self.base.listWidget_Char.addItems([output])
        rel.clear()
        str_add = ET.fromstring(strtest)
        for elem in str_add.iter('Char'):
            elem.set('charID', input_id)
            elem.set('age', input_age)
        root_char.append(str_add)
        ET.indent(tree_char, space='  ', level=0)
        tree_char.write(res[0], encoding="utf-8")
        input_all.clear()
        #self.base.save_all.setVisible(False)


    def cleatNotAll(self):
        self.base.age.clear()
        self.base.id.clear()
        self.base.surname.clear()
        self.base.name.clear()
        self.base.nikname.clear()
        self.base.adress.clear()
        self.base.nikname_robot.clear()
        self.base.stats_robot.clear()
        self.base.stats.clear()

    def clearAll(self):
        self.base.age.clear()
        self.base.id.clear()
        self.base.nationality.clear()
        self.base.fraction.clear()
        self.base.stats.clear()
        self.base.surname.clear()
        self.base.name.clear()
        self.base.nikname.clear()
        self.base.race.clear()
        self.base.adress.clear()
        self.base.model_robot.clear()
        self.base.fraction_robot.clear()
        self.base.nikname_robot.clear()
        self.base.stats_robot.clear()





app = QtWidgets.QApplication(sys.argv)
application = Xml_perevod()
application.show()
sys.exit(app.exec_())
