# Algorithm:
# 1. Define the string `str`.
# 2. Initialize an empty string `r_str` to store the reversed string.
# 3. Use a while loop to iterate through the string from end to start:
#    - Add each character to `r_str`.
# 4. Print the reversed string.

str = 'jagooo'
print(str)
r_str = ""
count = len(str)

while count > 0:
    r_str += str[count - 1]
    count -= 1

print(r_str)