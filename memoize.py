def memoize(key, time=0):
    """Decorator to memoize functions using memcache.
         @param key: The key to use for the cache. The key can either be:
         1. A function: It will be called with *args and **kwargs that were passed to the function being decorated
         2. A string.
    """
    def decorator(fxn):
        def wrapper(*args, **kwargs):
            # is it a function? then just call the function
            cache_key = calculate_cache_key(key, *args, **kwargs)
            if not cache_key:
                return fxn(*args, **kwargs)
            data = memcache.get(cache_key)
            if data is not None:
                return data
            # If not found in cache, call the wrapped function
            data = fxn(*args, **kwargs)
            # Then save the results
            memcache.set(cache_key, data, time)
            return data
        return wrapper
    return decorator

def invalidates_cache(key):
    def decorator(fxn):
        def wrapper(*args, **kwargs):
            # is it a function? then just call the function
            cache_key = calculate_cache_key(key, *args, **kwargs)
            # Sometimes, we need to clear more than one cache_element, e.g. attendance record which
            is_list = False
            if isinstance(cache_key, list):
                is_list = True
                memcache.delete_many(cache_key)
            else:
                memcache.delete(cache_key)
            #Now call the wrapped function
            return fxn(*args, **kwargs)
        return wrapper
    return decorator
