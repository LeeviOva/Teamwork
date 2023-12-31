import uuid
from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models.models import Bike, Base
import app


blp = Blueprint("Items", __name__, description="Operations on items")


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
@blp.route('/add_bike', methods=['POST'])
@blp.response(201, bike.dict())
class AddItem(MethodView):
    def __init__(self):
        #from app import Session as session
        self.bike = Bike()
        self.session = app.Session()
    def add_bike(self, body):
        new_bike = Bike(**body)

        # Add the bike to the database
        self.session.add(new_bike)
        self.session.commit()

        return new_bike.dict(), 201


@blp.route("/item/<string:bike_id>")
class Item(MethodView):
    def __init__(self):
        #from app import Session
        self.bike = Bike()
        self.session = app.Session()

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


#     # def get(self, item_id):
#     #     try:
#     #         for item in items["items"]:
#     #             if item["item_id"] == item_id:
#     #                 return item
#     #     except KeyError:
#     #         abort(404, message="Item not found.")

#     def delete(self, item_id):
#         try:
#             del items[item_id]
#             return {"message": "Item deleted."}
#         except KeyError:
#             abort(404, message="Item not found.")

#     def put(self, item_id):
#         item_data = request.get_json()
#         # There's  more validation to do here!
#         # Like making sure price is a number, and also both items are optional
#         # Difficult to do with an if statement...
#         if "price" not in item_data or "name" not in item_data:
#             abort(
#                 400,
#                 message="Bad request. Ensure 'price', and 'name' are included in the JSON payload.",
#             )
#         try:
#             item = items[item_id]

#             # https://blog.teclado.com/python-dictionary-merge-update-operators/
#             item |= item_data

#             return item
#         except KeyError:
#             abort(404, message="Item not found.")


# @blp.route("/item")
# class ItemList(MethodView):
#     def get(self):
#         return {"items": list(items.values())}

#     def post(self):
#         item_data = request.get_json()
#         # Here not only we need to validate data exists,
#         # But also what type of data. Price should be a float,
#         # for example.
#         if (
#             "price" not in item_data
#             or "store_id" not in item_data
#             or "name" not in item_data
#         ):
#             abort(
#                 400,
#                 message="Bad request. Ensure 'price', 'store_id', and 'name' are included in the JSON payload.",
#             )
#         for item in items.values():
#             if (
#                 item_data["name"] == item["name"]
#                 and item_data["store_id"] == item["store_id"]
#             ):
#                 abort(400, message=f"Item already exists.")

#         item_id = uuid.uuid4().hex
#         item = {**item_data, "id": item_id}
#         items[item_id] = item

#         return item