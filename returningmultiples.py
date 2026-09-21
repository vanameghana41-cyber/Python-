def stats(numbers):
    """
    Returns the minimum, maximum, and average of a list of numbers.
    """
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return (minimum, maximum, average)
nums = [10, 20, 30, 40, 50]
min_val, max_val, avg_val = stats(nums)
print("Minimum:", min_val)
print("Maximum:", max_val)
print("Average:", avg_val)
#Minimum: 10
#Maximum: 50
#Average: 30.0
