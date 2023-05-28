# Вопрос 16. Геометрия на плоскости. Площадь многоугольника. Задача. На плоскости задан многоугольник координатами вершин в порядке их обхода. Многоугольник не обязательно выпуклый. Требуется найти его площадь.

# To find the area of a polygon given the coordinates of its vertices, you can use the shoelace formula. The shoelace formula gets its name because if you list the coordinates in a column, it looks like the lacing of a shoe. Here is an example Python function that implements the shoelace formula for finding the area of a polygon:

def polygon_area(vertices):
    n = len(vertices)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[i][1] * vertices[j][0]
    return abs(area) / 2
  

# The vertices parameter is a list of (x, y) tuples representing the coordinates of the vertices of the polygon. The function first calculates the number of vertices n, initializes the area to zero, and then iterates over each vertex and calculates a term of the shoelace formula. Finally, the absolute value of the area is divided by 2 to get the final result.

# Here is an example usage of the polygon_area function:

vertices = [(0, 0), (0, 1), (1, 1), (1, 0)]
area = polygon_area(vertices)
print(area)  # prints 1.0

