#!/usr/bin/python3

from models.category import Category


CA = Category()
CA.save()
print(CA.to_dict())