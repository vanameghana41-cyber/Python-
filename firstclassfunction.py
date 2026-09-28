def greet(name):
    return f"Hello, {name}!"

say_hello = greet   
print(say_hello("Saimeghana"))

def call_twice(func, value):
    return func(value), func(value)

print(call_twice(greet, "World"))

def make_multiplier(n):
    def multiplier(x):
        return n * x
    return multiplier

times3 = make_multiplier(3)
print(times3(10))   
'''Hello, Saimeghana!
('Hello, World!', 'Hello, World!')'''
30
