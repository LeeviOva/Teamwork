from app import api
from resources.storageservice import blp as ItemBlueprint

api.register_blueprint(ItemBlueprint)


