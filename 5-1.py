#5-1


s = input("Enter a string: ")
result = ""
for ch in s:
    if ch not in result:
        result += ch
print("After removing duplicates:", result)


#output:
#Enter a string: hello
#After removing duplicates: helo
