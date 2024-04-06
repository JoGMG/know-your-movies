#!/usr/bin/python3
""" API views for Cast instances. """
from models import storage
from models.cast import Cast
from api.views import app_views
from flask import jsonify, abort, request


@app_views.route('/cast', strict_slashes=False, methods=['GET'])
def get_cast():
    """ Retrieves all Cast instances. """
    cast = [cast.to_dict() for cast in storage.all(Cast).values()]
    return jsonify(cast)


@app_views.route('/cast/<cast_id>', strict_slashes=False, methods=['GET'])
def get_a_cast(cast_id):
    """
    Retrieves a Cast instance by ID.

    Arguments:
        - `cast_id`: Cast instance ID.
    """
    cast = storage.get(Cast, cast_id)
    if not cast:
        abort(404)
    return jsonify(cast.to_dict())


@app_views.route('/cast/<cast_id>', strict_slashes=False, methods=['PUT'])
def update_cast(cast_id):
    """
    Updates a Cast instance by ID.

    Arguments:
        - `cast_id`: Cast instance ID.
    """
    cast = storage.get(Cast, cast_id)
    if not cast:
        abort(404)
    req_data = request.get_json()
    if not req_data:
        return jsonify({"error": "Request data is empty or not a JSON"}), 400
    ignore = ['__class__', 'id', 'movie_id', 'created_at', 'updated_at']
    for key, value in req_data.items():
        if key not in ignore:
            setattr(cast, key, value)
    cast.save()
    return jsonify(cast.to_dict()), 200


@app_views.route('/cast/<cast_id>', strict_slashes=False, methods=['DELETE'])
def delete_cast(cast_id):
    """
    Deletes a Cast instance by ID.

    Arguments:
        - `cast_id`: Cast instance ID.
    """
    cast = storage.get(Cast, cast_id)
    if not cast:
        abort(404)
    cast.delete()
    storage.save()
    return jsonify({}), 200
