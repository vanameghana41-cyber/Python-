import re

sentence = "1024 requests were served in 3 seconds"
m = re.match(r"\d", sentence)
print("Match result:", m)
s = re.search(r"served", sentence)
print("Search result:", s)  
print("Span of 'served':", s.span())
f1 = re.fullmatch(r"\d+", "12345")
print("Fullmatch on '12345':", f1) 
f2 = re.fullmatch(r"\d+", "123a5")
print("Fullmatch on '123a5':", f2) 