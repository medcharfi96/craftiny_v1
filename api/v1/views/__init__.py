#!/usr/bin/python3
"""Initialize Blueprint views"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.article import *
from api.v1.views.category import *
from api.v1.views.comment import *
from api.v1.views.likes import *
from api.v1.views.product import *
from api.v1.views.tags import *
from api.v1.views.user import *
