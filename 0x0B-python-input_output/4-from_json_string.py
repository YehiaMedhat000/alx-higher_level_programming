#!/usr/bin/python3
""" Module defining the fucntion `` """
import json


def from_json_string(my_str):
    """ function that returns an object (Python data structure)
        represented by a JSON string:

        Args:
            my_str -- The string used to return JSON string

        Returns:
            The JSON string of the obj
    """
    return json.dumps(my_str)
