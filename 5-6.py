#5-6


s = input("Enter a string: ")
sub = input("Enter the substring: ")
position = -1
for i in range(len(s) - len(sub) + 1):
    if s[i:i + len(sub)] == sub:
        position = i
        break
print("First occurrence index:", position)
count = 0
for i in range(len(s) - len(sub) + 1):
    if s[i:i + len(sub)] == sub:
        count += 1
print("Number of occurrences:", count)


#output:
#Enter a string: hello
#Enter the substring: hel
#First occurrence index: 0
#Number of occurrences: 1

