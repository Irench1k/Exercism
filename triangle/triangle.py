def equilateral(sides: list[float]) -> bool:
    a, b, c = sides
    if is_triangle(sides):
        if a == b == c:
            return True
    return False


def isosceles(sides: list[float]) -> bool:
    a, b, c = sides
    if is_triangle(sides):
        if a == b or b == c or a == c:
            return True
    return False


def scalene(sides: list[float]) -> bool:
    a, b, c = sides
    if is_triangle(sides):
        if a != b and b != c and a != c:
            return True
    return False


def is_triangle(sides: list[float]) -> bool:
    a, b, c = sides
    if a + b + c > 0:
        if a + b >= c and b + c >= a and a + c >= b:
            return True
        return False
    return False
