from flask import Flask
from flask_restless import APIManager
# start Models
from model.Models import FactoryModels
# config DB
from db.Connection import MainConnection

app = Flask(__name__)

# initialize
# initialize DB
db = MainConnection().connect(app)
# initialize APIManager
api_manager = APIManager(app, flask_sqlalchemy_db=db)
# initialize factory Models
factory = FactoryModels()

# Creating Models
Person = factory.init_person(db)
# Create endpoints
api_manager.create_api(Person, methods=['GET', 'POST', 'DELETE', 'PUT'])


if __name__ == '__main__':
    app.run()
