def steps(n: int):
    if n <= 0:
        raise ValueError("Only positive integers are allowed")
    number_of_steps = 0
    while n != 1:
        if n % 2 == 0:
            number_of_steps += 1
            n =  n / 2
            print(f"Its even and the result is: {n}")
        else:
            number_of_steps += 1
            n = (n * 3) + 1
            print(f"Its odd and the result is: {n}")
    return number_of_steps


print(steps(12))
