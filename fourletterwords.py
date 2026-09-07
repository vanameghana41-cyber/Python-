words = ["apple", "cat", "banana", "dog", "elephant"]
long_words = [w for w in words if len(w) > 4]
print("Original words:", words)
print("Words with >4 letters:", long_words)
'''Original words: ['apple', 'cat', 'banana', 'dog', 'elephant']
Words with >4 letters: ['apple', 'banana', 'elephant']'''
