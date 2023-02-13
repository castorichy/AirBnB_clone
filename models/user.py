#!/usr/bin/python3
from models.base_model import BaseModel
"""declaration of class user"""

class User(BaseModel):
    """class user that inherys from basemodel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

