#!/usr/bin/python3
"""
tags.py
"""

from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.tags import Tag


@app_views.route('/tags', methods=['GET'], strict_slashes=False)
def get_tags():
    """get tag information for all tags"""
    taglist = []
    for tag in storage.all("Tag").values():
        taglist.append(tag.to_dict())
    return jsonify(taglist)


@app_views.route('/tags/<string:tag_id>', methods=['GET'],
                 strict_slashes=False)
def get_tag(tag_id):
    """get tag information for specified tag"""
    tag = storage.get("Tag", tag_id)
    if tag is None:
        abort(404)
    return jsonify(tag.to_dict())


@app_views.route('/tags/<string:tag_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_tag(tag_id):
    """deletes a tag based on its tag_id"""
    tag = storage.get("Tag", tag_id)
    if tag is None:
        abort(404)
    tag.delete()
    storage.save()
    return (jsonify({}))


@app_views.route('/tags', methods=['POST'], strict_slashes=False)
def post_tag():
    """create a new tag"""
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'label' not in request.get_json():
        return make_response(jsonify({'error': 'Missing label'}), 400)
    tag = tag(**request.get_json())
    tag.save()
    return make_response(jsonify(tag.to_dict()), 201)


@app_views.route('/tags/<string:tag_id>', methods=['PUT'],
                 strict_slashes=False)
def put_tag(tag_id):
    """update an tag"""
    tag = storage.get("Tag", tag_id)
    if tag is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for attr, val in request.get_json().items():
        if attr not in ['id', 'created_at', 'updated_at']:
            setattr(tag, attr, val)
    tag.save()
    return jsonify(tag.to_dict())
