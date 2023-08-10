def square(number: int):
    if number in range(1, 65):
        result = pow(2, number-1)
        return result
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    return pow(2, 64) - 1
