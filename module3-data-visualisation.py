import matplotlib.pyplot as plt
import matplotlib

from numpy.random import randn
import numpy as np
import seaborn as sns
matplotlib.use('TkAgg')
import pandas as pd

df = pd.read_csv('Модуль 3. Визуализация данных/files/heart.csv')
print(df.info())

figure = plt.figure()
df.ChestPainType.value_counts().sort_index().plot.line()
plt.show()

