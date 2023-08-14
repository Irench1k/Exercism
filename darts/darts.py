import math


def score(x, y):
    hypotenuse = math.sqrt(x**2 + y**2)
    if hypotenuse > 10:
        return 0
    if 10 >= hypotenuse > 5:
        return 1
    if 5 >= hypotenuse > 1:
        return 5
    else:
        return 10


print(score(10, 0))
