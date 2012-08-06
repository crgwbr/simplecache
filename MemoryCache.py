from time import time

class MemoryCache():
    def __init__(self, **kwargs):
        self.cache = {}
        self.timeout = {}
    
    def get(self, key):
        timeout = self.timeout.get(key, 0)
        if timeout == 0 or timeout > time():
            return self.cache.get(key)
        
        if self.timeout.has_key(key):
            del self.timeout[key]
            del self.cache[key]
        
        return None
    
    def set(self, key, value, expire):
        self.timeout[key] = 0 if expire == 0 else (time() + expire)
        self.cache[key] = value
        return True
