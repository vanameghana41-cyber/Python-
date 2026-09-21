import re

text = "The numbers are 42 and 99."

pattern = r"\d+"
matches = re.findall(pattern, text)
print("findall:", matches)  
matches_iter = re.finditer(pattern, text)
for match in matches_iter:
    print("finditer:", match.group(), "at", match.span())
# Output:
# finditer: 42 at (16, 18)
# finditer: 99 at (23, 25)