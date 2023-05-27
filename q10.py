# Вопрос 10. Бинарный поиск. Метод реализации. Задача. Найдите такое число x, что x2 + √x = C, с точностью не менее 6 знаков после точки.

# To solve this problem, we can use the binary search method. First, we need to set the boundaries for our search. Since x is a positive number, we can set the lower boundary as 0 and the upper boundary as C. Then, we can start performing binary search by finding the mid-point between the lower and upper boundaries. We can calculate the value of the left-hand side of the equation x^2 + sqrt(x) using the mid-point value of x.

# If this value is greater than C, then we know that the solution lies in the left half of the search space, so we can update our upper boundary to be the mid-point value. If the value is less than C, then the solution lies in the right half of the search space, so we can update our lower boundary to be the mid-point value. We can keep performing this process until we find a value of x that satisfies the equation with the desired precision.

import math

def find_x(C):
    EPSILON = 1e-6
    left, right = 0, C

    while right - left > EPSILON:
        mid = (left + right) / 2
        if mid * mid + math.sqrt(mid) > C:
            right = mid
        else:
            left = mid

    return round(mid, 6)
  
#In this implementation, we set EPSILON to be thetolerance level for our solution, which is 1e-6 (i.e. 6 decimal places). We start with the lower and upper boundaries as 0 and C, respectively. Then, we perform binary search by finding the mid-point between the left and right boundaries. If the value of the equation at the mid-point is greater than C, we update the upper boundary to be the mid-point value, else we update the lower boundary to be the mid-point value.

# We keep performing this process until the difference between the left and right boundaries is less than the tolerance level. Finally, we return the mid-point value rounded to 6 decimal places as the solution to the equation
