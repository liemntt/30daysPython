# Day 9 - 30 Days of Python Programming

# Excersice 1
age = input('Enter your age: ')
age = int(age)
if age >= 18:
    print('You are old enough to learn to drive.')
else:
    year = 18 - age
    print('You need ', year, ' more years to learn to drive')
my_age = int(input('Enter my_age: '))
your_age = int(input('Enter your_age: '))
if my_age == your_age:
    print('You and I have the same age.')
elif abs(my_age - your_age) == 1:
    if my_age > your_age:
        print('I am a year older than you.')
    else:
        print('You are a year older than me.')
else:
    if my_age > your_age:
        print('I am', my_age - your_age, 'years older than you.')
    else:
        print('You are', your_age - my_age, 'years older than me.')
number_one = int(input('Enter number one:'))
number_two = int(input('Enter number two:'))
if number_one > number_two:
    print('number_one greater than number_two')
elif number_two == number_one:
    print('number_one equals number_two')
elif number_two > number_one:
    print('number_one smaller than number_two')

# Excersice 2
student_scores = int(input('Input student score:'))
if student_scores >= 90:
    print('Grade A:', student_scores, 'scores.')
elif 90 > student_scores >= 70:
    print('Grade B', student_scores, 'scores.')
elif 70 > student_scores >= 60:
    print('Grade C', student_scores, 'scores.')
elif 60 > student_scores >= 50:
    print('Grade D', student_scores, 'scores.')
else:
    print('Grade F', student_scores, 'scores.')
month = input('Input month:')
if month == 'September' or month == 'October' or month == 'November':
    print('The season is Autumn')
elif month == 'December' or month == 'January' or month == 'February':
    print('The season is Winter')
elif month == 'March' or month == 'April' or month == 'May':
    print('The season is Spring')
elif month == 'June' or month == 'July' or month == 'August':
    print('The season is Summer')
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input('Enter new fruit: ')
if new_fruit in fruits:
    print('That fruit already exist in the list.')
else:
    fruits.append(new_fruit)
    print('New fruits', fruits)
    
# Excersice 3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python', 'Java'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person.keys():
    length = len(person.get('skills'))
    middle = int(length / 2)
    if length % 2 == 0:
        print(middle)
        print('Middle skills:', person.get('skills')[middle])
        print('Middle skills:', person.get('skills')[middle - 1])
    else:
        print(middle)
        print('Middle skills:', person.get('skills')[middle])
    if 'Python' in person.get('skills'):
        print('User has Python skill.')
    else:
        print('User don\'t have Python skill.')
    skills = person.get('skills')
    if len(skills) == 2 and 'JavaScript' in skills and 'React' in skills:
        print('He is a front-end developer.')
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print('He is a back-end developer.')
    elif 'Node' in skills and 'React' in skills and 'MonghDB' in skills:
        print('He is a fullstack developer.')
    else:
        print('Unknown title.')
if 'is_marred' in person.keys() and 'country' in person.keys():
    if person.get('is_marred') and person.get('country') == 'Finland':
        print(person.get('first_name'), person.get('last_name'), 'lives in', person.get('country'), '.He is married.')

