#!/usr/bin/python3

import functools


def cache(func):
    """create a cache to where the key is the args and return cache
    if available
    """
    functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = str(args + tuple(kwargs))
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache

@cache
def fibo(n):
    """Recursively finds the fibonacci"""
    if n <= 2:
        return n
    return fibo(n - 1) + fibo(n - 2)

print(fibo(50))
