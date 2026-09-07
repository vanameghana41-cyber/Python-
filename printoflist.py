items = input("Enter 12 elements separated by spaces: ")
my_list = items.split()
if len(my_list) == 12:
    middle_elements = my_list[4:8]
    print("Original list:", my_list)
    print("Middle 4 elements:", middle_elements)
else:
    print("Please enter exactly 12 elements.")
