numbers = [5, -3, 7, -1, 0, 4, -8]
new_list = [x if x >= 0 else 0 for x in numbers]
print("Original list:", numbers)
print("After replacing negatives:", new_list)
'''Original list: [5, -3, 7, -1, 0, 4, -8]
After replacing negatives: [5, 0, 7, 0, 0, 4, 0]'''
