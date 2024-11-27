# Algorithm:
# 1. Initialize a tuple `num` with numbers.
# 2. Use a loop to check if each number is odd or even.
# 3. Increment counters `odd` and `even` accordingly.
# 4. Print the counts.

num = (1, 2, 3, 4, 5, 6, 7, 8, 9)
odd = even = 0

for x in num:
    if x % 2:  # Odd if remainder is 1
        odd += 1
    else:      # Even if divisible by 2
        even += 1

print(odd)
print(even)
