def exchange_money(budget: float, exchange_rate: float) -> float:
    return budget / exchange_rate


def get_change(budget: float, exchanging_value: float) -> float:
    left_money = budget - exchanging_value
    return left_money


def get_value_of_bills(denomination: float, number_of_bills: float) -> int:
    total_bills = int(denomination * number_of_bills)
    return total_bills


def get_number_of_bills(budget: float, denomination: float) -> float:
    number_of_currency_bills = budget // denomination
    return number_of_currency_bills


def get_leftover_of_bills(budget: float, denomination: float) -> float:
    leftover = budget % denomination
    return leftover


def exchangeable_value(budget: float, exchange_rate: float, spread: int, denomination: int) -> int:
    new_exchange_rate = (exchange_rate * (spread / 100)) + exchange_rate
    total_budget = budget / new_exchange_rate
    total_currency_denmination = total_budget // denomination
    result = int(total_currency_denmination * denomination)
    return result
