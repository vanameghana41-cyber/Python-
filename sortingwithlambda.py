students = [("Ravi", 78), ("Sita", 92), ("Amit", 65)]
sorted_students = sorted(students, key=lambda s: s[1], reverse=True)
print("Sorted by marks:", sorted_students)
words = ["apple", "cat", "banana", "dog", "elephant"]
sorted_words = sorted(words, key=lambda w: len(w))
print("Sorted by length:", sorted_words)
'''Sorted by marks: [('Sita', 92), ('Ravi', 78), ('Amit', 65)]
Sorted by length: ['cat', 'dog', 'apple', 'banana', 'elephant']'''
