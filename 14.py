# Algorithm:
# 1. Create a 2D NumPy array `nums` with specified values.
# 2. Use a condition to print values greater than `n`.
# 3. Use another condition to print values less than `n`.

import numpy as np

nums = np.array([[5, 3, 7], [3, 4, 6], [1, 2, 9]])
print(nums)  # Print the original array

n = 5
print(nums[nums > n])  # Print values greater than 5

n = 6
print(nums[nums < n])  # Print values less than 6