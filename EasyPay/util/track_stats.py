from functools import wraps


def tracker(call):
    def decorator_tracker(method):
        @wraps(method)
        def wrapper(*args, **kw):
            method(*args, **kw)
            call()
        return wrapper
    return decorator_tracker
