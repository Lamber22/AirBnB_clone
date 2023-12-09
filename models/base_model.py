#!/usr/bin/python3
# base_model.py
<<<<<<< HEAD

=======
"""Defines the BaseModel class that defines all attributes and methods
for other classes.
"""
>>>>>>> 71081dfbc4af658dc1cfbfe35157e2f7911d183a
import models
from uuid import uuid4
from datetime import datetime

<<<<<<< HEAD
"""Defines a base class that defines all attributes/methods"""

=======
>>>>>>> 71081dfbc4af658dc1cfbfe35157e2f7911d183a

class BaseModel:
    """Represents the Base class for HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel.

        Args:
<<<<<<< HEAD
            *args (any) - any
            **kwargs(dict) - key/value pairs of attributes
        """
        t_format = '%Y-%m-%dT%H:%M:%S.%f'
=======
            *args (any) - Unused.
            **kwargs(dict) - key/value pairs of attributes.
        """

        tform = "%Y-%m-%dT%H:%M:%S.%f"
>>>>>>> 71081dfbc4af658dc1cfbfe35157e2f7911d183a
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
<<<<<<< HEAD
                    self.__dict__[k] = datetime.strptime(v, t_format)
=======
                    self.__dict__[k] = datetime.strptime(v, tform)
>>>>>>> 71081dfbc4af658dc1cfbfe35157e2f7911d183a
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime"""
<<<<<<< HEAD
        self.updated_at = datetime.now()
=======
        self.updated_at = datetime.today()
>>>>>>> 71081dfbc4af658dc1cfbfe35157e2f7911d183a
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
<<<<<<< HEAD

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
=======
        Includes the key/value pair __class__ representing
        the class name of the object.
        """"

        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__clas__.__name__
>>>>>>> 71081dfbc4af658dc1cfbfe35157e2f7911d183a
        return rdict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
<<<<<<< HEAD
        return f"[{clname}] ({self.id}) {self.__dict__}"
=======
        return = "[{}] ({})".format(clname, self.id, self.__dict__)
>>>>>>> 71081dfbc4af658dc1cfbfe35157e2f7911d183a
