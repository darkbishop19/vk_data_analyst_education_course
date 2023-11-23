import statsmodels.stats.api as sms

#Необходимо найти левую границу доверительного интервала с уровнем доверия (обратно уровню значимости - альфа ) равным 95%.
# Точность - 2 знака после запятой.

response_times = [150, 130, 140, 160, 180, 170, 190, 200, 175, 165]
t = sms.DescrStatsW(response_times)
interval = t.tconfint_mean(alpha=0.05, alternative='two-sided')
print(interval)

