from __init__ import Cache
import unittest2
import time

class CacheTest(unittest2.TestCase):
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
        
    def test_dummy_cache(self):
        cache = Cache("DummyCache")
        
        key = [1, 2, 3]
        value = "hello!"
        cache.set(key, value, 0)
        self.assertEqual(cache.get(key), value, "Set value is not equal to returned value")
        
        for lifespan in range(1, 20, 5):
            key = "a key"
            value = "a value"
            cache.set(key, value, lifespan)
            self.assertEqual(cache.get(key), value, "Set value is not equal to returned value")
            time.sleep(lifespan / 2.0)
            self.assertEqual(cache.get(key), value, "Set value is not equal to returned value")
            time.sleep(lifespan / 2.0)
            self.assertIsNone(cache.get(key), "Key should be expired")
        
        
if __name__ == "__main__":
    unittest2.main()
        
        
        