from PyQt5 import QtCore, QtWidgets

import database.db as db
import services
from screens.ui.register_ui import RegisterDialog


class Register(QtWidgets.QWidget, RegisterDialog):
    """ Обработка интерактивных элементов окна регистрации """

    switch_to_login = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        
        self.sign_up_btn.clicked.connect(self.sign_up_click)

    def get_data(self):
        """ Функция получения данных из полей регистрации """
        register_data = dict([
            ('username', (self.name_line_edit.text(), 50)),
            ('pass', (self.pass_line_edit.text(), 25)),
            ('pass_confirm', self.pass2_line_edit.text()),
            ('email', (self.email_line_edit.text(), 25))
        ])
        return register_data
    
    def sign_up_click(self):
        """ Функция обработки нажатия кнопки sign up """
        register_data = self.get_data()
        user_register = services.user_registration(register_data)
        if user_register['status']:
            QtWidgets.QMessageBox.information(
                self, 'Информация',
                user_register['message'], QtWidgets.QMessageBox.Ok
            )
            self.switch_to_login.emit()  
        else:       
            QtWidgets.QMessageBox.critical(
                self, 'Ошибка',
                user_register['message'], QtWidgets.QMessageBox.Ok
            )
