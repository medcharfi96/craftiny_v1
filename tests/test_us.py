#!/usr/bin/python3
"""
hash coding
"""
from models.user import User

zer =User()
zer.password = "zab3lik"
zer.password = zer.hashpwd(zer.password)
zer.email = "medpwd"

zer.first_name = "pwd"
zer.last_name = "PWD"
zer.avatar = "zab"
zer.token = "nop"
zer.adress = "sfax"
zer.phone_number = 20133470
zer.typ = 0

zer.save()
print(zer.to_dict())