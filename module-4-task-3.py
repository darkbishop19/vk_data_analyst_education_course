import numpy as np
math_grades = [85, 90, 78, 92, 88, 85, 76, 98, 94, 87]
#расчитать стандартное отклонение
s = np.std(math_grades, ddof=1)
# print(s)
#6.783

#4 задание - выборочное среднее оценок студентов
mean = np.mean(math_grades)
# print(mean)
#87.3

#5 задание - выборочная медиана оценок студентов
median = np.median(math_grades)
# print(median)
#87.5
