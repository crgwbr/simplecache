from api.lib.cache import Cache
from api import settings
import unittest2


class CacheTest(unittest2.TestCase):
    def setUp(self):
        self.cache_settings = settings.CACHE
    
    def tearDown(self):
        settings.CACHE = self.cache_settings
        
    def test_generate_key(self):
        a = Cache.generate_key(1, 2, 3)
        b = Cache.generate_key(2, 3)
        c = Cache.generate_key(1, 2)
        self.assertNotEqual(a, b)
        self.assertNotEqual(a, c)
        self.assertNotEqual(b, c)
        
        a = Cache.generate_key(1.2, 2.23, 3.234)
        b = Cache.generate_key(2.654, 3.876)
        c = Cache.generate_key(1.123, 2.098)
        self.assertNotEqual(a, b)
        self.assertNotEqual(a, c)
        self.assertNotEqual(b, c)
        
        a = Cache.generate_key([1, 2, 3])
        b = Cache.generate_key([2, 3])
        c = Cache.generate_key([1, 2])
        self.assertNotEqual(a, b)
        self.assertNotEqual(a, c)
        self.assertNotEqual(b, c)
        
        a = Cache.generate_key({'a': 1, 'b': 2, 'c': 5})
        b = Cache.generate_key({'b': 2, 'c': 5})
        c = Cache.generate_key({'a': 1, 'b': 2})
        self.assertNotEqual(a, b)
        self.assertNotEqual(a, c)
        self.assertNotEqual(b, c)
        
    def test_dummy_cache(self):
        settings.CACHE['backend'] = "DummyCache"
        cache = Cache()
        key = [1, 2, 3]
        cache.set(key, "hello!", 0)
        self.assertEqual(cache.get(key), "hello!")
        
        
        
        
        