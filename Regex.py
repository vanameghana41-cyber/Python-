import re
paragraph = "NASA launched a rocket from the USA to study the ATMOSPHERE and ENVIRONMENT."
caps_words = re.findall(r'\b[A-Z]{2,}\b', paragraph)
print("All CAPS words:", caps_words)
print("Words longer than 6 characters with start index:")
for match in re.finditer(r'\b\w{7,}\b', paragraph)
print(f"Word: {match.group()}, Start index: {match.start()}")
prices = "apples: $3.50, bananas: $1.20, mango: $4.75"
amounts = re.findall(r'\$\d+\.\d{2}', prices)
print("Dollar amounts:", amounts)
count = len(amounts)
print("Number of dollar amounts found:", count)
