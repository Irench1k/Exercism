def equilateral(sides: list[float]) -> bool:
    a, b, c = sides
    return is_triangle(sides) and (a == b == c)


def isosceles(sides: list[float]) -> bool:
    a, b, c = sides
    return is_triangle(sides) and (a == b or b == c or a == c)


def scalene(sides: list[float]) -> bool:
    a, b, c = sides
    return is_triangle(sides) and (a != b and b != c and a != c)


def is_triangle(sides: list[float]) -> bool:
    a, b, c = sides
    return (a + b + c > 0) and (a + b >= c and b + c >= a and a + c >= b)
