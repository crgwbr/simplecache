from time import time

class DummyCache():
    def get(self, key):
        return None
    
    def set(self, key, value, expire):
        return True
