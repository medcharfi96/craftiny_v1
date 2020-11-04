#!/usr/bin/python3

from  models.user import User


us = User()
us.email = "med"
us.password = "123456"
us.first_name = "med"
us.last_name = "charfi"
us.avatar = "zab"
us.token = "nop"
us.adress = "sfax"
us.phone_number = 20133470
us.typ = 0

us.save()
print(us.to_dict())