#!/usr/bin/python3

from models.user import User,BaseModel,Base
from models.engine.db_storage import DBStorage
us =  new User
ba = DBStorage.new(us)
print(ba)