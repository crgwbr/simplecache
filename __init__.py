import pickle

class Cache():
    def __init__(self, backend, **config):
        self.config = config
        
        self.CacheModule = __import__(backend, fromlist=[backend])
        self.CacheBackend = getattr(self.CacheModule, backend)
        self.backend = self.CacheBackend(**config)
    
    @classmethod
    def generate_key(cls, *args):
        params = pickle.dumps(args)
        return hex(hash(params))
    
    def get(self, key):
        if not isinstance(key, basestring):
            key = self.generate_key(key)
        
        return self.backend.get(key)
    
    def set(self, key, value, expire = 0):
        if not isinstance(key, basestring):
            key = self.generate_key(key)
        
        return self.backend.set(key, value, expire)
