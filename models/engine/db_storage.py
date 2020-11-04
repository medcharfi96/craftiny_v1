#!/usr/bin/python3
"""
class DBStorage
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import models
from models.Model_Com import BaseModel, Base
from models.user import User
from models.article import Article
from models.likes import Likes
from models.comment import Comment
from models.product import Products
from models.tags import Tag
from models.category import Category

classes = {"BaseModel": BaseModel, "User": User, "Article": Article, "Likes": Likes, "Comment": Comment, "Product": Products, "Tags": Tag, "Category": Category}

class DBStorage():
    """DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Inisialisation of class DBStorage"""
        MYSQL_USER = "craft_user_v1"
        MYSQL_PWD = "12345"
        MYSQL_HOST = "localhost"
        MYSQL_DB = "craftiny_v1"
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(MYSQL_USER,
                                             MYSQL_PWD,
                                             MYSQL_HOST,
                                             MYSQL_DB,
                                             pool_pre_ping=True))

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def check(self, cls=None, email="str"):
        """check the user connected """
        val_list = self.__session.query(cls).all()
        for user in val_list:
            if email == user.email:
                return 1
        else:
            return 0

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """save all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reload data from db"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """close session methode"""
        self.__session.close()

    def get(self, cls, id):
        """
        REturn object from class name
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def checkbysecurecode(self, userid, securecode):
        """
        Returns the object of class Token
        """


        all_cls = models.storage.all(Token)
        for value in all_cls.values():
            if value.securecode == securecode and value.user_id == userid:
                return value

        return None

    def checkbysecurecode(self, userid, securecode):
        """
        Returns the object of class Token
        """


        all_cls = models.storage.all(Token)
        for value in all_cls.values():
            if value.securecode == securecode and value.user_id == userid:
                return value

        return None

    def getbyemail(self, cls, email):
        """
        Return user by email
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.email.upper() == email.upper()):
                return value

        return None

    def craft_nbr(self, cls, user_id):
        """count number of craft"""


        if cls not in classes.values():
            return None

        if user_id is not None:
            follow_list = models.storage.get_by_followed_id(cls, user_id)
            number_of_follow = len(follow_list)
            return (str(number_of_follow))



    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count

    def getlist_by_attr(self, cls, user_id, follower_id=None):
        """
        get all craft by user id
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        list_val = []
        for value in all_cls.values():
            if value.user_id == user_id:
                if cls == Post:
                    new_post_dict = value.to_dict()
                    new_post_dict["number_of_reaction"] = value.number_of_reaction()
                    if follower_id is not None:
                        if value.check_if_user_reacted(follower_id):
                            new_post_dict["react_status"] = "1"
                        else:
                            new_post_dict["react_status"] = "0"
                    list_val.append(new_post_dict)
                else:
                    list_val.append(value.to_dict())

        if cls == Post:
            models.storage.sort_posts(list_val)

        return list_val


    def sort_posts(self, post_lists):
        """sort a list of craft by creation date"""
        my_new_list = post_lists
        my_new_list.sort(key=lambda date: date["creation_date"])
        my_new_list.reverse()
        return my_new_list
