# Math , Random and UUID

import math
import random
import uuid

# What is module ??

# A module is a Python file / library containing pre-writtern  code that we can reuse.

"""
1. Math : Mathemetical Operation
2. Random : Generate random values
3. UUID : Generate unique IDs
"""

# Math Module in Python

# .Square root

number = 144

result = math.sqrt(number)

print("numbers:",number)
print("result:",result)

# power

print("3 power 4:", math.pow(3,5))

# Ceil and floor

number = 8.7

print("Number :" , number)
print("Ceil :" , math.ceil(number))
print("Floor :" , math.floor(number))

#. Negative Number

number = -4.3

print("Number :" , number)
print("Ceil :" , math.ceil(number))
print("Floor :" , math.floor(number))

# Factorial

number = 5

print("Factorial :" , math.factorial(number))

# Constants

print("PI :" , math.pi)
print("E :" , math.e)

# Circle area

radius = 5

area = math.pi * math.pow(radius , 2)

print("Circle Area:" , area)

# Circle Circumference

radius = 5

circumference = 2 * math.pi * radius

print("Radius:", radius)

print("Circle Circumference:", circumference)

# Distance Calculation 

a = 3
b = 4

distance = math.sqrt(math.pow(a, 2) + math.pow(b, 2))

print("Distance:", distance)

# Rounding Up Using math.ceil()

number = float(input("Enter a decimal number: "))

result = math.ceil(number)

print("Ceil:", result)

# Random Module

# random number 

number = random.randint(1 , 1000)

print("Random Number:" , number)

# Random choice

students = [
    "Raj",
    "om",
    "ravi",
    "prince",
    "darshan"
]

selected_name = random.choice(students)

print("Random Name:" , selected_name)

# shuffle

students = [
    "Raj",
    "om",
    "ravi",
    "prince",
    "darshan"
]

print("Old List :" , students)

random.shuffle(students)

print("New List :" , students)

#Dice Simulator

dice = random.randint(1, 6)

print("Dice Number:", dice)

# OTP Generator

otp = random.randint(100000, 999999)

print("OTP:", otp)

# UUID Module

# Universally Unique Identifier

# Generate UUID


user_id = uuid.uuid4()

student_id = uuid.uuid4()

print("user ids:", user_id)

print("student_id:", student_id)

# UUID Type
dns_namespace = uuid.NAMESPACE_DNS
name = "instagram.com"

my_id = uuid.uuid5(dns_namespace , name)

print("UUID:" , my_id)
print("Type:" , type(my_id)) 

# Generate UUID5

dns_namespace = uuid.NAMESPACE_DNS
name = "python.org"

my_id = uuid.uuid5(dns_namespace, name)

print("UUID:", my_id)
print("Type:", type(my_id))

