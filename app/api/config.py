from api import maintenance_app

class ApiConfig:
    maintenance_app.config['API_TITLE'] = "Maintenance"
    maintenance_app.config['API_VERSION'] = "1.0"
    maintenance_app.config['OPENAPI_VERSION'] = "3.0.2"