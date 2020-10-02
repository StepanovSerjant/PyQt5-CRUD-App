# https://docs.sqlalchemy.org/en/13/orm/tutorial.html
# https://docs.sqlalchemy.org/en/13/orm/backref.html
from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

class User(Base):
    """ Таблица пользователя """
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)  
    password = Column(String(25), nullable=False)  
    email = Column(String(25), nullable=False, unique=True)  
    wishes = relationship("Wish", backref='user')

    def __init__(self, name, password, email):
        self.name = name    
        self.password = password    
        self.email = email

    def __repr__(self):
        return "<User(name='%s', password='%s', email='%s')>" % (self.name,
            self.password, self.email)


class Wish(Base):
    """ Таблица желаний пользователей """
    __tablename__ = "Wishes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)  
    link = Column(String(80), nullable=False)
    description = Column(String(50), nullable=False)
    created_at = Column(DateTime(), nullable=False, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('Users.id'), nullable=False)

    def __init__(self, name, link, description, created_at, user_id):
        self.name = name    
        self.link = link
        self.description = description
        self.created_at = created_at
        self.user_id = user_id

    def __repr__(self):
        return "<Wish(name='%s', link='%s', description='%s', created_at='%s', user_id='%s')>" % (self.name,
            self.link, self.description, self.created_at, self.user_id)

