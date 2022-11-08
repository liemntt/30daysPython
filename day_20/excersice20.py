import requests
import json
import math
import pandas
from functools import reduce
from bs4 import BeautifulSoup



url = 'http://www.gutenberg.org/files/1112/1112.txt'

def most_frequent_words(url):
    response = requests.get(url)
    if response.status_code == 200:
        text = response.text
        words = text.split()
        words_count = {}
        for word in words:
            if word in words_count.keys():
                words_count[word] += 1
            else:
                words_count[word] = 1
        result = []
        for _ in range(0, 10):
            max = 0
            word = ''
            for count in words_count.keys():
                if max < words_count[count] and not is_contain(result, count):
                    max = words_count[count]
                    word = count
            result.append((word, max))
        print(result)
    else:
        print('Error happen.')

def is_contain(result, element):
    for value in result:
        if value[0] == element:
            return True
    return False
most_frequent_words(url)
cats_api = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(cats_api)
cats_list = response.json()
# print(cats_list)
def get_min_cats_weight(cats):
    min_last = -1
    max_last = -1
    for cat in cats:
        min, max = map(lambda x: int(x) ,cat['weight']['metric'].split('-'))
        if min < min_last or min_last == -1:
            min_last = min
        if max < max_last or max_last == -1:
            max_last = max
    print(f'Min weight metrics: {min_last} - {max_last}')
def get_max_cats_weight(cats):
    min_last = -1
    max_last = -1
    for cat in cats:
        min, max = map(lambda x: int(x) ,cat['weight']['metric'].split('-'))
        if min > min_last or min_last == -1:
            min_last = min
        if max > max_last or max_last == -1:
            max_last = max
    print(f'Max weight metrics: {min_last} - {max_last}')
get_min_cats_weight(cats_list)
get_max_cats_weight(cats_list)

def calculate_mean_weight(cats):
    mins = []
    maxs = []
    for cat in cats:
        min, max = map(lambda x: int(x) ,cat['weight']['metric'].split('-'))
        mins.append(min)
        maxs.append(max)
    mean_mins = int(reduce(lambda x,y: x+y, mins) / len(mins))
    mean_maxs = int(reduce(lambda x,y: x+y, maxs) / len(maxs))
    print(f'Mean weight metrics: {mean_mins} - {mean_maxs}')
calculate_mean_weight(cats_list)
def calculate_median_weith(cats):
    mins = []
    maxs = []
    for cat in cats:
        min, max = map(lambda x: int(x) ,cat['weight']['metric'].split('-'))
        mins.append(min)
        maxs.append(max)
    median_min_index = int(len(mins) / 2)
    median_mins = mins[median_min_index]
    median_max_index = int(len(maxs) / 2)
    median_maxs = maxs[median_max_index]
    print(f'Median weight metrics: {median_mins} - {median_maxs}')
calculate_median_weith(cats_list)

def calculate_standard_deviation_weight(cats):
    mins = []
    maxs = []
    for cat in cats:
        min, max = map(lambda x: int(x) ,cat['weight']['metric'].split('-'))
        mins.append(min)
        maxs.append(max)
    mean_mins = int(reduce(lambda x,y: x+y, mins) / len(mins))
    mean_maxs = int(reduce(lambda x,y: x+y, maxs) / len(maxs))
    sqrt_variance_mins = map(lambda x: (x - mean_mins)**2, mins)
    sqrt_variance_maxs = map(lambda x: (x - mean_maxs)**2, maxs)
    standard_deviation_min = math.sqrt(reduce(lambda x,y: x+y, sqrt_variance_mins) / len(mins))
    standard_deviation_max = math.sqrt(reduce(lambda x,y: x+y, sqrt_variance_maxs) / len(maxs))
    print(f'Standard deviation weight metrics: {standard_deviation_min} - {standard_deviation_max}')
calculate_standard_deviation_weight(cats_list)
def get_min_cats_life_span(cats):
    min_last = -1
    max_last = -1
    for cat in cats:
        min, max = map(lambda x: int(x) ,cat['life_span'].split('-'))
        if min < min_last or min_last == -1:
            min_last = min
        if max < max_last or max_last == -1:
            max_last = max
    print(f'Min life span: {min_last} - {max_last}')
def get_max_cats_life_span(cats):
    min_last = -1
    max_last = -1
    for cat in cats:
        min, max = map(lambda x: int(x) ,cat['life_span'].split('-'))
        if min > min_last or min_last == -1:
            min_last = min
        if max > max_last or max_last == -1:
            max_last = max
    print(f'Max life span: {min_last} - {max_last}')
def calculate_mean_life_span(cats):
    mins = []
    maxs = []
    for cat in cats:
        min, max = map(lambda x: int(x) ,cat['life_span'].split('-'))
        mins.append(min)
        maxs.append(max)
    mean_mins = int(reduce(lambda x,y: x+y, mins) / len(mins))
    mean_maxs = int(reduce(lambda x,y: x+y, maxs) / len(maxs))
    print(f'Mean life span: {mean_mins} - {mean_maxs}')
def calculate_median_life_span(cats):
    mins = []
    maxs = []
    for cat in cats:
        min, max = map(lambda x: int(x) ,cat['life_span'].split('-'))
        mins.append(min)
        maxs.append(max)
    median_min_index = int(len(mins) / 2)
    median_mins = mins[median_min_index]
    median_max_index = int(len(maxs) / 2)
    median_maxs = maxs[median_max_index]
    print(f'Median life span: {median_mins} - {median_maxs}')
def calculate_standard_deviation_life_span(cats):
    mins = []
    maxs = []
    for cat in cats:
        min, max = map(lambda x: int(x) ,cat['life_span'].split('-'))
        mins.append(min)
        maxs.append(max)
    mean_mins = int(reduce(lambda x,y: x+y, mins) / len(mins))
    mean_maxs = int(reduce(lambda x,y: x+y, maxs) / len(maxs))
    sqrt_variance_mins = map(lambda x: (x - mean_mins)**2, mins)
    sqrt_variance_maxs = map(lambda x: (x - mean_maxs)**2, maxs)
    standard_deviation_min = math.sqrt(reduce(lambda x,y: x+y, sqrt_variance_mins) / len(mins))
    standard_deviation_max = math.sqrt(reduce(lambda x,y: x+y, sqrt_variance_maxs) / len(maxs))
    print(f'Standard deviation life span: {standard_deviation_min} - {standard_deviation_max}')
get_min_cats_life_span(cats_list)
get_max_cats_life_span(cats_list)
calculate_median_life_span(cats_list)
calculate_mean_life_span(cats_list)
calculate_standard_deviation_life_span(cats_list)

def create_frequence_country_table(cats):
    result = {}
    for cat in cats:
        if cat['country_code'] not in result.keys():
            result[cat['country_code']] = 1
        else:
            result[cat['country_code']] += 1
    data = {
        'country': result.keys(),
        'frequence': result.values()
    }
    table = pandas.DataFrame(data)
    print(table)
def create_frequence_breed_table(cats):
    result = {}
    for cat in cats:
        if cat['name'] not in result.keys():
            result[cat['name']] = 1
        else:
            result[cat['name']] += 1
    data = {
        'breed': result.keys(),
        'frequence': result.values()
    }
    table = pandas.DataFrame(data)
    print(table)
create_frequence_country_table(cats_list)
create_frequence_breed_table(cats_list)

def read_uci():
    response = requests.get('https://archive.ics.uci.edu/ml/datasets.php')
    text = response.text
    # with open('files/raw.html', 'w') as file:
    #     file.write(text)
    soup = BeautifulSoup(text, 'html.parser')
    print(soup.title)
read_uci()