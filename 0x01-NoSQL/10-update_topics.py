#!/usr/bin/env python3
"""Change school topics"""


def update_topics(mongo_collection, name, topics):
    """
    Function that changes all topics
    """
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
