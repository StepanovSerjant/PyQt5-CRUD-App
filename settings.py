import os


DATABASE_ENGINE = 'sqlite:///'
DATABASE_DIR = os.getcwd()
DATABASE_NAME = 'vista_crud.db'
DATABASE = ''.join([DATABASE_ENGINE, os.path.join(DATABASE_DIR, DATABASE_NAME)])

STYLE_DIR = os.path.join(os.getcwd(), 'screens/ui/style/css')
