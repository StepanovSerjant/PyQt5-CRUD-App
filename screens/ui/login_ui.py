# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5 import QtCore, QtGui, QtWidgets

from settings import STYLE_DIR


class LoginDialog(object):
    """ Сеттинг окна авторизации """
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(705, 366)

        Dialog.setStyleSheet(open(os.path.join(STYLE_DIR, 'login_screen.css')).read())

        self.username_lbl = QtWidgets.QLabel(Dialog)
        self.username_lbl.setGeometry(QtCore.QRect(210, 139, 123, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.username_lbl.setFont(font)
        self.username_lbl.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.username_lbl.setObjectName("username_lbl")
        self.password_lbl = QtWidgets.QLabel(Dialog)
        self.password_lbl.setGeometry(QtCore.QRect(210, 189, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.password_lbl.setFont(font)
        self.password_lbl.setObjectName("password_lbl")
        self.name_line_edit = QtWidgets.QLineEdit(Dialog)
        self.name_line_edit.setGeometry(QtCore.QRect(350, 139, 171, 31))
        self.name_line_edit.setDragEnabled(False)
        self.name_line_edit.setObjectName("name_line_edit")
        self.pass_line_edit = QtWidgets.QLineEdit(Dialog)
        self.pass_line_edit.setGeometry(QtCore.QRect(350, 190, 171, 31))
        self.pass_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_line_edit.setObjectName("pass_line_edit")
        """ Кнопка войти """
        self.login_btn = QtWidgets.QPushButton(Dialog)
        self.login_btn.setGeometry(QtCore.QRect(240, 270, 111, 31))
        self.login_btn.setObjectName("login_btn")
        """ Кнопка регистрации """
        self.sign_up_btn = QtWidgets.QPushButton(Dialog)
        self.sign_up_btn.setGeometry(QtCore.QRect(390, 270, 111, 31))
        self.sign_up_btn.setObjectName("sign_up_btn")

        self.list_title_lbl = QtWidgets.QLabel(Dialog)
        self.list_title_lbl.setGeometry(QtCore.QRect(120, 20, 491, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.list_title_lbl.setFont(font)
        self.list_title_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.list_title_lbl.setObjectName("list_title_lbl")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Wish App"))
        self.username_lbl.setText(_translate("Dialog", "Username"))
        self.password_lbl.setText(_translate("Dialog", "Password"))
        self.login_btn.setText(_translate("Dialog", "Login"))
        self.sign_up_btn.setText(_translate("Dialog", "Sign Up"))
        self.list_title_lbl.setText(_translate("Dialog", "WISH APP"))
