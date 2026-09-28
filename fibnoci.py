def fibonacci(n):
    if n <= 0:
        return "Invalid input!"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
for i in range(1, 16):
    print(fibonacci(i), end=" ")
    '''0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 

