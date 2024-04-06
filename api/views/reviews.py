#!/usr/bin/python3
""" API views for Review instances. """
from models import storage
from models.review import Review
from api.views import app_views
from flask import jsonify, abort, request


@app_views.route('/reviews', strict_slashes=False, methods=['GET'])
def get_reviews():
    """ Retrieves all Review instances. """
    reviews = [review.to_dict() for review in storage.all(Review).values()]
    return jsonify(reviews)


@app_views.route('/reviews/<review_id>', strict_slashes=False, methods=['GET'])
def get_review(review_id):
    """
    Retrieves a Review instance by ID.

    Arguments:
        - `review_id`: Review instance ID.
    """
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    return jsonify(review.to_dict())


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
    ignore = ['__class__',
              'id',
              'movie_id',
              'user_id',
              'created_at',
              'updated_at']
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
