# Day 2 - 30 Days of Python programming

# Excersice 1
from itertools import product
from math import remainder


first_name = 'Thanh Liem'
last_nane = 'Nguyen Thuc '
full_name = 'Nguyen Thuc Thanh Liem'
country = 'Viet Name'
city = 'Da Nang'
age = 30
year = 2022
is_married = False
is_true = True
is_light_on = True
multi1, multi2, multi3 = 1 , 'Nguyen', {1,2,3}

# Excersice 2
print(type(first_name))
print(type(last_nane))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(multi1))
print(type(multi2))
print(type(multi3))
print(len(first_name))
print(max(len(first_name), len(last_nane)))
num_one = 5
num_two = 4
total = num_one + num_two
print(total)
diff = num_one - num_two
print(diff)
product_value = num_one * num_two
print(product_value)
division = num_one / num_two
print(division)
remainder = num_one % num_two
print(remainder)
exp = num_one ** num_two
print(exp)
floor_division = int(num_one / num_two)
print(floor_division)
r = 30
area_of_circle = 3.14 * (r ** 2)
print(area_of_circle)
circum_of_circle = 2 * 3.14 * r
print(circum_of_circle)
input_r = int(input('input r --->'))

print(input_r ** 2 * 3.14)
first_name = input('input first_name -->')
last_name = input('input last_name -->')
country = input('input country -->')
age = input('input age -->')
print(first_name, last_name, country, age)