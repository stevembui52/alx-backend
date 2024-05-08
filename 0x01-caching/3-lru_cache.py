#!/usr/bin/python3
"""Create LRUCache class that inherits from BaseCaching"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ Define LRUCache """

    def __init__(self):
        """ Initialize LRUCache """
        self.queue = []
        super().__init__()

    def put(self, key, item):
                print('DISCARD: {}'.format(delete))

    def get(self, key):
        """ Return the value associated with the given key """
        if self.cache_data.get(key):
            self.queue.remove(key)
            self.queue.append(key)
        return self.cache_data.get(key)
