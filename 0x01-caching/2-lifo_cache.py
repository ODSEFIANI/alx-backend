#!/usr/bin/env python3
""" BaseCaching py module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    FIFO algo
    """

    def __init__(self):
        """
        Inherits from the basechavhin
        """
        super().__init__()
        self.lst = []

    def put(self, key, item):
        """
        Cache a key-value pair
        """
        if key is None or item is None:
            pass
        else:
            items = len(self.cache_data)
            if items >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.lst[-1]))
                del self.cache_data[self.lst[-1]]
                del self.lst[-1]
            if key in self.lst
                del self.lst[self.order.index(key)]
            self.lst.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value linked to a given key, or None
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
