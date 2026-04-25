from functools import lru_cache

@lru_cache(maxsize=None)
def fib_number(n: int) -> int:
    if n <= 2:
        return 1
    return fib_number(n - 1) + fib_number(n - 2)


print(fib_number(5))
print(fib_number(6))
print(fib_number(8))
print(fib_number(50))