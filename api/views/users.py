#!/usr/bin/python3
""" API views for User instances. """
from models import storage
from models.user import User
from api.views import app_views
from flask import jsonify, abort, request


@app_views.route('/users', strict_slashes=False, methods=['GET'])
def get_users():
    """ Retrieves all User instances. """
    users = [user.to_dict() for user in storage.all(User).values()]
    return jsonify(users)


@app_views.route('/users/<user_id>', strict_slashes=False, methods=['GET'])
def get_user(user_id):
    """
    Retrieves a User instance by ID.

    Arguments:
        - `user_id`: User instance ID.
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users', strict_slashes=False, methods=['POST'])
def post_users():
    """ Creates a new User instance. """
    req_data = request.get_json()
    if not req_data:
        return jsonify({"error": "Request data is empty or not a JSON"}), 400
    if 'email' not in req_data:
        return jsonify({"error": "Missing email"}), 400
    new_user = User(**req_data)
    new_user.save()
    return jsonify(new_user.to_dict()), 201


@app_views.route('/users/<user_id>', strict_slashes=False, methods=['PUT'])
def update_user(user_id):
    """
    Updates a User instance by ID.

    Arguments:
        - `user_id`: User instance ID.
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    req_data = request.get_json()
    if not req_data:
        return jsonify({"error": "Request data is empty or not a JSON"}), 400
    ignore = ['__class__', 'id', 'created_at', 'updated_at']
    for key, value in req_data.items():
        if key not in ignore:
            setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict()), 200


@app_views.route('/users/<user_id>', strict_slashes=False, methods=['DELETE'])
def delete_user(user_id):
    """
    Deletes a User instance by ID.

    Arguments:
        - `user_id`: User instance ID.
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    user.delete()
    storage.save()
    return jsonify({}), 200
