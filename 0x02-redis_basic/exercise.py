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

    def get(self, key: str, fn: callable = None):
        """
        Get a key-value pair from Redis
        """
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        Get a string from Redis
        """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """
        Get an int from Redis
        """
        return self.get(key, int)