numbers = [1, 2, 3]
print("Initial list:", numbers)
numbers.append(4)
print("After append:", numbers)
numbers.insert(1, 10)
print("After insert:", numbers)
numbers.extend([5, 6])
print("After extend:", numbers)
numbers.remove(10)
print("After remove:", numbers)
popped = numbers.pop()
print("After pop:", numbers, "| Popped:", popped)
numbers.sort()
print("After sort:", numbers)
numbers.reverse()
print("After reverse:", numbers)
print("Count of 2:", numbers.count(2))
print("Index of 3:", numbers.index(3))
'''Initial list: [1, 2, 3]
After append: [1, 2, 3, 4]
After insert: [1, 10, 2, 3, 4]
After extend: [1, 10, 2, 3, 4, 5, 6]
After remove: [1, 2, 3, 4, 5, 6]
After pop: [1, 2, 3, 4, 5] | Popped: 6
After sort: [1, 2, 3, 4, 5]
After reverse: [5, 4, 3, 2, 1]
Count of 2: 1
Index of 3: 2'''
