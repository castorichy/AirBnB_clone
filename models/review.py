#!/usr/bin/python3
from models.base_model import BaseModel

"""declaration of class review"""


class Review(BaseModel):
    """Public class attributes"""
    place_id = ""
    user_id = ""
    text = ""
