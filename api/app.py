#!/usr/bin/python3
import os
from models import storage
from api.views import app_views
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.teardown_appcontext
def teardown(exc):
    """ Closes the current SQL database session """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ Handles 404 Error Response """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    """ Main Function """
    app.run(
        host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
        port=os.getenv('HBNB_API_PORT', 5000),
        threaded=True,
        debug=True
    )
