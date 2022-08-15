# Day 5 - 30 days of Python programming

from statistics import median


lst = ['item', 'item2', 'item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']

# First Example
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime', 'apple']
first_fruit, second_fruit, third_fruit, *rest = lst
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']
# Second Example about unpacking list
first, second, third, *rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10
# Third Example about unpacking list
countries = ['Germany', 'France', 'Belgium', 'Sweden',
             'Denmark', 'Finland', 'Norway', 'Iceland', 'Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:]  # it returns all the fruits
# it does not include the last index,['orange', 'mango']
orange_and_mango = fruits[-3:-1]
# this will give starting from -3 to the end,['orange', 'mango', 'lemon']
orange_mango_lemon = fruits[-3:]
# a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']
reverse_fruits = fruits[::-1]


# syntax
lst = ['item1', 'item2']
del lst[1]  # only a single item
del lst        # to delete the list completely

fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
# this deletes items between given indexes, so it does not delete the item with index 3!
del fruits[1:3]
print(fruits)       # ['orange', 'lime']
del fruits
# print(fruits)       # This should give: NameError: name 'fruits' is not defined

# Excersice 1
lst = list()
empty_list = []
num_list = [1, 2, 3, 4, 5]
print('List length: ', len(num_list))
print('First : ', num_list[0])
print('Last: ', num_list[len(num_list) - 1])
middle = (len(num_list) + 1) / 2
middle = int(middle)
print('Middle: ', num_list[middle])
mixed_data_types = ['Thanh Liem', 30, '170cm', False, '331 Nguyen Sinh Cung']
it_companies = ['Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print('Number of companies in list: ', len(it_companies))
print('First company:', it_companies[0])
print('Last company:', it_companies[len(it_companies) - 1])
middle = (len(it_companies) + 1) / 2
middle = int(middle)
print('Middle company:', it_companies[middle])
it_companies[4] = 'FPT'
print(it_companies)
it_companies.append('Yahoo')
it_companies.insert(middle, 'NASH')
it_companies[0] = it_companies[0].upper()
it_companies = it_companies + list('#; ')
does_exist = 'Google' in it_companies
print('Is Google exist: ', does_exist)
it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)
it_companies.reverse()
print(it_companies)
it_companies = it_companies[3:]
print(it_companies)
it_companies = it_companies[:-3]
print(it_companies)
it_companies.pop(3)
print(it_companies)
it_companies.remove('Google')
del it_companies[0:2]
it_companies.clear()
print(it_companies)
del it_companies
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
code = front_end + back_end
print(code)
front_end.extend(back_end)
print(front_end)
full_stack = code.copy()
redux_index = full_stack.index('Redux')
full_stack.insert(redux_index + 1, 'Python')
full_stack.insert(redux_index + 1, 'SQL')
print(full_stack)

# Excersice level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(min(ages))
print(max(ages))
print(ages)
ages.append(min(ages))
ages.append(max(ages))
print(ages)
ages.sort()
print(ages)
length = len(ages)
if length % 2 == 0:
    print('Even list')
    index = int(length / 2)
    print(ages[index])
    print(ages[index + 1])
else:
    print('Odd list')
    middle = (length + 1) / 2
    print(ages[middle])
sum = 0
for ele in ages:
    sum += ele
average = sum / len(ages)
print(average)
range_age = max(ages) - min(ages)
print(range_age)
print ('Min and average compare:', min(ages) < average)
print ('Max and average compare:', max(ages) > average)
print ('Max using abs', ())
countries = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Cape Verde',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombi',
    'Comoros',
    'Congo (Brazzaville)',
    'Congo',
    'Costa Rica',
    "Cote d'Ivoire",
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'East Timor (Timor Timur)',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia, The',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea, North',
    'Korea, South',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Macedonia',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia and Montenegro',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Swaziland',
    'Sweden',
    'Switzerland',
    'Syria',
    'Taiwan',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
    'Yemen',
    'Zambia',
    'Zimbabwe'
]

length = len(countries)
print('Length countries:', length)
if length % 2 == 0:
    index = int(length / 2)
    print('Index :', index)
    first_half = countries[0: index]
    last_half = countries[index: length]
    print(len(first_half))
    print(len(last_half))
else:
    index = int(length / 2)
    first_half = countries[0: index + 1]
    last_half = countries[index + 1: length]
    print(len(first_half))
    print(len(last_half))
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *rest = countries
print(china, russia, usa)
print(rest)
