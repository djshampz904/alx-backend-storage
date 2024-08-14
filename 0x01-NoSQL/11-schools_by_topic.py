#!/usr/bin/env python3
"""
List of school hava a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """Return the list of school having a specific topic"""
    return mongo_collection.find({"topics": topic})
