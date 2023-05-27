# Вопрос 1. Линейный алгоритм. Решение задачи о поиске максимальной разности.
# Задача. Дан массив a0, a1,...an−1. Необходимо выбрать в нём два элемента ai и aj такие, что i<j и разность
# (aj−ai) максимальна

# Для решения данной задачи можно применить простой линейный алгоритм, который работает за O(n) времени. Алгоритм заключается в следующем:

#     Инициализируем переменную max_diff нулевым значением.
#     Инициализируем переменную min_elem значением первого элемента массива.
#     Для каждого элемента a[i] в массиве, начиная со второго элемента:
#         Вычисляем разность diff = a[i] - min_elem.
#         Если diff больше текущего значения max_diff, то обновляем max_diff.
#         Если a[i] меньше текущего значения min_elem, то обновляем min_elem.
#     Возвращаем значение max_diff.

def max_diff(arr):
    n = len(arr)
    max_diff = 0
    min_elem = arr[0]
    
    for i in range(1, n):
        diff = arr[i] - min_elem
        
        if diff > max_diff:
            max_diff = diff
        if arr[i] < min_elem:
            min_elem = arr[i]
    return max_diff
  
#   Данный алгоритм проходит по массиву всего один раз, выполняя только по одной операции для каждого элемента. Поэтому его сложность составляет O(n), что делает его достаточно эффективным для решения данной задачи.
