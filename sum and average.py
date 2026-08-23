
num = int(input("Enter a number: "))
sum_digits = 0
count = 0
temp = num   
while temp > 0:
    digit = temp % 10       
    sum_digits += digit      
    count += 1               
    temp //= 10              

average = sum_digits / count

print("Sum of digits =", sum_digits)
print("Average of digits =", average)
#Enter a number: 63
#Sum of digits = 9
#Average of digits = 4.5
