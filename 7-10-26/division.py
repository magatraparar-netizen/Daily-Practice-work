try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Division =", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Finally block executed.")