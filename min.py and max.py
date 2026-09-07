numbers = [5, 8, 2, 10, 3]
maximum = numbers[0]
minimum = numbers[0]
total = 0
for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
    total += num

print("List:", numbers)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Sum:", total)
List: [5, 8, 2, 10, 3]
'''Maximum: 10
Minimum: 2
Sum: 28'''
