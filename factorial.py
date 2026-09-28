def factorial(n):
    if n < 0:
        return "Invalid input! Factorial not defined for negatives."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
def factorial_iterative(n):
    if n < 0:
        return "Invalid input!"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("Recursive:", factorial(5))
print("Iterative:", factorial_iterative(5))
'''Recursive: 120
Iterative: 120'''
