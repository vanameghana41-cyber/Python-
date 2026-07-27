# Simple program to take multiple values and print their sum

numbers = input("Enter numbers separated by spaces: ")
nums = numbers.split()                                  
total = sum(map(int, nums))                            
print("Sum =", total)
