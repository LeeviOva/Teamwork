from sqlalchemy.orm import sessionmaker
from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from config import BaseConfig
import uuid
from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models.models import Bike, Base

app = Flask(__name__)

app.config.from_object(BaseConfig)

api = Api(app)
db = SQLAlchemy(app)
engine = create_engine('sqlite:///bikedb.sqlite')
Base.metadata.create_all(engine)

storage_blueprint = Blueprint("Items", __name__, description="Operations on items")

items = {
            "items": [
                {
                    "name": "my item",
                    "item_id":2,
                    "price": 15.99
                },
                {
                    "name": "my item",
                    "item_id":4,
                    "price": 15.25
                }
            ]
        }

bike = Bike()
@storage_blueprint.route('/add_bike', methods=['POST'])
@storage_blueprint.response(201, bike.dict())
class AddBikeToStorage(MethodView):
    def __init__(self):
        #from app import Session as session
        self.bike = Bike()
        self.session = Session()

    def add_bike(self, body):
        new_bike = Bike(**body)

        # Add the bike to the database
        # self.session.add(new_bike)
        # self.session.commit()
        Session.add(new_bike)
        Session.commit()
        Session.close()
        return new_bike.dict(), 201


@storage_blueprint.route("/item/<string:bike_id>")
class BikeInStorage(MethodView):
    def __init__(self):
        #from app import Session
        self.bike = Bike()
        self.session = Session()

    def get(self, bike_id):
        """Get bike details"""
        try:
            #bike = Bike.query.get(bike_id)
            bike = self.session.query(Bike).filter_by(id=bike_id).first()
            #print(bike)

            if self.bike.id == bike_id:
                return jsonify(self.bike.dict())
            else:
                abort(404, message="Bike not found")
        except KeyError:
            abort(404, message="Bike not found")

api.register_blueprint(storage_blueprint)

if __name__ == "__main__":
    with app.app_context():
        Session = sessionmaker(bind=db.engine)
        db.create_all()
    app.run(debug=True)