from PyQt5 import QtCore, QtWidgets

import services
from screens.ui.login_ui import LoginDialog


class Login(QtWidgets.QWidget, LoginDialog):
    """ Обработка интерактивных элементов окна авторизации """

    switch_to_main = QtCore.pyqtSignal(str, name='main_signal')
    switch_to_register = QtCore.pyqtSignal(name='register_signal')

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.login_btn.clicked.connect(self.login_click)
        self.sign_up_btn.clicked.connect(self.sign_up_click)

    def login_click(self):
        """ Функция обработки нажатия на клавишу login """
        user_name = self.name_line_edit.text()
        user_password = self.pass_line_edit.text()
        auth_data = dict([
            ('name', user_name),
            ('password', user_password)
        ])
        auth = services.user_auth(auth_data)
        
        if auth['status']:
            self.switch_to_main.emit(user_name) 
        else:
            QtWidgets.QMessageBox.critical(
                self, 'Ошибка', auth['message'], QtWidgets.QMessageBox.Ok
            )

    def sign_up_click(self):
        """ Функция обработки нажатия на клавишу sign up """
        self.switch_to_register.emit() 
        