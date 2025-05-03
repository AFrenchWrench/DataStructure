from math import ceil, log, sqrt
from time import perf_counter
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        end_time = perf_counter()
        duration = end_time - start_time
        print(f"[TIMER] Function '{func.__name__}' executed in {duration:.6f} seconds.")
        return result

    return wrapper


@timer
def fib(n):
    phi = (1 + sqrt(5)) ** n
    psi = (1 - sqrt(5)) ** n
    coef = sqrt(5) / (5 * (2**n))
    return int(coef * (phi - psi))


def fib_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


@timer
def run_fib_recursive(n):
    return fib_recursive(n)


n = int(input())
print(fib(n))
print(run_fib_recursive(n))
