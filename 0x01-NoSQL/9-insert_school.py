#!/usr/bin/env python3
"""Module to insert a new document in a MongoDB collection"""

def insert_school(mongo_collection, **kwargs):
    """This function inserts a new document in a collection."""
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id

if __name__ == "__main__":
    pass
