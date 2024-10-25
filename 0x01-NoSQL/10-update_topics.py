#!/usr/bin/env python3

"""This module changes the topics of a school document."""

def update_topics(mongo_collection, name, topics):
    """This function updates the topics of a document."""
    mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
    )

if __name__ == "__main__":
    pass
