# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adding_item.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5 import QtCore, QtGui, QtWidgets

from settings import STYLE_DIR


class WishDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(501, 404)
        self.header_lbl = QtWidgets.QLabel(Dialog)
        self.header_lbl.setGeometry(QtCore.QRect(150, 0, 211, 91))

        Dialog.setStyleSheet(open(os.path.join(STYLE_DIR, 'adding_screen.css')).read())

        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.header_lbl.setFont(font)
        self.header_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.header_lbl.setObjectName("header_lbl")
        self.name_lbl = QtWidgets.QLabel(Dialog)
        self.name_lbl.setGeometry(QtCore.QRect(60, 100, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.name_lbl.setFont(font)
        self.name_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.name_lbl.setObjectName("name_lbl")
        self.link_lbl = QtWidgets.QLabel(Dialog)
        self.link_lbl.setGeometry(QtCore.QRect(60, 150, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.link_lbl.setFont(font)
        self.link_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.link_lbl.setObjectName("link_lbl")
        self.description_lbl = QtWidgets.QLabel(Dialog)
        self.description_lbl.setGeometry(QtCore.QRect(60, 200, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.description_lbl.setFont(font)
        self.description_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.description_lbl.setObjectName("description_lbl")
        self.description_txt = QtWidgets.QTextEdit(Dialog)
        self.description_txt.setGeometry(QtCore.QRect(220, 200, 211, 121))
        self.description_txt.setObjectName("description_txt")
        self.name_line_edit = QtWidgets.QLineEdit(Dialog)
        self.name_line_edit.setGeometry(QtCore.QRect(220, 100, 211, 31))
        self.name_line_edit.setDragEnabled(False)
        self.name_line_edit.setObjectName("name_line_edit")
        self.link_line_edit = QtWidgets.QLineEdit(Dialog)
        self.link_line_edit.setGeometry(QtCore.QRect(220, 150, 211, 31))
        self.link_line_edit.setDragEnabled(False)
        self.link_line_edit.setObjectName("link_line_edit")
        self.add_btn = QtWidgets.QPushButton(Dialog)
        self.add_btn.setGeometry(QtCore.QRect(200, 350, 111, 31))
        self.add_btn.setObjectName("add_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Wish App"))
        self.header_lbl.setText(_translate("Dialog", "ADD"))
        self.name_lbl.setText(_translate("Dialog", "Название"))
        self.link_lbl.setText(_translate("Dialog", "Ссылка"))
        self.description_lbl.setText(_translate("Dialog", "Описание"))
        self.add_btn.setText(_translate("Dialog", "Add"))
