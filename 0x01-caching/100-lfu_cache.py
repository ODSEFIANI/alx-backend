#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    class
    """

    def __init__(self):
        """
        Innheritance
        """
        super().__init__()
        self.usg = []
        self.frequ = {}

    def put(self, key, item):
        """
        dictionnary
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                lfu = min(self.frequ.values())
                lfu_keys = []
                for k, v in self.frequ.items():
                    if v == lfu:
                        lfu_keys.append(k)
                if len(lfu_keys) > 1:
                    lru_lfu = {}
                    for k in lfu_keys:
                        lru_lfu[k] = self.usg.index(k)
                    discard = min(lru_lfu.values())
                    discard = self.usg[discard]
                else:
                    discard = lfu_keys[0]

                print("DISCARD: {}".format(discard))
                del self.cache_data[discard]
                del self.usg[self.usg.index(discard)]
                del self.frequ[discard]
            if key in self.frequ:
                self.frequ[key] += 1
            else:
                self.frequ[key] = 1
            if key in self.usg:
                del self.usg[self.usg.index(key)]
            self.usg.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve
        """
        if key is not None and key in self.cache_data.keys():
            del self.usg[self.usg.index(key)]
            self.usg.append(key)
            self.frequ[key] += 1
            return self.cache_data[key]
        return None
