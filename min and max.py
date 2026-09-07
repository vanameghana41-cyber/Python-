nums = [1, 2, 3, 5, 6]
min_val = nums[0]
max_val = nums[0]
sum_val = 0

# Find minimum
for i in nums:
    if i < min_val:
        min_val = i

# Find maximum
for i in nums:
    if i > max_val:
        max_val = i

# Find sum
for i in nums:
    sum_val += i

print("minimum element:", min_val)
print("maximum element:", max_val)
print("Sum of elements:", sum_val)
'''minimum element: 1
maximum element: 6
Sum of elements: 17'''
