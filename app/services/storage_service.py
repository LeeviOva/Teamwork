from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_smorest import Api, Blueprint
from flask.views import MethodView
from marshmallow import ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bikedb.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)

# Define the BikeModel and other logic as before

bike_bp = Blueprint(
    "bikes", __name__, url_prefix="/bikes", description="Bike Operations"
)

class BikesView(MethodView):
    def get(self):
        """Get all bikes"""
        bikes = BikeModel.query.all()
        return BikeSchema().dump(bikes, many=True)

    def post(self, args):
        """Add a new bike"""
        try:
            new_bike = BikeModel(**args)
            db.session.add(new_bike)
            db.session.commit()
            return BikeSchema().dump(new_bike)
        except ValidationError as e:
            db.session.rollback()
            return {"message": "Validation error", "errors": e.messages}, 400

class BikeView(MethodView):
    def get(self, bike_id):
        """Get bike details"""
        bike = BikeModel.query.get(bike_id)
        if bike:
            return BikeSchema().dump(bike)
        return {"message": "Bike not found"}, 404

    def put(self, args, bike_id):
        """Update bike details"""
        try:
            bike = BikeModel.query.get(bike_id)
            if bike:
                bike.brand = args.get('brand', bike.brand)
                # Implement logic to update other attributes
                db.session.commit()
                return BikeSchema().dump(bike)
            return {"message": "Bike not found"}, 404
        except ValidationError as e:
            db.session.rollback()
            return {"message": "Validation error", "errors": e.messages}, 400

    def delete(self, bike_id):
        """Delete a bike"""
        bike = BikeModel.query.get(bike_id)
        if bike:
            db.session.delete(bike)
            db.session.commit()
            return {"message": "Bike deleted successfully"}
        return {"message": "Bike not found"}, 404

bike_bp.add_url_rule("/", view_func=BikesView.as_view("bikes"))
bike_bp.add_url_rule("/<int:bike_id>", view_func=BikeView.as_view("bike"))

api.register_blueprint(bike_bp)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
