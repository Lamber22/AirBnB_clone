#!/usr/bin/python3
# base_model.py

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
        
        format_str = '%Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, format_str)
                else:
                    self.__dict__[k] = v

    def save(self):
        """Update updated_at with the current datetime"""
        self.updated_at = datetime.now()
                
