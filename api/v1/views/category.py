#!/usr/bin/python3
"""
category.py
"""

from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.category import Category


@app_views.route('/categories', methods=['GET'], strict_slashes=False)
def get_categories():
    """get category information for all categories"""
    catlist = []
    for category in storage.all("Category").values():
        catlist.append(category.to_dict())
    return jsonify(catlist)


@app_views.route('/categories/<string:category_id>', methods=['GET'],
                 strict_slashes=False)
def get_category(category_id):
    """get category information for specified category"""
    category = storage.get("Category", category_id)
    if category is None:
        abort(404)
    return jsonify(category.to_dict())


@app_views.route('/categories/<string:category_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_category(category_id):
    """deletes a category based on its category_id"""
    category = storage.get("Category", category_id)
    if category is None:
        abort(404)
    category.delete()
    storage.save()
    return (jsonify({}))


@app_views.route('/categories', methods=['POST'], strict_slashes=False)
def post_category():
    """create a new category"""
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'label' not in request.get_json():
        return make_response(jsonify({'error': 'Missing label'}), 400)
    category = category(**request.get_json())
    category.save()
    return make_response(jsonify(category.to_dict()), 201)


@app_views.route('/categories/<string:category_id>', methods=['PUT'],
                 strict_slashes=False)
def put_category(category_id):
    """update an category"""
    category = storage.get("Category", category_id)
    if category is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for attr, val in request.get_json().items():
        if attr not in ['id', 'created_at', 'updated_at']:
            setattr(category, attr, val)
    category.save()
    return jsonify(category.to_dict())
