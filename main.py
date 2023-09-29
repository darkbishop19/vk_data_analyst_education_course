'''Вопрос 1
Создайте вектор NumPy, который содержит значения от 10 до 500. Возведите все значения вектора в квадрат и вычтите из каждого элемента вектора число 234. Чему равна сумма всех элементов получившегося вектора?
(ответ введите целым числом без пробелов)
'''
import numpy as np

# Создаем вектор от 10 до 500
def chat_solution():
    vector = np.arange(10, 501)

    # Возводим все элементы в квадрат
    vector_squared = vector ** 2

    # Вычитаем из каждого элемента число 234
    result_vector = vector_squared - 234

    # Находим сумму всех элементов вектора
    sum_result = np.sum(result_vector)

    print(sum_result)

def my_soultion():
    vector = np.arange(10,501)
    sum_result = sum((vector**2)-234)
    print(sum_result)

'''Ответ получается одинаковым !'''