def is_valid(isbn: str):
    isbn = isbn.replace("-", "")
    result = 0

    if len(isbn) != 10:
        return False
    else:
        for index, digit in enumerate(isbn):
            if digit.isdigit():
                result += int(digit) * (len(isbn) - index)
            elif isbn[-1] == "X":
                result += 10
            else:
                return False
            
    if result % 11 == 0:
        return True
    return False


print(is_valid("3-598-21507-X"))
