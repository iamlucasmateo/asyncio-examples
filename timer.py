import time

def timer(func):
    start_time = time.time()
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    print(f"Running the whole thing took {time.time() - start_time}")
    return inner
