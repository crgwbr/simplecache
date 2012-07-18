from __init__ import Cache
from DummyCache import DummyCache
import unittest2
import time

class CacheTest(unittest2.TestCase):
    
    def test_backend_loader(self):
        cache1 = Cache("DummyCache")
        self.assertTrue(isinstance(cache1, Cache), "Cache did not instantiate properly")
        self.assertEqual(cache1.CacheBackend, DummyCache, "Cache backend was not imported correctly")
        self.assertTrue(isinstance(cache1.backend, DummyCache), "Cache Backend did not instantiate properly")
        
        cache2 = Cache(DummyCache)
        self.assertTrue(isinstance(cache2, Cache), "Cache did not instantiate properly")
        self.assertEqual(cache2.CacheBackend, DummyCache, "Cache backend was not imported correctly")
        self.assertTrue(isinstance(cache2.backend, DummyCache), "Cache Backend did not instantiate properly")
        
    def test_dummy_cache(self):
        cache = Cache("DummyCache")
        
        key = [1, 2, 3]
        value = "hello!"
        cache.set(key, value, 0)
        self.assertEqual(cache.get(key), value, "Set value is not equal to returned value")
        
        for lifespan in range(1, 11, 5):
            key = "a key"
            value = "a value"
            cache.set(key, value, lifespan)
            self.assertEqual(cache.get(key), value, "Set value is not equal to returned value")
            time.sleep(lifespan / 2.0)
            self.assertEqual(cache.get(key), value, "Set value is not equal to returned value")
            time.sleep(lifespan / 2.0)
            self.assertIsNone(cache.get(key), "Key should be expired")
    
    def test_generate_key(self):
        a = Cache.generate_key(1, 2, 3)
        b = Cache.generate_key(2, 3)
        c = Cache.generate_key(1, 2)
        self.assertNotEqual(a, b, "Cache keys should not be equal")
        self.assertNotEqual(a, c, "Cache keys should not be equal")
        self.assertNotEqual(b, c, "Cache keys should not be equal")
        
        a = Cache.generate_key(1.2, 2.23, 3.234)
        b = Cache.generate_key(2.654, 3.876)
        c = Cache.generate_key(1.123, 2.098)
        self.assertNotEqual(a, b, "Cache keys should not be equal")
        self.assertNotEqual(a, c, "Cache keys should not be equal")
        self.assertNotEqual(b, c, "Cache keys should not be equal")
        
        a = Cache.generate_key([1, 2, 3])
        b = Cache.generate_key([2, 3])
        c = Cache.generate_key([1, 2])
        self.assertNotEqual(a, b, "Cache keys should not be equal")
        self.assertNotEqual(a, c, "Cache keys should not be equal")
        self.assertNotEqual(b, c, "Cache keys should not be equal")
        
        a = Cache.generate_key({'a': 1, 'b': 2, 'c': 5})
        b = Cache.generate_key({'b': 2, 'c': 5})
        c = Cache.generate_key({'a': 1, 'b': 2})
        self.assertNotEqual(a, b, "Cache keys should not be equal")
        self.assertNotEqual(a, c, "Cache keys should not be equal")
        self.assertNotEqual(b, c, "Cache keys should not be equal")
    
    def test_singletons(self):
        a = Cache.get_instance('DummyCache')
        b = Cache.get_instance('DummyCache')
        self.assertEqual(a, b, "Multiple instances were created")
        self.assertEqual(hash(a), hash(b), "Multiple instances were created")
        
        a = Cache('DummyCache')
        b = Cache('DummyCache')
        self.assertNotEqual(a, b, "Multiple instances were not created")
        self.assertNotEqual(hash(a), hash(b), "Multiple instances were not created")
        
        
if __name__ == "__main__":
    unittest2.main()
        
        
        