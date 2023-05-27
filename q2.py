# Вопрос 2. Линейный алгоритм. Префиксные суммы. Решение задачи о запросе суммы на отрезке.
# Задача. Пусть дан массив a0, a1, ... an−1. В элементах массива записано количество осадков, выпавших
# в моменты времени 0, 1, ..,n−1. Необходимо ответить на m запросов о количестве осадков,
# выпавших с i-го по j-й момент времени (1≤i≤j≤n). Формулируя задачу более строго, необходимо
# уметь отвечать на запросы суммы элементов массива на отрезке c [i;j].

# prefix_sum[i] = a[0] + a[1] + ... + a[i]
# sum[i,j] = prefix_sum[j] - prefix_sum[i-1]

def prefix_sum(arr):
    n = len(arr)
    prefix_sum = [0] * n
    prefix_sum[0] = arr[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]
    return prefix_sum

def sum_range(prefix_sum, i, j):
    if i == 0:
        return prefix_sum[j]
    else:
        return prefix_sum[j] - prefix_sum[i-1]

