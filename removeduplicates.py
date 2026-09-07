my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)

print("Original list:", my_list)
print("List without duplicates:", unique_list)
'''Original list: [1, 2, 2, 3, 4, 4, 5]
List without duplicates: [1, 2, 3, 4, 5]'''
