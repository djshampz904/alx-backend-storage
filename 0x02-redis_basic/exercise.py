#!/usr/bin/env python3
"""
Create a cache class that stores a key-value pair in Redis
"""
from typing import Union
import redis
import uuid


class Cache:
    """
    Cache class
    """

    def __init__(self):
        """
        Constructor
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store a key-value pair in Redis
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
