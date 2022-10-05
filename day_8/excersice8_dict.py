# Day 8 - 30 days of Python Programming

dog = {}
dog['name'] = 'Milu'
dog['color'] = 'Red'
dog['breed'] = 'Chihuahua'
dog['age'] = 4
dog['legs'] = 4
print(dog)
student_dict = {
    'first_name' : 'Liem',
    'last_name' : 'Nguyen',
    'gender' : 'Male',
    'age' : 30,
    'marital_status' : False,
    'skills': ['HTML', 'CSS', 'Java'],
    'country' : 'Vietnam',
    'city' : 'HCM',
    'address' : '30/2 CMTT'
}
print('Student dict length: ', len(student_dict))
print('Data type of skills ', type(student_dict.get('skills')))
print('Skills ', student_dict.get('skills'))
student_dict.get('skills').append('C++')
student_dict['skills'].append('Python')
keys = student_dict.keys()
values = student_dict.values()
student_tuple = student_dict.items()
print(student_tuple)
student_dict.popitem()
student_dict.pop('age')
del student_dict['city']
print(student_dict)
del dog