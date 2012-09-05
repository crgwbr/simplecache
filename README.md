# SimpleCache

SimpleCache is a simple Python cache wrapper designed for performance web 
applications. It's very lightweight and supports multiple caching backends 
like Memcache, DummyCache (a fake, in-memory cache designed for 
development), and FileCache.

SimpleCache is in *active* development and is still very alpha. This isn't 
recommended for anyone who doesn't feel like debugging an infinite black 
hole of bugs.

## Usage

The Cache class (the main interface of SimpleCache) is not technically a 
singleton since it fully supports multiple instances. While you may wish 
to create multiple instances sometimes, for most cases you'll only want 
a single instance to be created.

Here's a simple example of how you can instantiate an use SimpleCache:

    >>> from simplecache import Cache
    >>> cache = Cache.get_instance('DummyBackend')
    >>> # Cache a value that will never expire
    >>> #         Cache Key       Cache Value  Expire In (seconds)
    >>> cache.set('My Cache Key', 3.141592654, 0)
    3.141592654
    
    >>> # Cache a value to expire in 120 seconds
    >>> cache.set('Hello!', ['how', 'are', 'you', '?'], 120)
    ['how', 'are', 'you', '?']
    
    >>> # Get a cached value
    >>> # Returns None if the value is expired or if it was never set
    >>> cache.get('Hello!')
    ['how', 'are', 'you', '?']
    
    >>> # Wait for key expire
    >>> import time
    >>> time.sleep(130)
    >>> cache.get('Hello!')
    None
    
    >>> # Lists, Dicts, Tuples, Ints, Strings all work as keys
    >>> cache.set(['a', 1, 'z', 4], 'hi there', 0)
    'hi there'
    
    