def convert(number: int) -> str:
    result = ''
    if by_3(number):
        result += 'Pling'
    if by_5(number):
        result += 'Plang'
    if by_7(number):
        result += 'Plong'
    
    return result or str(number)


def by_3(number: int) -> bool:
    return number % 3 == 0


def by_5(number: int) -> bool:
    return number % 5 == 0


def by_7(number: int) -> bool:
    return number % 7 == 0
