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
    if os.getenv('KYM_STORAGE') == 'db':
        movie_reviews = [review.to_dict() for review in movie.reviews]
    else:
        movie_reviews = [review for review in movie.reviews]
    return jsonify(movie_reviews)


@app_views.route(
        '/movies/<movie_id>/reviews', strict_slashes=False, methods=['POST'])
def post_movie_reviews(movie_id):
    """
    Creates a new Review instance for a Movie instance.

    Arguments:
        - `movie_id`: Movie instance ID.
    """
    movie = storage.get(Movie, movie_id)
    if not movie:
        abort(404)
    req_data = request.get_json()
    if not req_data:
        return jsonify({"error": "Request data is empty or not a JSON"}), 400
    if 'text' not in req_data:
        return jsonify({"error": "Missing text"}), 400
    if 'email' not in req_data:
        return jsonify({"error": "Missing email"}), 400
    user_id = None
    user_email = req_data.get('email', None)
    for user in storage.all(User).values():
        if user_email:
            if user_email == user.email:
                user_id = user.id
    if not user_id:
        if 'name' not in req_data:
            if user_email:
                new_user = User(email=user_email)
        else:
            user_name = req_data.get('name', None)
            if user_email and user_name:
                new_user = User(email=user_email, name=user_name)
        new_user.save()
        user_id = new_user.id
    req_data['movie_id'] = movie_id
    req_data['user_id'] = user_id
    new_movie_review = Review(
        movie_id=req_data['movie_id'],
        user_id=req_data['user_id'],
        text=req_data['text']
    )
    new_movie_review.save()
    return jsonify(new_movie_review.to_dict()), 201


@app_views.route('/reviews/<review_id>', strict_slashes=False, methods=['PUT'])
def update_review(review_id):
    """
    Updates a Review instance by ID.
    
    Arguments:
        - `review_id`: Review instance ID.
    """
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    req_data = request.get_json()
    if not req_data:
        return jsonify({"error": "Request data is empty or not a JSON"}), 400
    ignore = ['__class__', 'id', 'movie_id', 'user_id', 'created_at', 'updated_at']
    for key, value in req_data.items():
        if key not in ignore:
            setattr(review, key, value)
    review.save()
    return jsonify(review.to_dict()), 200


@app_views.route(
        '/reviews/<review_id>', strict_slashes=False, methods=['DELETE'])
def delete_review(review_id):
    """
    Deletes a Review instance by ID.
    
    Arguments:
        - `review_id`: Review instance ID.
    """
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    review.delete()
    storage.save()
    return jsonify({}), 200
