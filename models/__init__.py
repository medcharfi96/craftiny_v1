#!/usr/bin/python3
"""
int class call to dbstorage
"""


from models.engine.db_storage import DBStorage

storage = DBStorage()
storage.reload()