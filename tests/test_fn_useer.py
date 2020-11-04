#!/usr/bin/python3

from models.user import User




us = User()
us.password = "azerty"
us.password = us.hashpwd(us.password)
us.email = "raszebi"
us.first_name = "trem omik"
us.phone_number = 00000000
us.save()
us.get
print(us.to_dict())
print("\n")
print("-----------------------------")
print(us.as_dict())
print("\n")
print("-----------------------------")
print(us.as_dict_nopwd())
