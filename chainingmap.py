from functools import reduce

nums = [1,2,3,4,5,6,7,8,9,10]
evens = filter(lambda x: x % 2 == 0, nums)
squares = map(lambda x: x**2, evens)
total = reduce(lambda a, b: a + b, squares)
print("Pipeline total:", total)
total_comp = sum([x**2 for x in nums if x % 2 == 0])
print("List comprehension total:", total_comp)
'''Pipeline total: 220
List comprehension total: 220'''
