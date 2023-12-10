from flask import Flask
from services.maintenance_service import maintenance_blueprint

maintenance_app = Flask(__name__)

# Register the service blueprint for maintenance_service app
maintenance_app.register_blueprint(maintenance_blueprint, url_prefix='/service')

if __name__ == '__main__':
    maintenance_app.run()


