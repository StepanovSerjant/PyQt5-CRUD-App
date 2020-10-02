# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5 import QtCore, QtGui, QtWidgets

from settings import STYLE_DIR


class RegisterDialog(object):
    """ Сеттинг окна регистрации """
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(578, 419)
        
        Dialog.setStyleSheet(open(os.path.join(STYLE_DIR, 'register_screen.css')).read())

        self.header_lbl = QtWidgets.QLabel(Dialog)
        self.header_lbl.setGeometry(QtCore.QRect(120, -10, 351, 111))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.header_lbl.setFont(font)
        self.header_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.header_lbl.setObjectName("label") 

        self.username_lbl = QtWidgets.QLabel(Dialog)
        self.username_lbl.setGeometry(QtCore.QRect(140, 120, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.username_lbl.setFont(font)
        self.username_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.username_lbl.setObjectName("username_lbl")

        self.password_lbl = QtWidgets.QLabel(Dialog)
        self.password_lbl.setGeometry(QtCore.QRect(130, 170, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.password_lbl.setFont(font)
        self.password_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.password_lbl.setObjectName("password_lbl")

        self.email_lbl = QtWidgets.QLabel(Dialog)
        self.email_lbl.setGeometry(QtCore.QRect(110, 270, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.email_lbl.setFont(font)
        self.email_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.email_lbl.setObjectName("email_lbl")

        self.name_line_edit = QtWidgets.QLineEdit(Dialog)
        self.name_line_edit.setGeometry(QtCore.QRect(300, 120, 161, 31))
        self.name_line_edit.setObjectName("name_line_edit")

        self.sign_up_btn = QtWidgets.QPushButton(Dialog)
        self.sign_up_btn.setGeometry(QtCore.QRect(240, 340, 121, 31))
        self.sign_up_btn.setObjectName("sign_up_btn")

        self.pass_2_lbl = QtWidgets.QLabel(Dialog)
        self.pass_2_lbl.setGeometry(QtCore.QRect(140, 220, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pass_2_lbl.setFont(font)
        self.pass_2_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_2_lbl.setObjectName("pass_2_lbl")

        self.pass_line_edit = QtWidgets.QLineEdit(Dialog)
        self.pass_line_edit.setGeometry(QtCore.QRect(300, 170, 161, 31))
        self.pass_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_line_edit.setObjectName("pass_line_edit")

        self.email_line_edit = QtWidgets.QLineEdit(Dialog)
        self.email_line_edit.setGeometry(QtCore.QRect(300, 270, 161, 31))
        self.email_line_edit.setObjectName("email_line_edit")
        
        self.pass2_line_edit = QtWidgets.QLineEdit(Dialog)
        self.pass2_line_edit.setGeometry(QtCore.QRect(300, 220, 161, 31))
        self.pass2_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass2_line_edit.setObjectName("pass2_line_edit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Wish App"))
        self.header_lbl.setText(_translate("Dialog", "Create an account"))
        self.username_lbl.setText(_translate("Dialog", "Username"))
        self.password_lbl.setText(_translate("Dialog", "Password"))
        self.email_lbl.setText(_translate("Dialog", "Email"))
        self.sign_up_btn.setText(_translate("Dialog", "Register"))
        self.pass_2_lbl.setText(_translate("Dialog", "Password"))
