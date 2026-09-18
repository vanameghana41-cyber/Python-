#3-4


s = input("Enter a string: ")
ch = input("Enter the character: ")
first = s.find(ch)
last = s.rfind(ch)
if first == -1:
    print("Character not found")
else:
    print("First occurrence index:", first)
    print("Last occurrence index:", last)


#output:
#Enter a string: hello
#Enter the character: hlo
#Character not found
    
