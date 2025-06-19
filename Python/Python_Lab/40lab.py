# Task 1: Implement a recursive function that calculates the factorial of a given nonnegative integer n.
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("Enter N:"))
print("factorial of 5 ",factorial(5))

# Task 2: Task 2: Implement a recursive function that calculates the nth Fibonacci number 
def fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("Enter N:"))
print("fibonacci number ",n,":",fibonacci(n))