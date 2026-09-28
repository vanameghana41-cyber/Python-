counter = 0

def increment_counter():
    global counter
    counter += 1
    print("Counter after increment:", counter)

# Call 5 times
for i in range(5):
    increment_counter()
'''Counter after increment: 1
Counter after increment: 2
Counter after increment: 3
Counter after increment: 4
Counter after increment: 5'''
