counter = 0

def show_local():
    counter = 10
    print("Local counter inside function:", counter)

show_local()
print("Global counter outside function:", counter)
'''Local counter inside function: 10
Global counter outside function: 0'''
