import json
import re
f = open('./files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>

# Excersice 1

def count(file_name):
    with open(file_name) as file:
        data = file.read()
        lines = data.splitlines()
        words = data.split()
        print(f'Number of line {len(lines)} in {file_name}')
        print(f'Number of words: {len(words)} in {file_name}')
count('files/obama_speech.txt')
count('files/michelle_obama_speech.txt')
count('files/donald_speech.txt')
count('files/melina_trump_speech.txt')

def most_spoken_languages(file_name, number_of_languages):
    with open(file_name) as file:
        raw = file.read()
        countries = json.loads(raw)
        languages = {}
        for country in countries:
            for language in country['languages']:
                if language in languages.keys():
                    languages[language] += 1
                else:
                    languages[language] = 1
        result = []
        for _ in range(0, number_of_languages):
            num = 0
            language = ''
            for element in languages.keys():
                if int(languages[element]) > num:
                    num = languages[element]
                    language = element
            result.append((num, language))
            languages.pop(language)
            result = [tuple(x) for x in result]
        print(result)
most_spoken_languages('files/countries_data.json', 2)
most_spoken_languages('files/countries_data.json', 10)

def most_populated_countries(file_name, number_of_countries):
    with open(file_name) as file:
        raw = file.read()
        countries = json.loads(raw)
        result = []
        for _ in range(0, number_of_countries):
            top_country = {'country': '', 'population': 0}
            remove_country = ''
            for country in countries:
                if top_country['country'] == '' or top_country['population'] < country['population']:
                    top_country['country'] = country['name']
                    top_country['population'] = country['population']
                    remove_country = country
            countries.remove(remove_country)
            result.append(top_country)
        print(result)

most_populated_countries('files/countries_data.json', 2)


# Excersice 2

def extract_incoming_emails(file_name):
    with open(file_name) as file:
        lines = file.read().splitlines()
        result = set()
        for line in lines:
            words = line.split()
            for word in words:
                match_result = re.match(r'^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$', word)
                if match_result != None:
                    result.add(word)
        print(result)

extract_incoming_emails('files/email_exchanges_big.txt')

def find_most_common_words(file_name, number_of_words):
    with open(file_name) as file:
        raw = file.read().split()
        result = []
        count_words = {}
        for word in raw:
            if word in count_words.keys():
                count_words[word] += 1
            else:
                count_words[word] = 1
        for _ in range(0, number_of_words):
            common_word = ''
            common_times = 0
            for word in count_words:
                if common_word == '' or count_words[word] > common_times:
                    common_word = word
                    common_times = count_words[word]
            count_words.pop(common_word)
            result.append((common_word, common_times))
        print(result)


find_most_common_words('files/obama_speech.txt', 10)
find_most_common_words('files/michelle_obama_speech.txt', 10)
find_most_common_words('files/donald_speech.txt', 10)
find_most_common_words('files/melina_trump_speech.txt', 10)