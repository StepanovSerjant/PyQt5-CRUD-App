# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_with_table_2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5 import QtCore, QtGui, QtWidgets

from settings import STYLE_DIR


class MainDialog(object):
    """ Сеттинг главного окна """
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(831, 559)
        self.table_view = QtWidgets.QTableView(Dialog)
        self.table_view.setGeometry(QtCore.QRect(40, 140, 601, 381))
        self.table_view.setFrameShape(QtWidgets.QFrame.Panel)
        self.table_view.setFrameShadow(QtWidgets.QFrame.Plain)
        self.table_view.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_view.setObjectName("table_view")

        Dialog.setStyleSheet(open(os.path.join(STYLE_DIR, 'main_screen.css')).read())

        self.add_btn = QtWidgets.QPushButton(Dialog)
        self.add_btn.setGeometry(QtCore.QRect(670, 140, 131, 31))
        self.add_btn.setObjectName("add_btn")
        self.remove_btn = QtWidgets.QPushButton(Dialog)
        self.remove_btn.setGeometry(QtCore.QRect(670, 190, 131, 31))
        self.remove_btn.setObjectName("remove_btn")
        self.header_lbl = QtWidgets.QLabel(Dialog)
        self.header_lbl.setGeometry(QtCore.QRect(160, 90, 381, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.header_lbl.setFont(font)
        self.header_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.header_lbl.setObjectName("header_lbl")
        self.logout_btn = QtWidgets.QPushButton(Dialog)
        self.logout_btn.setGeometry(QtCore.QRect(670, 30, 131, 31))
        self.logout_btn.setObjectName("logout_btn")
        self.username_lbl = QtWidgets.QLabel(Dialog)
        self.username_lbl.setGeometry(QtCore.QRect(10, 30, 111, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.username_lbl.setFont(font)
        self.username_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.username_lbl.setObjectName("username_lbl")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Wish App"))
        self.add_btn.setText(_translate("Dialog", "Add"))
        self.remove_btn.setText(_translate("Dialog", "Remove"))
        self.header_lbl.setText(_translate("Dialog", "WISH LIST"))
        self.logout_btn.setText(_translate("Dialog", "Log out"))
        self.username_lbl.setText(_translate("Dialog", "User"))
