"""
cache implementation
use queue structure to implement the FIFO algorithm.
provide the basic methods like get, set, and clear ...
"""


from queue import Queue


class Cache:
    # init the cache and set the max size to 16 bits.
    def __init__(self) -> None:
        self.cache = Queue(maxsize=16)

    # get method
    def get_cache(self, location):
        # return the value at that location,
        # if not exist, return none by default.
        for cache in self.cache.queue:
            if location in cache.keys():
                return cache[location]

    # set method
    def set_cache(self, location, value):
        # check if the cache is full
        if self.cache.full():
            self.cache.get()
        # check if the data is already in the cache
        # data could come from user or memory
        # if it comes from user, you have to update the memory also. I think that should not be implement here.
        for cache in self.cache.queue:
            if location in cache.keys():
                cache[location] = value
                return
        # if none of above if true, just update the cache.
        self.cache.put({location: value})

    # clear the cache.
    def clear_cache(self):
        while not self.cache.empty():
            try:
                self.cache.get(False)
            except:
                continue
            self.cache.task_done()

    # cache iteration.
    def print_cache(self):
        for cache in self.cache.queue:
            print(cache)
