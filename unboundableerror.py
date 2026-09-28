counter = 0

def wrong_increment():
    counter += 1   

def correct_increment():
    global counter
    counter += 1
    print("Fixed counter:", counter)

correct_increment()
#Fixed counter: 1
