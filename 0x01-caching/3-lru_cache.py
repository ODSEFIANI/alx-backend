#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Lruchache
    """
    def __init__(self):
        """
        Innherits
        """
        super().__init__()
        self.usg = []

    def put(self, key, item):
        """
        dictioanry
        """
        if key is None or item is None:
            pass
        else:
            items = len(self.cache_data)
            if items >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.usg[0]))
                del self.cache_data[self.usg[0]]
                del self.usg[0]
            if key in self.usg:
                del self.usg[self.usg.index(key)]
            self.usg.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        retrive
        """
        if key is not None and key in self.cache_data.keys():
            del self.usg[self.usg.index(key)]
            self.usg.append(key)
            return self.cache_data[key]
        return None
