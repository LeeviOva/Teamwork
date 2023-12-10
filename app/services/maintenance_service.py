from flask import Blueprint
from flask.views import MethodView
from api.api import maintenance_api
from models.models import Bike
from api.schemas.schemas import BikeSchema

# Blueprint for maintenance service
maintenance_blueprint = Blueprint('maintenance', __name__)

@maintenance_blueprint.route('/bike')
class BikeView(MethodView):
    def get(self, bike_id):
        """Get bike details"""
        bike = Bike.query.get(bike_id)
        if bike:
            return BikeSchema().dump(bike)
        return {"message": "Bike not found"}, 404

    def put(self, args, bike_id):
        """Update bike details"""
        try:
            bike = Bike.query.get(bike_id)
            if bike:
                bike.brand = args.get('brand', bike.brand)
                # Implement logic to update other attributes
                #db.session.commit()
                return BikeSchema().dump(bike)
            return {"message": "Bike not found"}, 404
        except Exception as e:
            #db.session.rollback()
            return {"message": "Validation error", "errors": e.messages}, 400

    # def delete(self, bike_id):
    #     """Delete a bike"""
    #     bike = Bike.query.get(bike_id)
    #     if bike:
    #         db.session.delete(bike)
    #         db.session.commit()
    #         return {"message": "Bike deleted successfully"}
    #     return {"message": "Bike not found"}, 404

# class MaintenanceService(MethodView):

#     #@maintenance_blueprint.arguments(1, location='query')
#    # @maintenance_blueprint.response(status_code=200)
#     def get(self):
#         get_list = [1,2,3,4,5,6]
#         return get_list

