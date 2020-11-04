#!/usr/bin/python3

from models.tags import Tag


TA = Tag()
TA.save()
print(TA.to_dict())