# app/app.py
from flask import Flask
from flask_smorest import Api
from app.services.app import db  # Adjust the import path

app = Flask(__name__)
app.config["API_TITLE"] = "Bikes API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.2"
api = Api(app)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
