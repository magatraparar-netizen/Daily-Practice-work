# flush()

file = open("student_flush.txt","w")
file.write("My name is Raj.")
file.flush()
print("Student data flushed successfully")
file.close()

# truncate

file = open("student_truncate.txt", "w", encoding="utf-8")
file.write("હેલો રાજ")
file.close()
file = open("student_truncate.txt","r+")

# file.truncate()

file.seek(0)
print(file.read())
file.close()
