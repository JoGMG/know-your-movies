#!/usr/bin/python3
""" API views for Movie instances. """
from models import storage
from models.movie import Movie
from api.views import app_views
from flask import jsonify, abort, request


@app_views.route('/movies', strict_slashes=False, methods=['GET'])
def get_movies():
    """ Retrieves all Movie instances. """
    movies = [movie.to_dict() for movie in storage.all(Movie).values()]
    return jsonify(movies)


@app_views.route('/movies/<movie_id>', strict_slashes=False, methods=['GET'])
def get_movie(movie_id):
    """
    Retrieves a Movie instance by ID.

    Arguments:
        - `movie_id`: Movie instance ID.
    """
    movie = storage.get(Movie, movie_id)
    if not movie:
        abort(404)
    return jsonify(movie.to_dict())


@app_views.route('/movies', strict_slashes=False, methods=['POST'])
def post_movies():
    """ Creates a new Movie instance. """
    req_data = request.get_json()
    if not req_data:
        return jsonify({"error": "Request data is empty or not a JSON"}), 400
    if 'title' not in req_data:
        return jsonify({"error": "Missing title"}), 400
    if 'release_date' not in req_data:
        return jsonify({"error": "Missing release date"}), 400
    new_movie = Movie(**req_data)
    new_movie.save()
    return jsonify(new_movie.to_dict()), 201


@app_views.route('/movies/<movie_id>', strict_slashes=False, methods=['PUT'])
def update_movie(movie_id):
    """
    Updates a Movie instance by ID.

    Arguments:
        - `movie_id`: Movie instance ID.
    """
    movie = storage.get(Movie, movie_id)
    if not movie:
        abort(404)
    req_data = request.get_json()
    if not req_data:
        return jsonify({"error": "Request data is empty or not a JSON"}), 400
    ignore = ['__class__', 'id', 'created_at', 'updated_at']
    for key, value in req_data.items():
        if key not in ignore:
            setattr(movie, key, value)
    movie.save()
    return jsonify(movie.to_dict()), 200


@app_views.route(
        '/movies/<movie_id>', strict_slashes=False, methods=['DELETE'])
def delete_movie(movie_id):
    """
    Deletes a Movie instance by ID.

    Arguments:
        - `movie_id`: Movie instance ID.
    """
    movie = storage.get(Movie, movie_id)
    if not movie:
        abort(404)
    movie.delete()
    storage.save()
    return jsonify({}), 200
