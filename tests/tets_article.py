#!/usr/bin/python3
from models.category import Category
from models.tags import Tag
from models.user import User
from models.article import Article

TA = Tag()
TA.label = "#test1"
TA.save()
CA = Category()
CA.label = "test1"
CA.save()
US = User()
US.password = "test1"
US.first_name = "test1 "
US.phone_number = 0000
US.save()

AR = Article()
AR.user_id = US.id
AR.tag_id = TA.id
AR.category_id = CA.id
AR.title = "tets"
AR.description = " walaaaaaaaaaaaaaaaaaaaah test"
AR.content = "nammi test"
AR.version = "test"
AR.promoted = 1
AR.save()
print(TA.to_dict())
print("------------------------------------------------")
print("\n")

print(CA.to_dict())
print("------------------------------------------------")
print("\n")

print(US.to_dict())
print("------------------------------------------------")
print("\n")

print(AR.to_dict())
print("------------------------------------------------")
print("\n")