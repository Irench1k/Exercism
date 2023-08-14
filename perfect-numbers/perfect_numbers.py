def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    factors = 0
    for n in range(1, number):
        if number % n == 0:
            factors += n

    if number == factors:
        return "perfect"
    if number < factors:
        return "abundant"
    if number > factors:
        return "deficient"


print(classify(6))
