# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testall.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 689)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Chars = QtWidgets.QTabWidget(self.centralwidget)
        self.Chars.setGeometry(QtCore.QRect(0, 20, 671, 621))
        self.Chars.setObjectName("Chars")
        self.Human = QtWidgets.QWidget()
        self.Human.setObjectName("Human")
        self.comboQuest = QtWidgets.QComboBox(self.Human)
        self.comboQuest.setGeometry(QtCore.QRect(120, 530, 69, 22))
        self.comboQuest.setObjectName("comboQuest")
        self.comboQuest.addItem("")
        self.comboQuest.addItem("")
        self.age = QtWidgets.QLineEdit(self.Human)
        self.age.setGeometry(QtCore.QRect(90, 70, 61, 41))
        self.age.setText("")
        self.age.setObjectName("age")
        self.nationality = QtWidgets.QLineEdit(self.Human)
        self.nationality.setGeometry(QtCore.QRect(120, 240, 531, 31))
        self.nationality.setObjectName("nationality")
        self.Id = QtWidgets.QLabel(self.Human)
        self.Id.setGeometry(QtCore.QRect(180, 80, 21, 21))
        self.Id.setObjectName("Id")
        self.label_nikname = QtWidgets.QLabel(self.Human)
        self.label_nikname.setGeometry(QtCore.QRect(20, 440, 41, 31))
        self.label_nikname.setObjectName("label_nikname")
        self.race = QtWidgets.QLineEdit(self.Human)
        self.race.setGeometry(QtCore.QRect(120, 200, 531, 31))
        self.race.setObjectName("race")
        self.label_gender = QtWidgets.QLabel(self.Human)
        self.label_gender.setGeometry(QtCore.QRect(20, 160, 47, 13))
        self.label_gender.setObjectName("label_gender")
        self.Age = QtWidgets.QLabel(self.Human)
        self.Age.setGeometry(QtCore.QRect(30, 80, 47, 13))
        self.Age.setObjectName("Age")
        self.label_adress = QtWidgets.QLabel(self.Human)
        self.label_adress.setGeometry(QtCore.QRect(20, 490, 47, 13))
        self.label_adress.setObjectName("label_adress")
        self.label_name = QtWidgets.QLabel(self.Human)
        self.label_name.setGeometry(QtCore.QRect(20, 410, 47, 13))
        self.label_name.setObjectName("label_name")
        self.label_nationality = QtWidgets.QLabel(self.Human)
        self.label_nationality.setGeometry(QtCore.QRect(20, 250, 91, 16))
        self.label_nationality.setObjectName("label_nationality")
        self.label_stats = QtWidgets.QLabel(self.Human)
        self.label_stats.setGeometry(QtCore.QRect(20, 330, 47, 13))
        self.label_stats.setObjectName("label_stats")
        self.surname = QtWidgets.QLineEdit(self.Human)
        self.surname.setGeometry(QtCore.QRect(120, 360, 531, 31))
        self.surname.setObjectName("surname")
        self.stats = QtWidgets.QLineEdit(self.Human)
        self.stats.setGeometry(QtCore.QRect(120, 320, 531, 31))
        self.stats.setObjectName("stats")
        self.label_fraction = QtWidgets.QLabel(self.Human)
        self.label_fraction.setGeometry(QtCore.QRect(20, 290, 47, 13))
        self.label_fraction.setObjectName("label_fraction")
        self.comboGenger = QtWidgets.QComboBox(self.Human)
        self.comboGenger.setGeometry(QtCore.QRect(120, 150, 51, 22))
        self.comboGenger.setObjectName("comboGenger")
        self.comboGenger.addItem("")
        self.comboGenger.addItem("")
        self.id = QtWidgets.QLineEdit(self.Human)
        self.id.setGeometry(QtCore.QRect(200, 70, 61, 41))
        self.id.setText("")
        self.id.setObjectName("id")
        self.label_surname = QtWidgets.QLabel(self.Human)
        self.label_surname.setGeometry(QtCore.QRect(20, 370, 47, 13))
        self.label_surname.setObjectName("label_surname")
        self.adress = QtWidgets.QLineEdit(self.Human)
        self.adress.setGeometry(QtCore.QRect(120, 480, 531, 31))
        self.adress.setObjectName("adress")
        self.fraction = QtWidgets.QLineEdit(self.Human)
        self.fraction.setGeometry(QtCore.QRect(120, 280, 531, 31))
        self.fraction.setObjectName("fraction")
        self.save_all = QtWidgets.QPushButton(self.Human)
        self.save_all.setGeometry(QtCore.QRect(360, 520, 161, 71))
        self.save_all.setObjectName("save_all")
        self.Rel_1 = QtWidgets.QLabel(self.Human)
        self.Rel_1.setGeometry(QtCore.QRect(280, 70, 231, 31))
        self.Rel_1.setObjectName("Rel_1")
        self.nikname = QtWidgets.QLineEdit(self.Human)
        self.nikname.setGeometry(QtCore.QRect(120, 440, 531, 31))
        self.nikname.setObjectName("nikname")
        self.rel = QtWidgets.QLineEdit(self.Human)
        self.rel.setGeometry(QtCore.QRect(480, 70, 61, 41))
        self.rel.setObjectName("rel")
        self.name = QtWidgets.QLineEdit(self.Human)
        self.name.setGeometry(QtCore.QRect(120, 400, 531, 31))
        self.name.setObjectName("name")
        self.CharLabel = QtWidgets.QLabel(self.Human)
        self.CharLabel.setGeometry(QtCore.QRect(20, 20, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.CharLabel.setFont(font)
        self.CharLabel.setObjectName("CharLabel")
        self.label_quest = QtWidgets.QLabel(self.Human)
        self.label_quest.setGeometry(QtCore.QRect(20, 530, 47, 13))
        self.label_quest.setObjectName("label_quest")
        self.label_race = QtWidgets.QLabel(self.Human)
        self.label_race.setGeometry(QtCore.QRect(20, 210, 41, 16))
        self.label_race.setObjectName("label_race")
        self.save_rel = QtWidgets.QPushButton(self.Human)
        self.save_rel.setGeometry(QtCore.QRect(410, 130, 91, 61))
        self.save_rel.setObjectName("save_rel")
        self.Chars.addTab(self.Human, "")
        self.Robot = QtWidgets.QWidget()
        self.Robot.setObjectName("Robot")
        self.RobotLabel = QtWidgets.QLabel(self.Robot)
        self.RobotLabel.setGeometry(QtCore.QRect(30, 20, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.RobotLabel.setFont(font)
        self.RobotLabel.setObjectName("RobotLabel")
        self.label_fraction_robot = QtWidgets.QLabel(self.Robot)
        self.label_fraction_robot.setGeometry(QtCore.QRect(20, 130, 47, 13))
        self.label_fraction_robot.setObjectName("label_fraction_robot")
        self.label_model_robot = QtWidgets.QLabel(self.Robot)
        self.label_model_robot.setGeometry(QtCore.QRect(20, 90, 51, 20))
        self.label_model_robot.setObjectName("label_model_robot")
        self.label_nikname_robot = QtWidgets.QLabel(self.Robot)
        self.label_nikname_robot.setGeometry(QtCore.QRect(20, 160, 51, 31))
        self.label_nikname_robot.setObjectName("label_nikname_robot")
        self.label_stats_robot = QtWidgets.QLabel(self.Robot)
        self.label_stats_robot.setGeometry(QtCore.QRect(20, 210, 47, 13))
        self.label_stats_robot.setObjectName("label_stats_robot")
        self.label_quest_robot = QtWidgets.QLabel(self.Robot)
        self.label_quest_robot.setGeometry(QtCore.QRect(20, 250, 47, 13))
        self.label_quest_robot.setObjectName("label_quest_robot")
        self.model_robot = QtWidgets.QLineEdit(self.Robot)
        self.model_robot.setGeometry(QtCore.QRect(80, 80, 531, 31))
        self.model_robot.setObjectName("model_robot")
        self.comboQuest_robot = QtWidgets.QComboBox(self.Robot)
        self.comboQuest_robot.setGeometry(QtCore.QRect(80, 240, 69, 22))
        self.comboQuest_robot.setObjectName("comboQuest_robot")
        self.comboQuest_robot.addItem("")
        self.comboQuest_robot.addItem("")
        self.nikname_robot = QtWidgets.QLineEdit(self.Robot)
        self.nikname_robot.setGeometry(QtCore.QRect(80, 160, 531, 31))
        self.nikname_robot.setObjectName("nikname_robot")
        self.stats_robot = QtWidgets.QLineEdit(self.Robot)
        self.stats_robot.setGeometry(QtCore.QRect(80, 200, 531, 31))
        self.stats_robot.setObjectName("stats_robot")
        self.fraction_robot = QtWidgets.QLineEdit(self.Robot)
        self.fraction_robot.setGeometry(QtCore.QRect(80, 120, 531, 31))
        self.fraction_robot.setObjectName("fraction_robot")
        self.save_all_robot = QtWidgets.QPushButton(self.Robot)
        self.save_all_robot.setGeometry(QtCore.QRect(230, 250, 161, 71))
        self.save_all_robot.setObjectName("save_all_robot")
        self.Chars.addTab(self.Robot, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 688, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Chars.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboQuest.setItemText(0, _translate("MainWindow", "true"))
        self.comboQuest.setItemText(1, _translate("MainWindow", "false"))
        self.Id.setText(_translate("MainWindow", "Id"))
        self.label_nikname.setText(_translate("MainWindow", "Никнейм"))
        self.label_gender.setText(_translate("MainWindow", "Гендер"))
        self.Age.setText(_translate("MainWindow", "Возраст"))
        self.label_adress.setText(_translate("MainWindow", "Дом"))
        self.label_name.setText(_translate("MainWindow", "Имя"))
        self.label_nationality.setText(_translate("MainWindow", "Национальность"))
        self.label_stats.setText(_translate("MainWindow", "Статы"))
        self.label_fraction.setText(_translate("MainWindow", "Фракция"))
        self.comboGenger.setItemText(0, _translate("MainWindow", "М"))
        self.comboGenger.setItemText(1, _translate("MainWindow", "Ж"))
        self.label_surname.setText(_translate("MainWindow", "Фамилия"))
        self.save_all.setText(_translate("MainWindow", "Сохранить"))
        self.Rel_1.setText(_translate("MainWindow", "Вводите rel по 1, нажимая сохранить"))
        self.CharLabel.setText(_translate("MainWindow", "Живой персонаж"))
        self.label_quest.setText(_translate("MainWindow", "Квест"))
        self.label_race.setText(_translate("MainWindow", "Раса"))
        self.save_rel.setText(_translate("MainWindow", "Сохранить rel"))
        self.Chars.setTabText(self.Chars.indexOf(self.Human), _translate("MainWindow", "Человек"))
        self.RobotLabel.setText(_translate("MainWindow", "Синтет"))
        self.label_fraction_robot.setText(_translate("MainWindow", "Фракция"))
        self.label_model_robot.setText(_translate("MainWindow", "Модель"))
        self.label_nikname_robot.setText(_translate("MainWindow", "Никнейм"))
        self.label_stats_robot.setText(_translate("MainWindow", "Статы"))
        self.label_quest_robot.setText(_translate("MainWindow", "Квест"))
        self.comboQuest_robot.setItemText(0, _translate("MainWindow", "true"))
        self.comboQuest_robot.setItemText(1, _translate("MainWindow", "false"))
        self.save_all_robot.setText(_translate("MainWindow", "Сохранить"))
        self.Chars.setTabText(self.Chars.indexOf(self.Robot), _translate("MainWindow", "Синтет"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())