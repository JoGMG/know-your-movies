#!/usr/bin/python3
""" API views for Movie Reviews instances. """
import os
from models import storage
from models.movie import Movie
from models.user import User
from models.review import Review
from api.views import app_views
from flask import jsonify, abort, request
from api.views.users import get_users, post_users


@app_views.route(
        '/movies/<movie_id>/reviews', strict_slashes=False, methods=['GET'])
def get_movie_reviews(movie_id):
    """
    Retrieves a Movie instance's reviews.

    Arguments:
        - `movie_id`: Movie instance ID.
    """
    movie = storage.get(Movie, movie_id)
    if not movie:
        abort(404)
    
    movie_reviews = []
    for review in movie.reviews:
        review_dict = review.to_dict()
        review_dict.pop("__class__")

        user = storage.get(User, review.user_id)
        ignore = ["id", "created_at", "updated_at", "__class__"]
        for key, value in user.to_dict().items():
            if key not in ignore:
                review_dict[key] = value
        movie_reviews.append(review_dict)

    return jsonify({"results": movie_reviews})


@app_views.route(
        '/movies/<movie_id>/reviews', strict_slashes=False, methods=['POST'])
def post_movie_reviews(movie_id):
    """
    Creates a new Review instance for a Movie instance.

    Arguments:
        - `movie_id`: Movie instance ID.
    """
    req_data = request.get_json()
    if not req_data:
        return jsonify({"error": "Request data is empty or not a JSON"}), 400
    if 'title' not in req_data:
        return jsonify({"error": "Missing title"}), 400
    if 'release_date' not in req_data:
        return jsonify({"error": "Missing release date"}), 400
    if 'email' not in req_data:
        return jsonify({"error": "Missing email"}), 400
    if 'content' not in req_data:
        return jsonify({"error": "Missing content"}), 400

    movie = storage.get(Movie, movie_id)
    if not movie:
        new_movie = Movie(
            id=movie_id,
            title=req_data["title"],
            release_date=req_data["release_date"],
            poster_path=req_data.get("poster_path", None),
            overview=req_data.get("overview", None)
        )
        new_movie.save()

    user_id = None
    user_email = req_data.get('email', None)
    user_author = req_data.get('author', None)
    if user_email:
        for user in storage.all(User).values():
            if user_email == user.email:
                user_id = user.id
    if not user_id:
        new_user = User(email=user_email, author=user_author)
        new_user.save()
        user_id = new_user.id

    req_data['movie_id'] = movie_id
    req_data['user_id'] = user_id
    new_movie_review = Review(
        movie_id=req_data['movie_id'],
        user_id=req_data['user_id'],
        content=req_data['content']
    )
    new_movie_review.save()
    return jsonify(new_movie_review.to_dict()), 201
