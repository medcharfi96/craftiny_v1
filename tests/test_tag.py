#!/usr/bin/python3

from models.tags import Tag


TA = Tag()
TA.label = "el nik lil sbeh"
TA.save()
print(TA.to_dict())