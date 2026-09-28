def c_to_f(c):
    return (c * 9/5) + 32

temps_c = [0, 20, 37, 100]
temps_f = list(map(c_to_f, temps_c))
print("Fahrenheit:", temps_f)
words = ["apple", "banana", "cherry"]
upper_words = list(map(str.upper, words))
print("Uppercase:", upper_words)
'''Fahrenheit: [32.0, 68.0, 98.6, 212.0]
Uppercase: ['APPLE', 'BANANA', 'CHERRY']'''
