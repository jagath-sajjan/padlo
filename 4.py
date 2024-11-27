# Algorithm:
# 1. Take marks as input from the user.
# 2. Use conditional statements to classify marks into grades:
#    - Distinction: 75–100
#    - First Class: 60–74
#    - Second Class: 50–59
#    - Pass: 35–49
#    - Fail: Below 35
# 3. Print the grade.

marks = int(input("Enter Marks: "))

if 75 <= marks <= 100:
    print("Distinction")
elif 60 <= marks <= 74:
    print("First Class")
elif 50 <= marks <= 59:
    print("Second Class")
elif 35 <= marks <= 49:
    print("Pass")
else:
    print("Fail")