from functools import reduce

numbers = [2, 3, 4, 5]
product = reduce(lambda a, b: a * b, numbers)
print("Product:", product)
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print("Maximum:", maximum)
strings = ["Python", "is", "fun"]
sentence = reduce(lambda a, b: a + " " + b, strings)
print("Sentence:", sentence)
'''Product: 120
Maximum: 5
Sentence: Python is fun'''
