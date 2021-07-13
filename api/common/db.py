import pymysql

import config
from flask import g, current_app


def get_db():
    if 'db' not in g:
        g.db = pymysql.connect(host=current_app.config['MYSQL_FOR_DB']['DATABASE_HOST'], port=current_app.config['MYSQL_FOR_DB']['DATABASE_PORT'],
                               user=current_app.config['MYSQL_FOR_DB']['DATABASE_USER'],
                               password=current_app.config['MYSQL_FOR_DB']['DATABASE_PASSWORD'],
                               db=current_app.config['MYSQL_FOR_DB']['DATABASE_DB'], charset=current_app.config['MYSQL_FOR_DB']['DATABASE_CHARSET'])

    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.cursor().close()
        db.close()


def close_engine(e=None):
    session = g.pop('session', None)
    if session is not None:
        session.close()
    engine = g.pop('engine', None)
    if engine is not None:
        engine.dispose()


def init_app(app):
    app.teardown_appcontext(close_db)


def init_engine(app):
    app.teardown_appcontext(close_engine)