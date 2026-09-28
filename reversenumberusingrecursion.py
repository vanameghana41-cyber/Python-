def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)

print("Sum of digits:", sum_of_digits(12345))
print("Reversed number:", reverse_number(12345))
'''Sum of digits: 15
Reversed number: 54321'''
