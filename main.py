import logging

def log_func(func):
    def decorator(*args ,**kwargs):
        logging.info(f"Calling {func.__name__} with args={args} , kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorator


@log_func
def my_func(a,b):
    # print("whar")
    return a+b

print(my_func(1,2))