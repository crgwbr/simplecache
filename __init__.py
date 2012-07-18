import pickle

singletons = {}

class Cache():
    def __init__(self, backend, **config):
        self.config = config
        
        if isinstance(backend, basestring):
            cache_module = __import__(backend, fromlist=[backend])
            self.CacheBackend = getattr(cache_module, backend)
        else:
            self.CacheBackend = backend
        
        self.backend = self.CacheBackend(**config)
    
    @classmethod
    def generate_key(klass, *args):
        params = pickle.dumps(args)
        return hex(hash(params))
    
    @classmethod
    def get_instance(klass, backend_name):
        if singletons.has_key(backend_name):
            return singletons[backend_name]
        inst = klass(backend_name)
        singletons[backend_name] = inst
        return inst
    
    def get(self, key):
        if not isinstance(key, basestring):
            key = self.generate_key(key)
        
        return self.backend.get(key)
    
    def set(self, key, value, expire = 0):
        if not isinstance(key, basestring):
            key = self.generate_key(key)
        
        return self.backend.set(key, value, expire)
