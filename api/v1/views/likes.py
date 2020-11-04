#!/usr/bin/python3
"""
likes.py
"""

from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.likes import Likes
from models.article import Article
from models.user import User


@app_views.route('/articles/<string:article_id>/likes', methods=['GET'],
                 strict_slashes=False)
def get_likes(article_id):
    """get likes for a specified article"""
    article = storage.get("Article", article_id)
    if article is None:
        abort(404)
    likelist = []
    for like in article.likes:
        likelist.append(like.to_dict())
    return jsonify(likelist)


@app_views.route('/likes/<string:like_id>', methods=['GET'],
                 strict_slashes=False)
def get_like(like_id):
    """get like information for specified like"""
    like = storage.get("Likes", like_id)
    if like is None:
        abort(404)
    return jsonify(like.to_dict())


@app_views.route('/likes/<string:like_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_like(like_id):
    """deletes a like based on its like_id"""
    like = storage.get("Likes", like_id)
    if like is None:
        abort(404)
    like.delete()
    storage.save()
    return (jsonify({}))


@app_views.route('/articles/<string:article_id>/likes', methods=['POST'],
                 strict_slashes=False)
def post_like(article_id):
    """create a new like"""
    article = storage.get("Article", article_id)
    if article is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    kwargs = request.get_json()
    if 'user_id' not in kwargs:
        return make_response(jsonify({'error': 'Missing user_id'}), 400)
    user = storage.get("User", kwargs['user_id'])
    if user is None:
        abort(404)
    kwargs['article_id'] = article_id
    like = like(**kwargs)
    like.save()
    return make_response(jsonify(like.to_dict()), 201)


@app_views.route('/likes/<string:like_id>', methods=['PUT'],
                 strict_slashes=False)
def put_like(like_id):
    """update a like"""
    like = storage.get("Likes", like_id)
    if like is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for attr, val in request.get_json().items():
        if attr not in ['id', 'user_id', 'article_id',
                        'created_at', 'updated_at']:
            setattr(like, attr, val)
    like.save()
    return jsonify(like.to_dict())
