#!/usr/bin/python3
from models.category import Category
from  models.tags import Tag
from  models.user import User
from models.product import Products
CAT = Category()
CAT.label = "a8888"
TA = Tag()
TA.label = "azzzabi"
PRO =Products()
US = User()
US.email = "AZEAZEAZEAZEAZEAZE"
US.password= "3asba"
PRO.user_id = US.id
tag_id = TA.id
category_id = CAT.id
title = "zazazaz"
description = "hjdbfjfe"
CAT.save()
TA.save()
US.save()
PRO.save()

print(CAT.to_dict())
print(TA.to_dict())
print(US.to_dict())
print(PRO.to_dict())