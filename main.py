'''


import csv
import datetime
from collections import Counter
import matplotlib.pyplot as plt

def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')

def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))

messages = load_csv('messages.csv')

checks = load_csv('checks.csv')

statuses = load_csv('statuses.csv')

hours = []

for message in messages:
    time = parse_time(message[4])
    hours.append(time.hour)

for check in checks:
    time = parse_time(check[2])
    hours.append(time.hour)

for status in statuses:
    time = parse_time(status[3])
    hours.append(time.hour)

hour_count = Counter(hours)

plt.bar(hour_count.keys(), hour_count.values())
plt.xlabel('Часы')
plt.ylabel('Количество событий')
plt.show()

'''