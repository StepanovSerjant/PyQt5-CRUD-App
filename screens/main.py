import datetime

import pandas as pd
from PyQt5 import QtCore, QtWidgets

import database.db as db
from screens.ui.main_ui import MainDialog


class TableModel(QtCore.QAbstractTableModel):
    """ Абстрактный класс для отображения таблицы внутри TableView """
    def __init__(self, data, username):
        QtCore.QAbstractTableModel.__init__(self)
        self._data = data
        self._username = username

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._data.columns[col]
        return None

    def flags(self, index):
        flags = super(self.__class__,self).flags(index)
        
        flags |= QtCore.Qt.ItemIsEditable
        flags |= QtCore.Qt.ItemIsSelectable
        flags |= QtCore.Qt.ItemIsEnabled
        return flags

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        # https://stackoverflow.com/questions/8479799/editing-qtableview-cell-value
        if index.column() == 3:
            return False
        current_time = datetime.datetime.now().replace(second=0, microsecond=0)
        self._data.iloc[index.row(), index.column()] = value
        self._data.iloc[index.row(), 3] = current_time
        db.edit_user_wish(
            self._username, index.row(),
            index.column(), value, current_time
        )
        return True


class Main(QtWidgets.QWidget, MainDialog):
    """ Обработка интерактивных элементов главного окна """
    switch_to_login = QtCore.pyqtSignal()
    switch_to_add = QtCore.pyqtSignal(str)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.add_btn.clicked.connect(self.add_click)
        self.remove_btn.clicked.connect(self.remove_click)
        self.logout_btn.clicked.connect(self.logout_click)

    def set_table_data(self, username):
        """ Вставка данных пользователя в таблицу """
        user_wishes = db.get_user_wishes(username)
        data_frame = [[wish.name, wish.link, wish.description, wish.created_at] for wish in user_wishes]
        data = pd.DataFrame(
            data_frame,
            columns = ['Name', 'Link', 'Description', 'Created at'],
            index=[str(i) for i in range(1, len(data_frame) + 1)]
        )

        # https://www.youtube.com/watch?v=hJEQEECZSH0
        self.model = TableModel(data, username)
        self.table_view.setModel(self.model)
        self.table_view.resizeColumnsToContents()

    def logout_click(self):
        """ Обработка нажатия кнопки logout """
        self.switch_to_login.emit()   

    def add_click(self):
        """ Обработка нажатия кнопки add """
        self.switch_to_add.emit(self.username_lbl.text().split(' ')[1])   

    def remove_click(self):
        """ Обработка нажатия кнопки remove (удаление элемента из таблицы) """
        index = self.table_view.currentIndex().row()
        if index == -1:
            QtWidgets.QMessageBox.critical(
                self, 'Ошибка', 'Необходимо выделить строку прежде, чем удалить!', QtWidgets.QMessageBox.Ok
            )
        else:
            username = self.username_lbl.text().split(' ')[1]
            db.delete_user_wish(username, index)
            self.set_table_data(username)
