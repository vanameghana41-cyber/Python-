numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cubes = list(map(lambda x: x**3, numbers))
print("Cubes:", cubes)
div_by_3 = list(filter(lambda x: x % 3 == 0, numbers))
print("Divisible by 3:", div_by_3)
'''Cubes: [1, 8, 27, 64, 125, 216, 343, 512, 729]
Divisible by 3: [3, 6, 9]'''
