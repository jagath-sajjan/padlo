# Algorithm:
# 1. Take two integer inputs, `a` and `b`.
# 2. Check if `b` is zero; if so, raise an `ArithmeticError`.
# 3. If no error occurs, print the result of `a / b`.
# 4. If an error occurs (specifically division by zero), print an error message.

try:
    a = int(input("Value Of A: "))
    b = int(input("Value Of B: "))
    if b == 0:
        raise ArithmeticError  # Explicitly raise an ArithmeticError
    else:
        print("a/b = ", a / b)
except ArithmeticError:  # Catch only ArithmeticError
    print("The Value Of b Can't Be Zero")  # Handle the division by zero error
