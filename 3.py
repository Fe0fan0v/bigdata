from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('ufo.csv', low_memory=False)
countries = pd.value_counts(df['country'].values)
months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
          'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
counts = {}
for i in df['datetime']:
    m, d, yt = i.split('/')
    y, t = yt.split(' ')
    if y in counts.keys():
        counts[y] += 1
    else:
        counts[y] = 1
plt.bar(counts.keys(), counts.values())
plt.xticks(list(counts.keys()), counts.keys(), rotation=90)
plt.ylabel('Частота появления')
plt.show()
shapes = pd.value_counts(df['shape'].values)
plt.bar(range(len(shapes)), shapes)
plt.xticks(range(len(shapes)), list(dict(shapes).keys()), rotation=90)
plt.show()
