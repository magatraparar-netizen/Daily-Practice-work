import math_utils as a
import math as m
import string_utils
from utilities.file_utils import write_file , read_file
from utilities.date_utils import days_between
from datetime import date
import helper
from shapes import circle
from shapes import rectangle

#Q.1 - Custom Module (math_utils)
print("Addition:" , a.add(20 , 30))
print("Subtraction:" , a.subtract(20 , 30))
print("Multiplication:" , a.multiply(20 , 30))
print("Division:" , a.divide(20 , 30))

# Q.2 - Math Module
print('square root 49:' , m.sqrt(49))
print("90 value in sin:" , m.sin(m.radians(90)))

# Q.3 - String Utilities Module
print("Vowel in String :" , string_utils.count_vowel("This is Python Language."))


# Q.4 - __name__ and __main__
import greet
greet.greet("star")

# Q.5 - Importing Helper Module
print("This script is imported as a module.")
helper.greet("Raj")

# Q.6 - Shapes Package
radius = 5

print("Area of Circle:", round(circle.area(radius), 2))
print("Circumference of Circle:", round(circle.circumference(radius), 2))

length = 10
width = 5

print("Area of Rectangle:", rectangle.area(length, width))
print("Perimeter of Rectangle:", rectangle.perimeter(length, width))

# Q.7 - Utilities Package (File Operations)
write_file("data.txt" , "Hello raj")

content = read_file("data.txt")

print("File Content:" , content)

# Q.7 - Utilities Package (File Operations)
# Date 
date1 = date(2005 , 9 , 9)
date2 = date(2026 , 9 , 9)

print("Number of days:" , days_between(date1 , date2))


# Q.8 - Explore Module Attributes using dir()
# Display attributes of math module
import math

print("Attributes of math module:")
print(dir(math))

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


s1 = Student("Raj", 21)

print("\nAttributes of Student object:")
print(dir(s1))