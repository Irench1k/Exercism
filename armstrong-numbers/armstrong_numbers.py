def is_armstrong_number(number: int) -> bool:
    digits = []
    for digit in str(number):
        digit = int(digit)
        digits.append(digit)
    
    power = len(digits)
    digits_in_power = []
    for digit in digits:
        digit_in_power = pow(digit, power)
        digits_in_power.append(digit_in_power)
    
    result = sum(digits_in_power)
    if result == number:
        return True
    return False


print(is_armstrong_number(153))
