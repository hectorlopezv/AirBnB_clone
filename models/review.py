#!/usr/bin/python3
"""Module for Amenity class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class representing a Amenity."""
    place_id = ""
    user_id = ""
    text = ""
