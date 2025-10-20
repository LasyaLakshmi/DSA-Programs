n = int(input("Enter No.of series: "))

# Factorial series
def factorial(n):
    if n < 0:
        return "factorial is not defined for negative numbers"
    elif n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

# Fibonacci series
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Test
print(f"Factorial of {n} is ",factorial(n))

if n <= 0:
    print("Please enter a positive integer to generate the Fibonacci series.")
else:
    print(f"Fibonacci of {n} is :")
    for i in range(n):
        print(fibonacci(i), end=" ")