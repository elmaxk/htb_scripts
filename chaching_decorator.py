#!/usr/bin/env python


"""
This module provides simple memoization arguments
that are able to store cached return results of
decorated function for specified period of time.
"""

import time
import hashlib
import pickle


cache = {}


def is_obsolete(entry, duration):
    """Check if a given entry is obsolete"""
    return time.time() - entry['time'] > duration


def compute_key(function, args, kw):
    """Compute caching key for given value"""
    key = pickle.dumps((function.__name__, args, kw))
    return hashlib.sha1(key).hexdigest()

def memoize(duration=10):
    """Keyword-aware memoization decorator

    It allows to memoize function arguments for specified
    duration time.
    """

    def _memoize(function):
        def __memoize(*args, **kw):
            key = compute_key(function, args, kw)

            # do we have it already in cache?
            if (
                key in cache and
                not is_obsolete(cache['key'], duration)
            ):
                # return cached value if it exists
                # and isn't too old
                print('We have a winner')
                return cache[key]['value']

            # compute result if there is no
            # valid cache available

            result = function(*args, **kw)
            # store result for later use
            cache[key] = {
                'value': result,
                'time': time.time()
            }
            return result
        return __memoize
    return _memoize