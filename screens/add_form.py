from PyQt5 import QtCore, QtWidgets

import database.db as db
import services
from screens.ui.add_form_ui import WishDialog


class WishForm(QtWidgets.QWidget, WishDialog):
    """ Обработка интерактивных элементов окна добавления желания в список """

    switch_to_main = QtCore.pyqtSignal(str)

    def __init__(self, username=None):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.username = username

        self.add_btn.clicked.connect(self.add_click)

    def get_wish_data(self):
        wish_data = dict([
            ('wish_name', (self.name_line_edit.text(), 50)),
            ('wish_link', (self.link_line_edit.text(), 80)),
            ('wish_description', (self.description_txt.toPlainText(), 50))
        ])
        return wish_data

    def add_click(self):
        wish_data = self.get_wish_data()
        adding_item = services.create_wish(wish_data)
        if adding_item['status']:
            print(self.username)
            print(wish_data['wish_name'])
            print(wish_data['wish_link'])
            print(wish_data['wish_description'])
            db.add_wish(
                self.username,
                wish_data['wish_name'][0],
                wish_data['wish_link'][0],
                wish_data['wish_description'][0]
            )

            QtWidgets.QMessageBox.information(
                self, 'Информация',
                adding_item['message'], QtWidgets.QMessageBox.Ok
            )
            self.switch_to_main.emit(self.username)         
        else:
            QtWidgets.QMessageBox.critical(
                self, 'Ошибка', 
                adding_item['message'], QtWidgets.QMessageBox.Ok
            )
            