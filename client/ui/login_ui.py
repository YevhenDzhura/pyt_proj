# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Login_Dialog(object):
    def setupUi(self, Login_Dialog):
        Login_Dialog.setObjectName("Login_Dialog")
        Login_Dialog.resize(400, 300)  # Измененный размер

        # Grid Layout
        self.gridLayout = QtWidgets.QGridLayout(Login_Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(50, 50, 50, 50)  # Добавленные отступы

        # Vertical Layout
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        # Horizontal Layout for the username field
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.username_label = QtWidgets.QLabel(Login_Dialog)
        self.username_label.setObjectName("username_label")
        self.username_label.setStyleSheet("font-size: 14pt; font-weight: bold;")  # Измененный шрифт
        self.horizontalLayout.addWidget(self.username_label)
        self.username_text = QtWidgets.QLineEdit(Login_Dialog)
        self.username_text.setObjectName("username_text")
        self.horizontalLayout.addWidget(self.username_text)
        self.verticalLayout.addLayout(self.horizontalLayout)

        # Horizontal Layout for the password field
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.password_label = QtWidgets.QLabel(Login_Dialog)
        self.password_label.setObjectName("password_label")
        self.password_label.setStyleSheet("font-size: 14pt; font-weight: bold;")  # Измененный шрифт
        self.horizontalLayout_2.addWidget(self.password_label)
        self.password_text = QtWidgets.QLineEdit(Login_Dialog)
        self.password_text.setObjectName("password_text")
        self.horizontalLayout_2.addWidget(self.password_text)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        # Horizontal Layout for the login button
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 20, 0, 0)  # Добавленные отступы
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.login_btn = QtWidgets.QPushButton(Login_Dialog)
        self.login_btn.setObjectName("login_btn")
        self.login_btn.setStyleSheet(
            "font-size: 12pt; font-weight: bold; background-color: #FF0000; color: white;")  # Измененный шрифт, цвет и фон
        self.horizontalLayout_3.addWidget(self.login_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        Login_Dialog.setStyleSheet("background-color: #FFFF00;")  # Измененный цвет фона

        self.retranslateUi(Login_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Login_Dialog)

    def retranslateUi(self, Login_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Login_Dialog.setWindowTitle(_translate("Login_Dialog", "Вікно входу"))
        self.username_label.setText(_translate("Login_Dialog", "Ім'я користувача"))
        self.password_label.setText(_translate("Login_Dialog", "Пароль"))
        self.login_btn.setText(_translate("Login_Dialog", "Увійти"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Login_Dialog = QtWidgets.QDialog()
    ui = Ui_Login_Dialog()
    ui.setupUi(Login_Dialog)
    Login_Dialog.show()
    sys.exit(app.exec_())

