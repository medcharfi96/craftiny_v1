#!/usr/bin/python3

from models.engine.db_storage import DBStorage




z = DBStorage()
z.get("user","1a315e20-a919-4d69-acf4-ffcd358ac1b0")

print(z)
z.getbyemail("user","raszebi")
print ("-------------------------------------")
print(z)
print("-----------------------")
z.get_by_commentid("user","1a315e20-a919-4d69-acf4-ffcd358ac1b0")
print(z)