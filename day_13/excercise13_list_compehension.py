numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
positive_numbers = [number for number in numbers if number >= 0]


list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
#output
#[1, 2, 3, 4, 5, 6, 7, 8, 9]
flat_list = [number for subList in list_of_lists for numbers in subList for number in numbers]
print(flat_list)
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]

result_list = [(i, 1, i, i*i, i*i*i, i*i*i*i, i*i*i*i*i) for i in range(11)]
print(result_list)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

result_list = [[country[0].upper(), country[0].upper()[0:3], country[1].upper()] for subList in countries for country in subList]
print(result_list)

result_list = [{'country': country[0].upper(), 'city': country[1].upper()} for subList in countries for country in subList]
print(result_list)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
result_list = [' '.join(name) for subList in names for name in subList]
print(result_list)

slope = lambda a, b: -b/a
print(slope(3,2))