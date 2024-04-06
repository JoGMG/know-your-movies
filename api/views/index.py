#!/usr/bin/python3
""" API views for App Index. """
from flask import jsonify
from api.views import app_views
from models import storage
from models.user import User
from models.review import Review


@app_views.route('/status', strict_slashes=False)
def status():
    """ Returns application status. """
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def stats():
    """ Retrieves count of User and Review instances. """
    users = storage.count(User)
    reviews = storage.count(Review)
    return jsonify({
        "users": users,
        "reviews": reviews
    })
