def is_even(n):
    """Return True if n is even, False otherwise."""
    return n % 2 == 0

# Driver program
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    if is_even(num):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
        Enter number 1: 6
#6 is even
#Enter number 2: 3
#3 is odd
#Enter number 3: 8
#8 is even
#Enter number 4: 9
#9 is odd
#Enter number 5: 4
#4 is even
