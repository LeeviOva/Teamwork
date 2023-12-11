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
from models.models import Bike, Base, Rental
from schemas.schemas import BikeSchema

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
@storage_blueprint.route('/add_bike/', methods=['POST'])
@storage_blueprint.response(201, BikeSchema())
class AddBikeToStorage(MethodView):
    def __init__(self):
        with app.app_context():
            Session = sessionmaker(bind=engine)
            self.session = Session()
        self.bike = Bike()

    def post(self):
        #new_bike = Bike(**body)
        new_bike = self.bike(brand='toyota', size='junior', user='male')
        self.session.add(new_bike)
        self.session.commit()
        return jsonify({"message": "Success", "data": new_bike.dict()})

@storage_blueprint.route("/item/<string:bike_id>")
class BikeInStorage(MethodView):
    def __init__(self):
        with app.app_context():
            Session = sessionmaker(bind=engine)
            self.session = Session()
        self.bike = Bike()
        #self.session = Session()

    def get(self, bike_id):
        """Get bike details"""
        try:
            #bike = Bike.query.get(bike_id)
            print(bike_id)
            bike = self.session.query(Bike).filter_by(id=bike_id).first()

            if bike.id == bike_id:
                return jsonify(bike.dict())
            else:
                abort(404, message="Bike not found")
        except KeyError:
            abort(404, message="Bike not found")

rental_blueprint = Blueprint("Rental service", __name__, description="Operations on rentalbikes")
@rental_blueprint.route("/rental/<string:bike_id>/<string:customer_id>")
class UpdateBikeStatus(MethodView):
    def __init__(self):
        self.rental = Rental()
        self.session = Session()

    def put(self, bike_id, customer_id):
        #new_rental = rental()
        print(bike_id)
        bike_id = self.session.query(Bike).filter_by(id=bike_id).first()
        if bike:
            return jsonify({"id": bike.id})
        else:
            abort(404, message="Bike not found")
            return jsonify(self.rental.dict())

    def delete(self, bike_id):
        pass



api.register_blueprint(storage_blueprint)
api.register_blueprint(rental_blueprint)



if __name__ == "__main__":
    with app.app_context():
        Session = sessionmaker(bind=engine)
        session = Session()
    app.run(debug=True)