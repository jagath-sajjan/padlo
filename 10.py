# Algorithm:
# 1. Define the function `upper` that takes a string `str` as input.
# 2. Initialize a counter `num_upper` to 0.
# 3. Loop through the first 4 characters of the string:
#    - Check if each character is uppercase.
#    - Increment `num_upper` for each uppercase letter.
# 4. If `num_upper` is 2 or more, return the entire string in uppercase.
# 5. Otherwise, return the original string.

def upper(s):
    num_upper = sum(1 for letter in s[:4] if letter.isupper())  # Count uppercase letters in the first 4 characters
    return s.upper() if num_upper >= 2 else s

print(upper('Nigma'))
print(upper('NiGma'))