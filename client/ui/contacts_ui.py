# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contacts.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_ContactsWindow(object):
    def retranslateUi(self, ContactsWindow):
        _translate = QtCore.QCoreApplication.translate
        ContactsWindow.setWindowTitle(_translate("ContactsWindow", "Мої Контакти"))
        self.label.setText(_translate("ContactsWindow",
                                      "<html><head/><body><p><span style=\"color: #FF0000;\">Всі Контакти</span></p></body></html>"))  # Изменен цвет
        self.add_new_contact_btn.setText(_translate("ContactsWindow", "Додати Новий Контакт"))
        self.delete_contact_btn.setText(_translate("ContactsWindow", "Видалити Контакт"))

    def setupUi(self, ContactsWindow):
        ContactsWindow.setObjectName("ContactsWindow")
        ContactsWindow.resize(400, 600)  # Изменен размер

        # Central Widget
        self.centralwidget = QtWidgets.QWidget(ContactsWindow)
        self.centralwidget.setObjectName("centralwidget")
        ContactsWindow.setCentralWidget(self.centralwidget)

        # Grid Layout
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # Vertical Layout
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        # Horizontal Layout for the title label
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setStyleSheet("font-size: 20pt; font-weight: bold; color: blue;")  # Изменен шрифт и цвет
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)

        # All Contacts List Widget
        self.all_contacts = QtWidgets.QListWidget(self.centralwidget)
        self.all_contacts.setObjectName("all_contacts")
        self.verticalLayout.addWidget(self.all_contacts)

        # Horizontal Layout for the new contact input and button
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.new_contact_name = QtWidgets.QLineEdit(self.centralwidget)
        self.new_contact_name.setObjectName("new_contact_name")
        self.horizontalLayout_2.addWidget(self.new_contact_name)
        self.add_new_contact_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_new_contact_btn.setObjectName("add_new_contact_btn")
        self.horizontalLayout_2.addWidget(self.add_new_contact_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        # Delete Contact Button
        self.delete_contact_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_contact_btn.setObjectName("delete_contact_btn")
        self.verticalLayout.addWidget(self.delete_contact_btn)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        # Menubar
        self.menubar = QtWidgets.QMenuBar(ContactsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))  # Изменен размер
        self.menubar.setObjectName("menubar")
        ContactsWindow.setMenuBar(self.menubar)

        # Statusbar
        self.statusbar = QtWidgets.QStatusBar(ContactsWindow)
        self.statusbar.setObjectName("statusbar")
        ContactsWindow.setStatusBar(self.statusbar)

        # Menu and Action
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.actionExit = QtWidgets.QAction(ContactsWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(ContactsWindow)
        QtCore.QMetaObject.connectSlotsByName(ContactsWindow)


