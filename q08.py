# Вопрос 8. Линейные структуры данных. Очередь. Определение и возможные реализации. Задача «Раздача подарков». Громозека раздавал N земным детям, стоящим по кругу, привезенные подарки. Чтобы не было никому обидно, Громозека решил, что будет каждый раз давать подарок K-му ребенку. Ребенок, получивший подарок с радостью выбегал из круга, а все остальные смыкали круг. Определите, в каком порядке дети получали подарки. Входные данные Входная строка содержит натуральные числа N и K, разделённые пробелом. Выходные данные Программа должна вывести в одну строку, через пробел, номера ребят в том порядке, как они получают подарок.

# Для решения данной задачи можно использовать структуру данных "очередь". Очередь представляет собой линейную структуру данных, которая работает по принципу "первым пришел - первым ушел" (FIFO). В Python можно реализовать очередь с помощью встроенного модуля collections и класса deque.

from collections import deque

n, k = map(int, input().split())

# Создаем очередь и заполняем ее номерами детей от 1 до N
queue = deque(range(1, n + 1))

result = []

while queue:
    # Добавляем K-1 детей из начала очереди в ее конец
    for i in range(k - 1):
        queue.append(queue.popleft())

    # Добавляем K-го ребенка в список результатов и удаляем его из очереди
    result.append(queue.popleft())

# Выводим номера детей в порядке, в котором они получали подарки
print(*result)

# Конечная очередь (queue) - это структура данных, которая представляет собой упорядоченный список элементов, в которых первый элемент добавлен в начало, а последний элемент добавлен в конец. Очередь работает по принципу "первым пришел - первым ушел" (FIFO - first in, first out). Это означает, что первый элемент, который был добавлен в очередь, будет первым, который будет удален из очереди. Элементы могут добавляться только в конец очереди, а удаляться только из начала очереди. Очередь широко используется в программировании для решения различных задач, например, обработки задач в очереди, обработки сообщений в сетевых протоколах, обработки задач в параллельных вычислениях и т.д.

# Конечная очередь (queue) широко используется в программировании для решения различных задач. Вот несколько примеров использования очереди:

#     Буфер обмена: Очередь может использоваться в операционной системе в качестве буфера обмена для хранения данных, которые были скопированы или вырезаны из одного места и ожидают вставки в другое место.

#     Обработка задач в очереди: Очередь может использоваться для хранения задач, которые должны быть обработаны в определенном порядке. Например, задачи могут быть добавлены в очередь, когда они поступают, и обработаны в порядке их добавления.

#     Обработка сообщений в сетевых протоколах: Очередь может использоваться в сетевых протоколах для обработки сообщений, которые приходят в систему. Сообщения могут быть добавлены в очередь, когда они поступают, и обработаны в порядке их добавления.

#     Обработка задач в параллельных вычислениях: Очередь может использоваться в параллельных вычислениях для координации выполнения задач на нескольких процессорах. Задачи могут быть добавлены в очередь и обработаны параллельно на разных процессорах.

#     Обработка событий в графических интерфейсах: Очередь может использоваться в графических интерфейсах для обработки событий, которые происходят в приложении. События могут быть добавлены в очередь, когда они происходят, и обработаны в порядке их добавления.

#     Парсинг данных: Очередь может использоваться для парсинга больших объемов данных, например, при обработке логов. Данные могут быть добавлены в очередь и обработаны последовательно.

#     Работа с потоками данных: Очередь может использоваться для хранения данных, которые поступают в систему из разных источников. Данные могут быть добавлены в очередь и обработаны в порядке их добавления.


import queue

# Создаем очередь
q = queue.Queue()

# Добавляем элементы в очередь
q.put(1)
q.put(2)
q.put(3)

# Получаем элементы из очереди
print(q.get())  # 1
print(q.get())  # 2
print(q.get())  # 3

# Проверяем, пуста ли очередь
print(q.empty()) 

# В очереди можно выполнять следующие операции:
#     Добавление элемента в конец очереди: Это можно сделать с помощью метода put() в Python. Например, queue.put(item) добавляет элемент item в конец очереди.
#     Получение элемента из начала очереди: Это можно сделать с помощью метода get() в Python. Например, queue.get() возвращает первый элемент в очереди и удаляет его из очереди.
#     Проверка пустоты очереди: Это можно сделать с помощью метода empty() в Python. Например, queue.empty() возвращает True, если очередь пуста, и False, если в очереди есть элементы.
#     Получение размера очереди: Это можно сделать с помощью метода qsize() в Python. Например, queue.qsize() возвращает количество элементов в очереди.
#     Проверка наличия элемента в очереди: Это можно сделать с помощью оператора in в Python. Например, item in queue возвращает True, если элемент item есть в очереди, и False, если его нет.
#     Получение элемента из начала очереди без удаления: Это можно сделать с помощью метода peek() в Python. Например, queue.peek() возвращает первый элемент в очереди, не удаляя его.
#     Ожидание добавления элемента в очередь: Это можно сделать с помощью метода join() в Python. Например, queue.join() блокирует исполнение до тех пор, пока не будут добавлены все элементы в очередь.
#     Очистка очереди: Это можно сделать с помощью метода clear() в Python. Например, queue.clear() удаляет все элементы из очереди.

