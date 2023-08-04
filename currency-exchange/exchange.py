def exchange_money(budget, exchange_rate):
    return budget / exchange_rate
    


def get_change(budget, exchanging_value):
    left_money = budget - exchanging_value
    return left_money


def get_value_of_bills(denomination, number_of_bills):
    total_bills = int(denomination * number_of_bills)
    return total_bills


def get_number_of_bills(budget, denomination):
    number_of_currency_bills = budget // denomination
    return number_of_currency_bills


def get_leftover_of_bills(budget, denomination):
    leftover = budget % denomination
    return leftover
    


def exchangeable_value(budget, exchange_rate, spread, denomination):
    exchange_fee = spread / 100
    exchange_rate_with_spread = exchange_rate * (1 + spread_decimal)
    exchanged_currency_value = budget * exchange_rate_with_spread
    max_exchanged_currency_value = int(exchanged_currency_value // denomination) * denomination
    
    return max_exchanged_currency_value 
