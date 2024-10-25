#!/usr/bin/env python3

"""This module returns the list of school
having a specific topic."""

def schools_by_topic(mongo_collection, topic):
    """This function finds a list of school with a
    specific topic."""

    return list(mongo_collection.find({"topics": topic}))

if __name__ == "__main__":
    pass
