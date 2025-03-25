#43
#Write a Python program to create Fibonacci series up to n using Lambda.

n = int(input("Enter the number for creating fibonacci : "))

fibonacci = lambda n, a=0, b=1: [a] if n == 1 else [a] + fibonacci(n-1, b, a+b)

print(f"Fibonacci Series up to {n} terms:", fibonacci(n))