a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

# Check if valid triangle
if a < b + c and b < a + c and c < a + b:
    if a == b and b == c:
        print("The given triangle is Equilateral")
    elif a == b or b == c or a == c:
        print("The given triangle is Isosceles")
    else:
        print("The given triangle is Scalene")
else:
    print("The given sides do not form a valid triangle")
    #Enter the value of a: 3
#Enter the value of b: 5
#Enter the value of c: 4
#The given triangle is Scalene

