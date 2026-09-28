import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def heavy_task():
    return sum(range(10_000_000))

heavy_task()
#heavy_task took 0.3288 seconds
