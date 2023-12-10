from flask import Flask
from flask_smorest import Api

#config
maintenance_app = Flask(__name__)
maintenance_app.config['API_TITLE'] = "Maintenance"
maintenance_app.config['API_VERSION'] = "1.0"
maintenance_app.config['OPENAPI_VERSION'] = "3.0.2"

maintenance_api = Api(maintenance_app)
