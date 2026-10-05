# 1. Create file with mode 'w'

file = open("student.txt", "w")

file.write("My name is Raj.\n")
file.write("I am studying BCA.\n")
file.write("I am learning Python.\n")

file.close()

print("student.txt created successfully....!!!!")


# 2. Read mode 'r'

file = open("student.txt", "r")

content = file.read()

print(content)

file.close()


# 3. Create another file with mode 'w'

file = open("college.txt", "w")

file.write("My College Name.\n")
file.write("BCA Course.\n")
file.write("Python Programming.\n")

file.close()

print("college.txt created successfully....!!!!")


# 4. Read another file

file = open("college.txt", "r")

content = file.read()

print(content)

file.close()

