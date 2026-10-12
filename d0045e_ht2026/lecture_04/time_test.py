from timeit import timeit

def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)

iterations = 5
total_time = timeit("fib(50)", number=iterations, globals=globals())

print(f"Average time is {total_time / iterations:.2f} seconds")