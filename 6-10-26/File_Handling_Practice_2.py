 # APPEND mode 'a'


file = open("student.txt","a")
file.write("i am learning file handing.\n")
file.close()
print("data added successfully...!!!")


# Write multiple lines using writelines()


file = open("college.txt","w")
lines = [
    "my college name.\n",
    "bca course.\n",
    "python programing.\n"
]
file.writelines(lines)
file.close


# r+ mode

file = open("student.txt","r+")
print(file.read())
file.seek(0)
file.tell()
file.write("updated:")
file.close


#w+ mode
file = open("student.txt","w+")
file.write("my name is raj\n")
file.write("i am learning python")

file.seek(1)
file.tell()
print(file.read())
file.close()


#a+ mode

file = open("student.txt","a+")

file.write("\nFile Handling is useful a+ mode")
file.seek(0)
print(file.read())
file.close()

# Binary write - wb

file = open("student.bin","wb")
data = b"hello python"
file.write(data)
file.close()

file = open("student.bin", "rb")

data = file.read()

print(data)
file.close()


# r + b /  w + b


file = open ("student.bin","r+b")
print(file.read())
file.write(b"Python File Handling.")
file.seek(0)
file.close()


 # a+b

file = open("student.bin","a+b")
data = b"new python data"
file.write(data)
file.seek(0)
data = file.read()
print(data)
file.close()


# with.....us

with open("student.txt",  "r") as file:
    print(file.read())


# mode attributes
file = open("student.txt","r")
file.close()

print(file.name)
print(file.mode)
print(file.closed)