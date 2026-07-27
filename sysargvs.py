# sum_two.py
import sys

# Print script name and total arguments
print("Script name:", sys.argv[0])
print("Total arguments passed:", len(sys.argv))

# Expecting exactly 3 arguments: script name + 2 numbers
if len(sys.argv) != 3:
    print("Usage: python sum_two.py <num1> <num2>")
else:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print("Sum:", a + b)
