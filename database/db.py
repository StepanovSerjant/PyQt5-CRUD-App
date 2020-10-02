import datetime

from PyQt5 import QtWidgets
from sqlalchemy_utils import database_exists
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from sqlalchemy_utils.functions import database_exists

from database.models import Base, User, Wish
from settings import DATABASE


Session = sessionmaker()
engine = create_engine(
    DATABASE,
    echo=True
)
Session.configure(bind=engine)
session = Session()


def create_db():
    """ Создание БД """
    if not database_exists(engine.url):
        Base.metadata.create_all(engine)


def get_user_info(username):
    """ Получение полной информации пользователе """
    user_info = session.query(User).filter_by(name=username).all()[0]
    return user_info


def user_exist(username):
    """ Проверка наличия пользователя в БД """
    is_exist = session.query(exists().where(User.name == username)).scalar()
    if is_exist:
        return True
    return False


def create_user(name, password, email):
    """ Добавление в базу нового пользователя """
    session.add(User(name, password, email))
    session.commit() 


def get_user_wishes(username):
    """ Функция получения списка желаний пользователя """
    user_id = session.query(User).filter_by(name=username).first().id
    user_wishes = session.query(Wish).filter_by(user_id=user_id).all()
    return user_wishes


def edit_user_wish(username, row_number, column_number, value, current_time):
    """ Функция изменения данных пользователя при изменении в таблице """
    # https://stackoverflow.com/questions/9667138/how-to-update-sqlalchemy-row-entry
    wish_to_change = get_user_wishes(username)[row_number]
    if column_number == 0:
        session.query(Wish).filter(Wish.id == wish_to_change.id).\
        update({Wish.name: value, Wish.created_at: current_time})
    elif column_number == 1:
        session.query(Wish).filter(Wish.id == wish_to_change.id).\
        update({Wish.link: value, Wish.created_at: current_time})
    elif column_number == 2:
        session.query(Wish).filter(Wish.id == wish_to_change.id).\
        update({Wish.description: value,
        Wish.created_at: current_time})
    session.commit()


def delete_user_wish(username, row_number):
    """ Функция удаление желания из списка """
    wish_to_delete = get_user_wishes(username)[row_number]
    session.delete(wish_to_delete)
    session.commit()


def add_wish(username, wish_name, wish_link, wish_description):
    """ Функция внесения нового желания в список """
    user_id = session.query(User).filter_by(name=username).first().id
    current_time = datetime.datetime.now().replace(second=0, microsecond=0)
    session.add(Wish(
        name=wish_name,
        link=wish_link,
        description=wish_description,
        created_at=current_time,
        user_id=user_id
    ))
    session.commit()
