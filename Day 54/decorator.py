import time
# current_time = time.time()
# print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        current_time = time.time()
        print(f"Runtime of {function.__name__} = {round(current_time - start_time, 5)} seconds.")
    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
