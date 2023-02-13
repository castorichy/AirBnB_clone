#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
""" Declaration of class BaseModels"""


class BaseModel:
    """ defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """ Declaration of public instance attributes,
        id, create_at and update_at
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value = datetime.\
                                strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)

    def __str__(self):
        """ Return a string representation of an instance in class basemodel"""

        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """updating the public instance attribute
            updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of dict
            key class must be added to dictionary with class name object
            create and updated must be converted to ISO format
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
