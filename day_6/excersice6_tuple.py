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
print(siblings)
print(new_tuple)
fruits = ('banana', 'cherry', 'apple', 'lemon')
vegatables = ('a', 'b', 'c', 'd')