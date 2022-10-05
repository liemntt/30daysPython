# Day 7 - 30 days of Python programming

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Excersice 1
length_it_companies = len(it_companies)
print(length_it_companies)
it_companies.add('Twitter')
it_companies.update(('FPT', 'Meta'))
remove_company = it_companies.pop()
it_companies.discard('FPT') # won't raise errors
it_companies.remove('Meta') # can raise errors
print(remove_company)
print(it_companies)

# Excersice 2
C = A.union(B)
print(C)
intersaction_set = A.intersection(B)
print(intersaction_set)
print('Is A subset B?', A.issubset(B))
print('Is A and B are disjoin sets?', A.isdisjoint(B))
print(A.symmetric_difference(B))
print(B.symmetric_difference(A))
del A, B, it_companies

# Excersice 3
age_set = set(age)
print('Age list length', len(age), ' .')
print('Age set length', len(age_set), ' .')
str = 'I am a teacher and I love to inspire and teach people'
words = str.split( )
words_set = set(words)
print(words_set)
