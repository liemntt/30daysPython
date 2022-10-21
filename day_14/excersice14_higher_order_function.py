from countries import countries_data
from string import ascii_lowercase
from day_11.countries_data import data
# Day 14 


# Excersice level 1

# 1.
# map: loop over the iterator and return new iterator
# filter: loop over the iterator and return new iterator that contain specific items
# reduce: loop over the iterator and return a single value

# 2.
# higher order functions: take a function and an iterator as parameters
# Closure: closure created by a function inside another function and it will be return
# Decorator: Add new functionality to an existing object without modify it's structure

# 3.
from functools import reduce


example_list = ['Python', 'Decorator pattern', 'Closure', 'Higher order functions']
map_result = map(lambda test: test.upper(), example_list)
print(list(map_result))
filter_result = filter(lambda test: len(test)> 10, example_list)
print(list(filter_result))
reduce_result = reduce(lambda x, y: x + y, example_list)
print(list(example_list))

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Excersice level 2
countries = list(map(lambda country: country.upper(), countries))
print(countries)
square_numbers = list(map(lambda x: x*x, numbers))
print(square_numbers)
names = list(map(lambda name: name.upper(), names))
print(names)
land_countries = list(filter(lambda country: 'LAND' in country, countries))
print(land_countries)
six_characters_countries = list(filter(lambda  country: len(country) == 6, countries))
print(six_characters_countries)

more_six_characters_countries = list(filter(lambda  country: len(country) >= 6, countries))
print(more_six_characters_countries)
start_with_e_countries = list(filter(lambda country: country.startswith('E'), countries))
print(start_with_e_countries)

lower_countries = filter(lambda country: country.startswith('e'), map(lambda country: country.lower(), countries))
print(list(lower_countries))

def get_string_lists(input_list):
    return list(filter(lambda element: type(element) == str, input_list))
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 1,2,3,4,5]
print(get_string_lists(countries))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = reduce(lambda x,y: x+y, numbers)
print(sum)
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def make_sentence(x, y):
    if y != 'Iceland':
        return ', '.join([x,y])
    return f'{x} and {y} are north European countries'

sentence = reduce(make_sentence, countries)
print(sentence)
# sample
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')

def categorize_countries(country, pattern):
    return pattern in country
result_list = filter(lambda country: categorize_countries(country, 'land'), countries_data)    
print(list(result_list))
def create_dict():
    result = {}
    for alphabet in ascii_lowercase:
        for country in countries_data:
            if country.startswith(alphabet.upper()):
                if alphabet in result.keys():
                    result[alphabet] += 1
                else:
                    result[alphabet] = 1
    return result
print(create_dict())
def get_first_ten_countries():
    result = []
    x = 0
    while(x < 10):
        result.append(countries_data[x])
        x += 1
    return result
print(get_first_ten_countries())
def get_last_ten_countries():
    result = []
    for x in range(1, 11):
        result.append(countries_data[len(countries_data) - x])
    return result
print(get_last_ten_countries())

# Excersice level 3: