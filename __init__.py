import api.settings

import pickle

class Cache():
    def __init__(self):
        self.settings = settings = api.settings.CACHE
        
        backend_name = settings['backend']
        import_path = __name__.split('.')
        import_path.append(backend_name)
        import_path = ('.').join(import_path)
        self.CacheModule = __import__(import_path, fromlist=[backend_name])
        self.CacheBackend = getattr(self.CacheModule, backend_name)
        self.backend = self.CacheBackend(**settings)
    
    @classmethod
    def generate_key(cls, *args):
        params = pickle.dumps(args)
        return hash(params)
    
    def get(self, key):
        if not isinstance(key, basestring):
            key = self.generate_key(key)
        
        return self.backend.get(key)
    
    def set(self, key, value, expire):
        if not isinstance(key, basestring):
            key = self.generate_key(key)
        
        return self.backend.set(key, value, expire)
