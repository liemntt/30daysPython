import random
from string import ascii_letters


# Excersice 1

def user_id_gen_by_user():
    result = ""
    number_digits, number_characters = input('Input number of digits, characters: ').split()
    number_digits = int(number_digits)
    number_characters = int(number_characters)
    count_digits = 0
    count_characters = 0
    while len(result) < number_characters + number_digits:
        random_value = random.random()
        if random_value > 0.5 and count_digits < number_digits:
            count_digits += 1
            result += str(random.randint(0, 10))
        elif count_characters < number_characters:
            count_characters += 1
            result += random.choice(ascii_letters)
    return result
def rgp_color_gen():
    rgb = []
    for iterator in range(0,3):
        rgb.append(random.randint(0, 255))
    result = f'rgb({rgb[0]},{rgb[1]},{rgb[2]})'
    print(result)
    return result

# Excersice 2
def list_of_hexa_colors(number):
    hexa_colors = []
    for _ in range(0, number):
        result = '#'
        while len(result) < 7:
            random_value = random.random()
            if random_value > 0.5:
                result += str(random.randint(0, 9))
            else:
                result += random.choice('abcdef')
        hexa_colors.append(result)
    print(hexa_colors)
def list_of_rgb_colors(number):
    rgb_colors = []
    for _ in range(0, number):
        rgb_colors.append(rgp_color_gen())
    print(rgb_colors)
def generate_colors(color_type, number_color):
    if color_type == 'hexa':
        list_of_hexa_colors(number_color)
    elif color_type == 'rgb':
        list_of_rgb_colors(number_color)


# Excersice 3
def shuffle_list(input_list):
    shuffled_list = []
    for _ in range(0, len(input_list)):
        value = random.choice(input_list)
        shuffled_list.append(value)
        input_list.remove(value)
    return shuffled_list
input_list = [1,2,3,4,5,6,7,8,9,10]
print(shuffle_list(input_list))
def random_set_number():
    result = set()
    while len(result) < 7:
        value = random.randint(0,9)
        result.add(value)
    return result
print(random_set_number())