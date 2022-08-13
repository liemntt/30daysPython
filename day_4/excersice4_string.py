# Day 4 - 30 days of Python programming

from os import stat
from re import S


thirty = 'Thirty'
days = 'days'
of = 'of'
python = 'Python'
space = ' '
print(thirty + space + days + space + of + space + python)
print(' '.join([thirty, days, of, python]))
print('%s %s %s %s' % (thirty, days, of, python))
list_str = [thirty, days, of, python]
print('%s' % (list_str))
print('{} {} {} {}'.format(thirty, days, of, python))
print(f'{thirty} {days} {of} {python}')
print(' '.join(['Coding', 'For', 'All']))
company = 'Coding For All'
print(company)
print('length company: ', len(company))
company = company.upper()
print('Upper company:', company)
company = company.lower()
print('Lower company:', company)
company = company.capitalize()
print('Capitalize company:', company)
company = company.title()
print('Title company:', company)
company = company.swapcase()
print('Swapcase company:', company)
slice_company = company[0:6]
print('Slice first word:', slice_company)
is_contains = company.index(slice_company)
print('Using index result:', is_contains)
is_contains = company.find(slice_company)
print('Using find result:', is_contains)
is_contains = company.rfind(slice_company)
print('Using rfind result:', is_contains)
is_contains = company.rindex(slice_company)
print('Using rindex result:', is_contains)
company = company.replace('cODING', 'python')
print(company)
statement = 'Python for everyone'
print('Statement before replace: ', statement)
statement = statement.replace('everyone', 'all')
print('Statement after replace: ', statement)
print('Coding For All'.split(' '))
statement = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(statement.split(', '))
statement = 'Coding For All'
print('Character at index 0 is:', statement[0])
print('Character at last index is:', statement[len(statement) - 1])
print('Character at last index is:', statement[-1])
print('Character at index 10: ', statement[10])


def acronym(str):
    output = str[0]
    index = 1
    while (index < len(str)):
        if str[index - 1] == ' ':
            output += str[index]
        index += 1
    output = output.upper()
    return output


statement = 'Python for everyone'
print(acronym(statement))
statement = 'Coding For All'
print(acronym(statement))
print('Index of \'C\' in \'Coding for all\' :', statement.index('C'))
print('Index of \'F\' in \'Coding for all\' :', statement.find('F'))
statement = 'Coding For All People'
print('Rfind of \'I\' in \'Coding For All People\'', statement.rfind('I'))
statement = "\'You cannot end a sentence with because because because is a conjunction\'"
print('Using find to \"because\" in statement: ', statement.find('because'))
print('Using rindex to \"because\" in statement: ', statement.rindex('because'))
finding_string = 'because because because'
print(statement.index('because because because'))
print(statement[32: 32 + len(finding_string)])
statement = 'You cannot end a sentence with because because because is a conjunction'
print('First occurrence of \'because\' ', statement.find('because'))
print('Coding For All'.startswith('Coding'))
print('Coding For All'.endswith('Coding'))
statement = '   Coding For All      '
print(statement.strip(' '))
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())
list_str = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' '.join(list_str))
statement = """I am enjoying this challenge.\nI just wonder what is next."""
print(statement)
statement = """Name\tAge\tCountry\tCity
Asabeneh\t250\tFinland\tHelsinki"""
print(statement)
radius = 10
area = 3.14 * radius ** 2
statement = 'The area of a circle with radius {} is {} meters square.'
print(statement.format(radius, area))
a, b = 8, 6
print(f'{a} + {b} = {a+b}')
print(f'{a} + {b} = {a-b}')
print(f'{a} + {b} = {a*b}')
print(f'{a} + {b} = {a/b:.2f}')
print(f'{a} + {b} = {a%b}')
print(f'{a} + {b} = {a//b}')
print(f'{a} + {b} = {a**b}')
