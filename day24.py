class LRUCache:
    
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.max_size = capacity
        self.current_size = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key]
            self.cache.move_to_end(key)
            return val
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
            return
        if self.current_size>=self.max_size:
            self.cache.popitem(last=False) # last=False sets FIFO like pop
            self.current_size-=1
        self.cache[key] = value
        self.current_size+=1