#!/usr/bin/python3
"""
product.py
"""

from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.product import Products
from models.category import Category
from models.user import User
from models.tags import Tag


@app_views.route('/categories/<string:category_id>/products', methods=['GET'],
                 strict_slashes=False)
def get_products(category_id):
    """get products for a specified category"""
    category = storage.get("Category", category_id)
    if category is None:
        abort(404)
    prodlist = []
    for product in category.products:
        prodlist.append(product.to_dict())
    return jsonify(prodlist)


@app_views.route('/products/<string:product_id>', methods=['GET'],
                 strict_slashes=False)
def get_product(product_id):
    """get product information for specified product"""
    product = storage.get("Product", product_id)
    if product is None:
        abort(404)
    return jsonify(product.to_dict())


@app_views.route('/products/<string:product_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_product(product_id):
    """deletes a product based on its product_id"""
    product = storage.get("Product", product_id)
    if product is None:
        abort(404)
    product.delete()
    storage.save()
    return (jsonify({}))


@app_views.route('/categories/<string:category_id>/products', methods=['POST'],
                 strict_slashes=False)
def post_product(category_id):
    """create a new product"""
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
    product = product(**kwargs)
    product.save()
    return make_response(jsonify(product.to_dict()), 201)


@app_views.route('/products/<string:product_id>', methods=['PUT'],
                 strict_slashes=False)
def put_product(product_id):
    """update a product"""
    product = storage.get("Product", product_id)
    if product is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for attr, val in request.get_json().items():
        if attr not in ['id', 'user_id', 'category_id',
                        'created_at', 'updated_at']:
            setattr(product, attr, val)
    product.save()
    return jsonify(product.to_dict())
