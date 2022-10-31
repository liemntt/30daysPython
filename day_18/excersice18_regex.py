import re

# Excersice 1
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
words = set(re.split(r'[\s]', re.sub('[.]', '', paragraph)))
print(words)
result = []
for word in words:
    count = len(re.findall(word, paragraph, re.I))
    result.append((word, count))

print(result)

points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-4) # 12
text = '''
The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 
0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance 
between the two furthest particles.
'''
matches = re.findall('-?\d+', text, re.I)
convert_to_int = list(map(lambda match : int(match), matches))
print(convert_to_int)
convert_to_int.sort()
print(convert_to_int)
distance = convert_to_int[len(convert_to_int) - 1] - convert_to_int[0]
print(distance)

# Excersice 2
def is_valid_variable(text):
    return re.fullmatch('[^\d][^-]*', text, re.I|re.M) != None
print(is_valid_variable('first_n ame')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname'))# True

# Excersice 3

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
def clean_text(text):
    return re.sub('[^\d\w\s]', '', sentence)
cleaned_text = clean_text(sentence)
print(cleaned_text)
def most_frequent_words(text):
    words = set(re.split(' ', text))
    result = []
    for word in words:
        count = len(re.findall(word + '\\b', text, re.I))
        result.append((count, word))
        result.sort()
        result.reverse()
    return result[0:3]


print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]