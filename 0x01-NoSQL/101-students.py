#!/usr/bin/env python3

from pymongo import MongoClient
"""This module returns all students sorted by average score."""

def top_students(mongo_collection):
    """This function returns all students sorted by average score."""

    pipeline = [
            {
                "$addFields": {
                    "averageScore": { "$avg": "$scores" }
                }
            },

            {
                "$sort": { "averageScore": -1 }
            }
    ]

    result = list(mongo_collection.aggregate(pipeline))
    return result
