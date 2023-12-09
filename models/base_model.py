#!/usr/bin/python3
# base_model.py

import models
from uuid import uuid4
from datetime import datetime

"""Defines a base class that defines all attributes/methods for other classes"""

class BaseModel:
    """Represents the Base class for this project"""

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel.

        Args:
            *args (any) - any 
            **kwargs(dict) - key/value pairs of attributes
        """
        
        t_format = '%Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, t_format)
                else:
                    self.__dict__[k] = v

    def save(self):
        """Update updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return f"[{clname}] ({self.id}) {self.__dict__}"
