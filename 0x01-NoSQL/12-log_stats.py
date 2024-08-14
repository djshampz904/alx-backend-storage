#!/usr/bin/env python3
"""
Provides some stats about Nginx logs stored in MongoDB
"""


from pymongo import MongoClient
list_all = __import__('8-all').list_all

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.logs.nginx
    log_count = school_collection.count_documents({})
    print("{} logs".format(log_count))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = school_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, method_count))
    status_check = school_collection.count_documents(
        {
            "method": "GET",
            "path": "/status"
        }
    )
    print("{} status check".format(status_check))
