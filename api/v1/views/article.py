#!/usr/bin/python3
"""
article.py
"""

from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.article import Article
from models.category import Category
from models.user import User
from models.tags import Tag


@app_views.route('/categories/<string:category_id>/articles', methods=['GET'],
                 strict_slashes=False)
def get_articles(category_id):
    """get articles for a specified category"""
    category = storage.get("Category", category_id)
    if category is None:
        abort(404)
    artlist = []
    for article in category.articles:
        artlist.append(article.to_dict())
    return jsonify(artlist)


@app_views.route('/articles/<string:article_id>', methods=['GET'],
                 strict_slashes=False)
def get_article(article_id):
    """get article information for specified article"""
    article = storage.get("Article", article_id)
    if article is None:
        abort(404)
    return jsonify(article.to_dict())


@app_views.route('/articles/<string:article_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_article(article_id):
    """deletes an article based on its article_id"""
    article = storage.get("Article", article_id)
    if article is None:
        abort(404)
    article.delete()
    storage.save()
    return (jsonify({}))


@app_views.route('/categories/<string:category_id>/articles', methods=['POST'],
                 strict_slashes=False)
def post_article(category_id):
    """create a new article"""
    category = storage.get("Category", category_id)
    if category is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    kwargs = request.get_json()
    if 'user_id' not in kwargs:
        return make_response(jsonify({'error': 'Missing user_id'}), 400)
    user = storage.get("User", kwargs['user_id'])
    if user is None:
        abort(404)
    kwargs['category_id'] = category_id
    article = article(**kwargs)
    article.save()
    return make_response(jsonify(article.to_dict()), 201)


@app_views.route('/articles/<string:article_id>', methods=['PUT'],
                 strict_slashes=False)
def put_article(article_id):
    """update a article"""
    article = storage.get("Article", article_id)
    if article is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for attr, val in request.get_json().items():
        if attr not in ['id', 'user_id', 'category_id',
                        'created_at', 'updated_at']:
            setattr(article, attr, val)
    article.save()
    return jsonify(article.to_dict())