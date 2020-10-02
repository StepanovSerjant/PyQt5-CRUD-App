import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from database import db
from screens.add_form import WishForm
from screens.register import Register
from screens.login import Login
from screens.main import Main


class Controller:
    """ Контроллер отвечающий за переключениями между окнами """
    def __init__(self):
        self.register = Register()
        self.login = Login()
        self.main = Main()
        self.wish_form = WishForm()

    def show_login(self):
        self.register.close()
        self.main.close()

        self.login.show()

        self.login.switch_to_main.connect(self.show_main)
        self.login.switch_to_register.connect(self.show_register)

    def show_register(self):
        self.login.close()
        self.register.show()

        self.register.switch_to_login.connect(self.show_login)

    def show_main(self, user):
        self.login.close()
        self.wish_form.close()
        self.main.show()

        self.main.username_lbl.setText(
            f'User: {user}'
        )
        self.main.username_lbl.adjustSize()

        self.main.set_table_data(user)
        self.main.switch_to_login.connect(self.show_login)
        self.main.switch_to_add.connect(self.show_wish_form)
    
    def show_wish_form(self, username):
        self.wish_form = WishForm(username)
        self.wish_form.show()
        self.wish_form.switch_to_main.connect(self.show_main)


def run():
    db.create_db()

    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
    