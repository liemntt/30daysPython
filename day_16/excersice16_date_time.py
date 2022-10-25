from datetime import datetime, date, time
# 1
current_date = datetime.now()
day = current_date.day
month = current_date.month
year = current_date.year
hour = current_date.hour
minutes = current_date.minute
print(f'{day}-{month}-{year} - {hour}:{minutes}')
timestamp = current_date.timestamp()
print(timestamp)
t = current_date.strftime("%m/%d/%Y, %H:%M:%S")
print(t)
sample_str = 'Today is 5 December, 2019.'
t = datetime.strptime('Today is 5 December, 2019.', 'Today is %d %B, %Y.')
print(t)
new_year = datetime(2023,1,1)
diff = new_year - current_date
print(diff)
# 1 January 1970
start_date = datetime(1970,1,1)
diff = current_date - start_date
print(f'Different between {start_date} and {current_date} is {diff}')