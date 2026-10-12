import math

try:
    num = float(input("Enter a number: "))

    if num < 0:
        raise ValueError("Cannot find square root of a negative number")

    result = math.sqrt(num)

    print("Square root =", result)

except ValueError as e:
    print("Error:", e)