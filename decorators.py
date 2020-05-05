from functools import wraps

def mydeco(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print('decorated by deco')
        return f(*args, **kwargs)
    return wrapper
    