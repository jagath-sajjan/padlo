# Algorithm:
# 1. Create a 2D NumPy array `nums` with specified values.
# 2. Use `np.sort()` to sort the entire array (flattened).
# 3. Use `np.sort(nums, axis=0)` to sort the array column-wise (along rows).
# 4. Print the sorted arrays.

import numpy as np

nums = np.array([[5, 3, 7], [6, 9, 8], [9, 1, 2]])
print(nums)  # Print the original array

print(np.sort(nums))  # Sort the entire array (flattened by default)

print(np.sort(nums, axis=0))  # Sort the array column-wise (by rows)