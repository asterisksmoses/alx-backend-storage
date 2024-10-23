#!/usr/bin/env python3

"""This module lists all the documents in a MongoDB collection."""

def list_all(mongo_collection):
    """This function lists all documents in a mongo collection."""
    docs = list(mongo_collection.find())
    return docs if docs else {}

if __name__ == "__main__":
    pass
