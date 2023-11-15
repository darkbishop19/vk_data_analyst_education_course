import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np
import pandas as pd

np.random.seed(1234)

norm_rv1 = stats.norm(loc=35, scale = 5)
# scale - стандартное отклонение
# loc - среднее

#генерирует случайные значения из распредления norm_rv1
gen_pop = norm_rv1.rvs(size=1000)

fig = plt.figure(figsize=(14, 7))
ax1 = plt.subplot(111)
plt.hist(gen_pop, 50, alpha=0.5)
plt.show()