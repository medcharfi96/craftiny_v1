#!/usr/bin/python3
"""
comment.py
"""

from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.comment import Comment
from models.article import Article
from models.user import User


@app_views.route('/articles/<string:article_id>/comments', methods=['GET'],
                 strict_slashes=False)
def get_comments(article_id):
    """get comments for a specified article"""
    article = storage.get("Article", article_id)
    if article is None:
        abort(404)
    comlist = []
    for comment in article.comments:
        comlist.append(comment.to_dict())
    return jsonify(comlist)


@app_views.route('/comments/<string:comment_id>', methods=['GET'],
                 strict_slashes=False)
def get_comment(comment_id):
    """get comment information for specified comment"""
    comment = storage.get("Comment", comment_id)
    if comment is None:
        abort(404)
    return jsonify(comment.to_dict())


@app_views.route('/comments/<string:comment_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_comment(comment_id):
    """deletes a comment based on its comment_id"""
    comment = storage.get("Comment", comment_id)
    if comment is None:
        abort(404)
    comment.delete()
    storage.save()
    return (jsonify({}))


@app_views.route('/articles/<string:article_id>/comments', methods=['POST'],
                 strict_slashes=False)
def post_comment(article_id):
    """create a new comment"""
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
    comment = comment(**kwargs)
    comment.save()
    return make_response(jsonify(comment.to_dict()), 201)


@app_views.route('/comments/<string:comment_id>', methods=['PUT'],
                 strict_slashes=False)
def put_comment(comment_id):
    """update a comment"""
    comment = storage.get("Comment", comment_id)
    if comment is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for attr, val in request.get_json().items():
        if attr not in ['id', 'user_id', 'article_id',
                        'created_at', 'updated_at']:
            setattr(comment, attr, val)
    comment.save()
    return jsonify(comment.to_dict())
