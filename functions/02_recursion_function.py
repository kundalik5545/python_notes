'''
Recursion function in python

Recursion is a programming technique where a function calls itself in order to solve a problem. A recursive function typically has two main components: a base case that stops the recursion, and a recursive case that breaks the problem into smaller subproblems.
'''

n = int(input("Enter a number: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
fact = factorial(n)
print(f"The factorial of {n} is {fact}")

