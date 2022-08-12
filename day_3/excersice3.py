# Day 3 - 30 Days of Python programming

from curses.textpad import rectangle
from re import A
import re


age = 30
height = 1.7
complex_num = 3 + 2j

triangle_base = input('Enter base: ')
triangle_height = input('Enter height: ')
area_of_triangle = 0.5 * float(triangle_base) * float(triangle_height)
print('The area of the triangle: ', area_of_triangle)
side_a = input('Enter side a: ')
side_b = input('Enter side b: ')
side_c = input('Enter side c: ')
perimeter_of_triangle = int(side_a) + int(side_b) + int(side_c)
print('The perimeter of the triangle: ', perimeter_of_triangle)
rectangle_lenght = input('Enter lengh: ')
rectangle_width = input('Enter width: ')
area_of_rectangle = float(rectangle_lenght) * float(rectangle_width)
print('Area of the rectangle is ', area_of_rectangle)
perimeter_of_rectangle = 2 * (int(rectangle_lenght) + int(rectangle_width))
print('Perimeter of the rectangle is ', perimeter_of_rectangle)
pi = 3.14
radius = input('Enter circle radius:')
radius = float(radius)
area_of_circle = pi * radius ** 2
circumference = 2 * pi * radius
print('Area of the circle is ', area_of_circle)
print('Circumferencer of the circle is ', circumference)
print('y = 2x - 2')
x_intercept = (0 + 2) / 2
y_intercept = 0 * 2 - 2
print('x-intercept is', x_intercept)
print('y-intercept is', y_intercept)
first_slope = (y_intercept) / (x_intercept)
first_point = [2, 2]
second_point = [6, 10]
slope = (second_point[1] - first_point[1]) / (second_point[0] - first_point[0])
print('Compare 2 slope:', first_slope == slope)
x = input('Insert x --->')
while ('q' not in x):
    x = int(x)
    y = x**2 + 6 * x + 9
    print(y)
    if (y == 0):
        print('X = ', x, ' ---> y = 0')
    x = input('Inser x --->. Press \'q\' to quit:')
python_length = input('Input python length:')
dragon_length = input('Input dragon length:')
if (python_length == dragon_length):
    print('Python and Dragon is equals')
elif (python_length > dragon_length):
    print('Python is longer than Dragon')
else:
    print('Dragon is lobger than Pytho')
if 'on' in 'Python' and 'on' in 'Dragon':
    print('Found')
statement = 'I hope this course is not full of jargon.'
if ('jargon ' in statement):
    print('Found')
else:
    print('Not found')
statement = 'Python'
length = len(statement)
print(type(length))
print(type(float(length)))
print(type(length))
print(type(str(length)))
x = input('Inser a number --->')
while ('q' not in x):
    x = int(x)
    if (x % 2 == 0):
        print('X is even')
    else:
        print('X is odd')
    x = input('Inser new number. Press q to quit:')
floor_division = 7 / 3
print(floor_division)
converted = 2.7
if (floor_division == int(converted)):
    print('floor_division == int(converted)')
print(type('10'))
print(type(10))
if type('10') == type(10):
    print('type(\'10\') is equals type(10)')
if int(9.8) == 10:
    print('int(9.8) is equals 10')
hours = int(input('Enter hours:'))
rate_per_hours = int(input('Enter rate per hours:'))
print('Your weekly earning is ', hours * rate_per_hours)
years = int(input('Enter number of year: '))
print('You have lived for ', years * 365 * 24 * 60 * 60, ' seconds')
x = 1
while x < 6:
    print(x, 1, x**1, x**2, x**3)
    x += 1
