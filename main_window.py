# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(996, 847)
        MainWindow.setMaximumSize(QtCore.QSize(996, 847))
        MainWindow.setStyleSheet("background-color: #22222e;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QComboBox{\n"
"border: 2px solid #f66867;\n"
"color: white;\n"
"background-color: #22222e;\n"
"}\n"
"\n"
"QListView{\n"
"    border:       none;\n"
"    color:                     white;\n"
"    font-weight:            bold;\n"
"    selection-background-color: rgb(34, 34, 46); \n"
"    show-decoration-selected: 1;\n"
"    margin-left: -10px;\n"
"    padding-bottom: 6px;\n"
"    padding-left    :           15px;\n"
"    padding-top    :           3px;\n"
"    background-color:  rgb(42, 42, 57);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(88, 88, 88);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(177, 64, 66);\n"
"    \n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.weight = QtWidgets.QLineEdit(self.centralwidget)
        self.weight.setEnabled(True)
        self.weight.setGeometry(QtCore.QRect(50, 190, 349, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.weight.setFont(font)
        self.weight.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 30;\n"
"color: white;")
        self.weight.setAlignment(QtCore.Qt.AlignCenter)
        self.weight.setObjectName("weight")
        self.height = QtWidgets.QLineEdit(self.centralwidget)
        self.height.setEnabled(True)
        self.height.setGeometry(QtCore.QRect(50, 310, 349, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.height.setFont(font)
        self.height.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 30;\n"
"color: white;")
        self.height.setAlignment(QtCore.Qt.AlignCenter)
        self.height.setObjectName("height")
        self.age = QtWidgets.QLineEdit(self.centralwidget)
        self.age.setEnabled(True)
        self.age.setGeometry(QtCore.QRect(50, 430, 349, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.age.setFont(font)
        self.age.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 30;\n"
"color: white;")
        self.age.setAlignment(QtCore.Qt.AlignCenter)
        self.age.setObjectName("age")
        self.output_calories = QtWidgets.QLineEdit(self.centralwidget)
        self.output_calories.setEnabled(True)
        self.output_calories.setGeometry(QtCore.QRect(500, 360, 349, 60))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.output_calories.setFont(font)
        self.output_calories.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"color: white;")
        self.output_calories.setAlignment(QtCore.Qt.AlignCenter)
        self.output_calories.setObjectName("output_calories")
        self.kcal_label = QtWidgets.QLabel(self.centralwidget)
        self.kcal_label.setGeometry(QtCore.QRect(500, 300, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.kcal_label.setFont(font)
        self.kcal_label.setStyleSheet("color: white;\n"
"")
        self.kcal_label.setObjectName("kcal_label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 3621, 141))
        self.frame.setStyleSheet("background-color: #fb5b5d;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.titile = QtWidgets.QLabel(self.frame)
        self.titile.setGeometry(QtCore.QRect(140, 40, 711, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.titile.setFont(font)
        self.titile.setStyleSheet("color: white;\n"
"")
        self.titile.setObjectName("titile")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(500, 480, 349, 60))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.start_button.setFont(font)
        self.start_button.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: #fb5b5d;\n"
"    border-radius: 30;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(226, 82, 84);\n"
"    \n"
"}  \n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(177, 64, 66);\n"
"    \n"
"}\n"
"\n"
"\n"
"")
        self.start_button.setObjectName("start_button")
        self.sex = QtWidgets.QComboBox(self.centralwidget)
        self.sex.setGeometry(QtCore.QRect(48, 570, 331, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.sex.setFont(font)
        self.sex.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sex.setStyleSheet("")
        self.sex.setEditable(False)
        self.sex.setObjectName("sex")
        self.sex.addItem("")
        self.sex.addItem("")
        self.sex.addItem("")
        self.sex.addItem("")
        self.activity = QtWidgets.QComboBox(self.centralwidget)
        self.activity.setGeometry(QtCore.QRect(50, 710, 661, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.activity.setFont(font)
        self.activity.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.activity.setStyleSheet("")
        self.activity.setEditable(False)
        self.activity.setObjectName("activity")
        self.activity.addItem("")
        self.activity.addItem("")
        self.activity.addItem("")
        self.activity.addItem("")
        self.activity.addItem("")
        self.activity.addItem("")
        self.kcal_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.kcal_label_2.setGeometry(QtCore.QRect(50, 540, 321, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.kcal_label_2.setFont(font)
        self.kcal_label_2.setStyleSheet("color: white;\n"
"")
        self.kcal_label_2.setObjectName("kcal_label_2")
        self.kcal_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.kcal_label_3.setGeometry(QtCore.QRect(50, 680, 321, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.kcal_label_3.setFont(font)
        self.kcal_label_3.setStyleSheet("color: white;\n"
"")
        self.kcal_label_3.setObjectName("kcal_label_3")
        self.diet_button = QtWidgets.QPushButton(self.centralwidget)
        self.diet_button.setGeometry(QtCore.QRect(500, 580, 349, 60))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.diet_button.setFont(font)
        self.diet_button.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color: #636363;\n"
"border-radius: 30;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(88, 88, 88);\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgb(72, 72, 72);\n"
"    \n"
"}\n"
"\n"
"")
        self.diet_button.setObjectName("diet_button")
        self.prompt = QtWidgets.QLabel(self.centralwidget)
        self.prompt.setGeometry(QtCore.QRect(460, 150, 261, 141))
        font = QtGui.QFont()
        font.setFamily("Viner Hand ITC")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.prompt.setFont(font)
        self.prompt.setStyleSheet("color: white;\n"
"")
        self.prompt.setText("")
        self.prompt.setPixmap(QtGui.QPixmap("prompt.png"))
        self.prompt.setObjectName("prompt")
        self.error_sex = QtWidgets.QLabel(self.centralwidget)
        self.error_sex.setGeometry(QtCore.QRect(400, 570, 41, 71))
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(73)
        self.error_sex.setFont(font)
        self.error_sex.setStyleSheet("color: rgb(255, 255, 255);")
        self.error_sex.setObjectName("error_sex")
        self.error_activity = QtWidgets.QLabel(self.centralwidget)
        self.error_activity.setGeometry(QtCore.QRect(730, 710, 41, 71))
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(73)
        self.error_activity.setFont(font)
        self.error_activity.setStyleSheet("color: rgb(255, 255, 255);")
        self.error_activity.setObjectName("error_activity")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.kcal_label.setText(_translate("MainWindow", "КОЛИЧЕСТВО ККАЛ:"))
        self.titile.setText(_translate("MainWindow", "ПОДСЧЕТ ДНЕВНОЙ НОРМЫ ККАЛ"))
        self.start_button.setText(_translate("MainWindow", "Сосчитать"))
        self.sex.setItemText(0, _translate("MainWindow", "- Не указано -"))
        self.sex.setItemText(1, _translate("MainWindow", "Мужчина"))
        self.sex.setItemText(2, _translate("MainWindow", "Женщина"))
        self.sex.setItemText(3, _translate("MainWindow", "Боевой вертолет"))
        self.activity.setItemText(0, _translate("MainWindow", "- Не указано -"))
        self.activity.setItemText(1, _translate("MainWindow", "Нет нагрузки и сидячий образ жизни"))
        self.activity.setItemText(2, _translate("MainWindow", "Небольшие пробежки или легкая гимнастика 1-3 раза в неделю"))
        self.activity.setItemText(3, _translate("MainWindow", "Спорт со средними нагрузками 3-5 раз в неделю"))
        self.activity.setItemText(4, _translate("MainWindow", "Полноценные тренировки 6-7 раз в неделю"))
        self.activity.setItemText(5, _translate("MainWindow", "Ваша работа связана с физ.трудом, тренировки 2 раза в день"))
        self.kcal_label_2.setText(_translate("MainWindow", "Пол:"))
        self.kcal_label_3.setText(_translate("MainWindow", "Активность:"))
        self.diet_button.setText(_translate("MainWindow", "Рекомендованное меню"))
        self.error_sex.setText(_translate("MainWindow", "!"))
        self.error_activity.setText(_translate("MainWindow", "!"))