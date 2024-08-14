#!/usr/bin/env python3
"""module for mongodb"""

from pymongo import MongoClient


def print_nginx_logs(dump):
    """function that returns the list of school having a specific topic"""
    print(f"{dump.count_documents({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {dump.count_documents({'method': 'GET'})}")
    print(f"\tmethod POST: {dump.count_documents({'method': 'POST'})}")
    print(f"\tmethod PUT: {dump.count_documents({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {dump.count_documents({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {dump.count_documents({'method': 'DELETE'})}")
    status_check_count = dump.count_documents(
        {'method': 'GET', 'path': '/status'}
    )
    print(f"{status_check_count} status check")


def main():
    """main function"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_logs(client.logs.nginx)


if __name__ == '__main__':
    main()