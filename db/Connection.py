from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from dotenv import load_dotenv
import os


load_dotenv()

class _SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class MainConnection(metaclass=_SingletonMeta):
    def connect(self, app, db):
        app.config['SQLALCHEMY_DATABASE_URI'] = db
        if os.getenv("ENV") == 'TEST':
            app.config['SQLALCHEMY_ECHO'] = False
        else:
            app.config['SQLALCHEMY_ECHO'] = True
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        db = SQLAlchemy(app)

        return db
