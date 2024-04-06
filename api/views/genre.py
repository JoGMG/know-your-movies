#!/usr/bin/python3
""" API views for Review instances. """
from models import storage
from models.genre import Genre
from api.views import app_views
from flask import jsonify, abort, request


@app_views.route('/genres', strict_slashes=False, methods=['GET'])
def get_genres():
    """ Retrieves all Genre instances. """
    genres = [genre.to_dict() for genre in storage.all(Genre).values()]
    return jsonify(genres)


@app_views.route('/genres/<genre_id>', strict_slashes=False, methods=['GET'])
def get_genre(genre_id):
    """
    Retrieves a Genre instance by ID.

    Arguments:
        - `genre_id`: Genre instance ID.
    """
    genre = storage.get(Genre, genre_id)
    if not genre:
        abort(404)
    return jsonify(genre.to_dict())


@app_views.route('/genres/<genre_id>', strict_slashes=False, methods=['PUT'])
def update_genre(genre_id):
    """
    Updates a Genre instance by ID.

    Arguments:
        - `genre_id`: Genre instance ID.
    """
    genre = storage.get(Genre, genre_id)
    if not genre:
        abort(404)
    req_data = request.get_json()
    if not req_data:
        return jsonify({"error": "Request data is empty or not a JSON"}), 400
    ignore = ['__class__', 'id', 'movie_id', 'created_at', 'updated_at']
    for key, value in req_data.items():
        if key not in ignore:
            setattr(genre, key, value)
    genre.save()
    return jsonify(genre.to_dict()), 200


@app_views.route(
        '/genres/<genre_id>', strict_slashes=False, methods=['DELETE'])
def delete_genre(genre_id):
    """
    Deletes a Genre instance by ID.

    Arguments:
        - `genre_id`: Genre instance ID.
    """
    genre = storage.get(Genre, genre_id)
    if not genre:
        abort(404)
    genre.delete()
    storage.save()
    return jsonify({}), 200
