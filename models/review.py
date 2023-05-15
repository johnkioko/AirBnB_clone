#!/usr/bin/python3
"""Review class creation"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review attributes"""
    place_id = ""
    user_id = ""
    text = ""
