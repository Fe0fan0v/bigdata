import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd

LABELS_SIZE = 14


def getColors(n):
    COLORS = []
    cm = plt.cm.get_cmap('hsv', n)
    for i in range(n):
        COLORS.append(cm(i))
    return COLORS


def dict_sort(d):
    keys = []
    vals = []
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    for k, v in d:
        keys.append(k)
        vals.append(v)
    return keys, vals


ds = pd.read_csv('complete.csv', escapechar='`', low_memory=False, error_bad_lines=False)

country_count = pd.value_counts(ds['country'].values, sort=True)

plt.title('Страны с большим количеством наблюдений', fontsize=LABELS_SIZE)
plt.bar(range(len(country_count)), dict_sort(dict(country_count))[1],
        color=getColors(len(country_count)))
plt.xticks(range(len(country_count)),
           dict_sort(dict(country_count))[0])
plt.show()
