items = {"pen": 10, "book": 50, "pencil": 5, "bag": 200}
sorted_items = sorted(items.items(), key=lambda x: x[1])
print("Items sorted by price:", sorted_items)
'''Items sorted by price: [('pencil', 5), ('pen', 10), ('book', 50), ('bag', 200)]'''
