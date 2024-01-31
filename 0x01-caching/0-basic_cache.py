#!/usr/bin/env python3
""" module BaseCaching py
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Cashing class
    """

    def __init__(self):
        """
        Initialization
        """
        BaseCaching.__init__(self)

    def get(self, key):
        """retrieve the data
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None

    def put(self, key, item):
        """use a dictionary as cache
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
