try:
    file = open("data.txt", "r")

    print(file.read())

except FileNotFoundError:
    print("File not found.")

finally:
    print("Finally block executed.")