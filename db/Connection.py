from flask_sqlalchemy import SQLAlchemy


class _SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class MainConnection(metaclass=_SingletonMeta):
    def connect(self, app):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///people.db'
        app.config['SQLALCHEMY_ECHO'] = True
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        db = SQLAlchemy(app)

        return db
