#!/usr/bin/python3
"""
de tt façon test ye5dem
"""
from models.user import User

us = User()
us.password = "nik f jbam"
us.first_name = "med charfi "
us.phone_number = 1447755


us.save()
print(us.to_dict())