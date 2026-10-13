# Higher Order Functions in Python

# Sorted()
# Map()
# Reduce()
# filter()

# Sorted Integers in Ascending and Descending Order

1.#ascending
numbers = [10,20,30,40,50,60,70,80,90,100]
ascending = sorted(numbers)
print(ascending)

#descending
numbers = [10,20,30,40,50,60,70,80,90,100]
descending = sorted(numbers,reverse=True)
print(descending)

# Sort String by Length

names = ["Raj","Om","Ravi","Prince","darshan"]
sorted_names = sorted(names , key=len)
print(sorted_names)

# Sort Strings by Last Letter using lambda

sorted_by_last_letter = sorted(names,key = lambda names : names[-1])
print(sorted_by_last_letter)

# Sort List of Dictionaries by age

student_data = [
    {"name":"rahul", "age":25},
    {"name":"rohit", "age":25},
    {"name":"virat", "age":25},
    {"name":"anushka", "age":25},
    {"name":"ritika", "age":25},
]
sorted_by_name = sorted(student_data , key = lambda student : student["name"])
print(student_data)
print(sorted_by_name)

#Sort Numbers by Last Digit

numbers = [48, 98, 21, 78, 36, 25]

sorted_numbers = sorted(numbers, key=lambda x: x % 10)

print(sorted_numbers)

2.# map() - Convert String to Uppercase

cars = ["Rolls-Royce","Ferrari","Lamborghini","BMW","jaguar","scorpio"]
uppercase_strings = list(map(str.upper , cars))
print(uppercase_strings)

# map() - Convert String to lowercase

cars = ["Rolls-Royce","Ferrari","Lamborghini","BMW","jaguar","scorpio"]
lowercase_strings = list(map(str.lower , cars))
print(lowercase_strings)

# map() - Square Every number

import math

numbers = [10,20,30,40,50,60]
numbers_square = list(map(lambda  x : int(math.pow(x, 2)), numbers))
number_square = list(map(pow , numbers , [] * len(numbers)))
square_root = [x * x for x in numbers]
print(number_square)
print(square_root)

# map() - Apply 18% Tax to PriceList

prices = [10 , 20  , 30 , 40 , 50]

final_price = list(map(lambda price: price + (price * 18 / 100) , prices))

print(final_price)

#Cube Every Number — map

numbers = [1, 2, 3, 4, 5, 6]

cubes = list(map(lambda x: x ** 3, numbers))

print(cubes)

# Filter() - Even Numbers

numbers = [10 , 15 , 20 , 25 , 30 , 35 , 40 , 45 , 50,55, 60, 65, 70]

even_num = list(filter(lambda x : x <= 30 , numbers))

print(even_num)

3.#Reduce() - Product of All Elements

from functools import reduce

numbers = [1 , 2 , 3 , 4 , 5 , 6, 7 ,8 ,9 , 10]

product = reduce(lambda x , y : x + y , numbers)

print(product)

#Product of All Elements — reduce()

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

product = reduce(lambda x, y: x * y, numbers)

print("Product:", product)

#Find the Largest Number — reduce()

from functools import reduce

numbers = [12, 45, 23, 67, 34, 89]

largest = reduce(lambda x, y: x if x > y else y, numbers)

print("Largest Number:", largest)

#Find the Smallest Number — reduce()

from functools import reduce

numbers = [12, 45, 23, 67, 34, 89]

smallest = reduce(lambda x, y: x if x < y else y, numbers)

print("Smallest Number:", smallest)