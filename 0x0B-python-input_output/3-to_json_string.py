#!/usr/bin/python3
""" Module defining the fucntion `` """
import json


def to_json_string(my_obj):
    """ function that returns the JSON representation of an object (string):

        Args:
            my_obj -- The object used to return JSON repr

        Returns:
            The JSON representation of the obj
    """
    return json.loads(my_obj)
