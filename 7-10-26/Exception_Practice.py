# 1. ValueError

try:

    age = int(input("Enter your age: "))

    print("Your age is:", age)

except ValueError:

    print("Error: Please enter a valid number.")


# 2. ZeroDivisionError

try:

    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    result = number1 / number2

    print("Result:", result)

except ZeroDivisionError:

    print("Error: Cannot divide by zero.")


# 3. IndexError

try:

    subjects = ["Python", "Java", "PHP"]

    print(subjects[5])

except IndexError:

    print("Error: Subject index does not exist.")


