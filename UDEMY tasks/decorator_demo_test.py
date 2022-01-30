from time import time
from functools import wraps

def speed_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = time()
        res = function(*args, **kwargs)
        end_time = time()
        print(f"time {end_time - start_time}")
        return res
    return wrapper()

@speed_time
def sum_lst():
    return sum([n for n in range(100000000)])

@speed_time
def sum_generator():
    return sum((n for n in range(100000000)))

print(sum_lst)
print(sum_generator)








