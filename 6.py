# Algorithm:
# 1. Initialize `cnt` (count), `sum` (total), and `number` (user input) variables.
# 2. Use a while loop to repeatedly take user input until 0 is entered:
#    - Add the number to `sum`.
#    - Increment the counter `cnt`.
# 3. After exiting the loop, check if any numbers were entered (excluding 0):
#    - If none, prompt the user to enter numbers.
#    - Otherwise, print the average (excluding the terminating 0) and the sum.

cnt = 0
total = 0.0
number = 1

while number != 0:
    number = int(input(""))
    total += number
    cnt += 1

if cnt == 1:  # Only 0 was entered
    print("Enter Numbers....")
else:
    print(total / (cnt - 1), total)  # Exclude terminating 0 from average calculation
