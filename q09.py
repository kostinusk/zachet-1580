# Вопрос 9. Бинарный поиск. Метод реализации. Задача. Напишите программу, которая находит в массиве элемент, самый близкий по величине к данному числу.

# Бинарный поиск - это алгоритм поиска элемента в упорядоченном массиве данных. Он работает путем деления массива пополам и последующего сравнения искомого элемента с элементом, находящимся в середине массива. Если искомый элемент меньше среднего элемента, поиск продолжается в левой половине массива; если искомый элемент больше среднего элемента, поиск продолжается в правой половине массива. Этот процесс повторяется до тех пор, пока искомый элемент не будет найден или пока размер массива не станет равным нулю.

# Бинарный поиск является очень эффективным алгоритмом поиска, так как он имеет сложность O(log n), где n - это количество элементов в массиве. Это означает, что время выполнения алгоритма увеличивается не пропорционально размеру входных данных, а логарифмически.

def binary_search(arr, target):
    min_diff = float('inf')
    min_index = None
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        diff = abs(target - arr[mid])
        if diff < min_diff:
            min_diff = diff
            min_index = mid

        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return mid

    return min_index

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

target = 25

result = binary_search(arr, target)

print("The element closest to the target is: ", arr[result])
