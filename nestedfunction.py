def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
my_counter = make_counter()

print(my_counter())  
print(my_counter())  
print(my_counter())  
'''1
2
3'''
