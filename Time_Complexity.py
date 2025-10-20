import time

def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def analyze_time(n):
    print(f"\nAnalyzing for n = {n}")
    start = time.time()
    fib_recursive(n)
    end = time.time()
    print(f"Recursive Fibonacci Time: {end - start:.6f} seconds")

    start = time.time()
    fib_iterative(n)
    end = time.time()
    print(f"Iterative Fibonacci Time: {end - start:.6f} seconds")

# Just run it directly
print("Comparing Recursive vs Iterative Time Complexity for Fibonacci Sequence")
for n in [10, 20, 30, 35]:
    analyze_time(n)
