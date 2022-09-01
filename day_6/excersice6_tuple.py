# Day 6 - 30 days of Python programming

from hashlib import new


empty_tuple = ()
empty_tuple = tuple()
random_1 = ('Harry Potter', 'Luffy', 'Kunka')
random_2 = ('Puck', 'Phantom Assassin', 'Maiden')
join_tuple = random_1 + random_2
print(len(join_tuple))
new_tuple = ('father', 'mother')
join_tuple = join_tuple + new_tuple
print(join_tuple)
siblings = join_tuple[0:6]
new_tuple = join_tuple[6:]
first, second, *rest = join_tuple
print(siblings)
print(new_tuple)
print(rest)
fruits = ('banana', 'cherry', 'apple', 'lemon')
vegatables = ('a', 'b', 'c', 'd')
animal = ('monkey','chicken', 'lion', 'dog')
food_stuff_tp = fruits + vegatables + animal
food_stuff_lt = list(food_stuff_tp)
length = len(food_stuff_lt)

if length % 2 == 0:
    index = int(length / 2)
    food_stuff_lt.pop(index - 1)
    food_stuff_lt.pop(index - 1)
else:
    index = int(length / 2)
    food_stuff_lt.pop(index)
print(food_stuff_lt)
food_stuff_tp = food_stuff_tp[3:]
print(food_stuff_tp)
food_stuff_tp = food_stuff_tp[:-3]
print(food_stuff_tp)
del food_stuff_tp
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
if 'Estonia' in nordic_countries:
    print('Estonia in nordic_country')
else:
    print('Estonia not in nordic_coutries')
if 'Iceland' in nordic_countries:
    print('Iceland in nordic_country')
else:
    print('Iceland not in nordic_coutries')