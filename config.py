import os

basedir = os.path.abspath(os.path.dirname(__file__))

PIC_DIR = os.path.join(basedir, 'museum_main/static/img/pictures')
PIC_THUMB_DIR = os.path.join(PIC_DIR, 'thumb')

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SECRET_KEY = 'development key'
USERNAME='admin'
PASSWORD='default'