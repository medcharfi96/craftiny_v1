#!/usr/bin/python3
"""
index.py to connect to API
"""

from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify
from models import storage


craftText = {
    "article": "Article",
    "category": "Category",
    "comment": "Comment",
    "likes": "Likes",
    "product": "Products",
    "tags": "Tag",
    "user": "User"
}


@app_views.route('/status', strict_slashes=False)
def craftStatus():
    """craftStatus"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def craftStats():
    """craftStats"""
    return_dict = {}
    for key, value in craftText.items():
        return_dict[key] = storage.count(value)
    return jsonify(return_dict)

if __name__ == "__main__":
    pass
