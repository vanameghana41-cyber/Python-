#5-2

s = input("Enter a string: ")
if s.isdigit():
    print("String contains only digits")
elif s.isalpha():
    print("String contains only alphabets")
elif s.isalnum():
    print("String is alphanumeric")
else:
    print("String contains special characters")



 #output:
# Enter a string: hello
#String contains only alphabets
   
