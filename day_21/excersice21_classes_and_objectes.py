import statistics
from functools import reduce
import math

class Statistics:

    def __init__(self, input) -> None:
        self.input = input

    def count(self) -> int:
        return len(self.input)
    
    def sum(self) -> int:
        return reduce(lambda x,y: x+y , self.input)

    def min(self) -> int:
        min = -1
        for i in self.input:
            if min == -1 or min > i:
                min = i
        return min

    def max(self):
        max = 0
        for i in self.input:
            if i > max:
                max = i
        return max
    def range(self) -> int:
        return self.max() - self.min()

    def mean(self) -> int:
        return math.ceil(statistics.mean(self.input))

    def median(self) -> int:
        return statistics.median(self.input)

    def std(self) -> float:
        return statistics.stdev(self.input)

    def mode(self) -> dict:
        count_dict = {}
        for i in self.input:
            if i not in count_dict.keys():
                count_dict[i] = 1
            else:
                count_dict[i] += 1
        count_max = 0
        count_value = ''
        for i in count_dict.keys():
            if count_max == 0 or count_max < count_dict[i]:
                count_max = count_dict[i]
                count_value = i
        return { 'mode': count_value, 'count': count_max}

    def var(self) -> float:
        return statistics.variance(self.input)

    def freq_dist(self) -> list:
        percent = float(100 / len(self.input))
        freq = {}
        for i in self.input:
            if i not in freq.keys():
                freq[i] = percent
            else:
                freq[i] += percent
        result = []
        for i in freq.keys():
            result.append((freq[i], i))
        return result

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)
print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]

class PersonAccount:

    def __init__(self, firstname, lastname, incomes, expenses) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses
    
    def total_income(self):
        pass
    
    def total_expense(self):
        pass

    def account_info(self):
        pass

    def add_income(self):
        pass

    def add_expense(self):
        pass

    def account_balance(self):
        pass