def is_valid(isbn: str):
    isbn = isbn.replace("-", "")
    result = 0
    infinite_number = "0123456789"

    if len(isbn) == 10:
        if isbn[-1] != "X" and isbn[-1] not in infinite_number:
            return False
        
        if isbn[-1] == "X":
            isbn[-1] = "10"
        
        for index, digit in enumerate(isbn):
            factor = len(isbn) - index
            product = int(digit) * factor
            result += product
    
        if result % 11 == 0:
            return True
        return False
    return False


print(is_valid("3-598-21508-X"))
