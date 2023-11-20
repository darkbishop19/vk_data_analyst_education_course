from scipy import stats
a = [3.2, 5.1, 4.3, 6.7, 7.9, 4.8, 5.6, 6.2, 5.9]
b = [2.9, 4.5, 6.1, 5.8, 4.2, 5.3, 4.7, 6.5, 6.8]

print(stats.mannwhitneyu(a, b))