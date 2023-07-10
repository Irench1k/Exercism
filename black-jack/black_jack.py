def value_of_card(card):
    if card in ["J", "Q", "K"]:
        return 10
    elif card is "A":
        return 1
    else:
        return int(card)
    
    

def higher_card(card_one, card_two):
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    elif value_of_card(card_one) < value_of_card(card_two):
        return card_two
    else:
        return card_one, card_two


def value_of_ace(card_one, card_two):

    if value_of_card(card_one) + value_of_card(card_two) >= 11 or card_one == "A" or card_two == "A":
        return 1
    else:
        return 11
    

def is_blackjack(card_one, card_two):
    if card_one == "A" and card_two in ["J", "Q", "K", "10"]:
        return True
    elif card_two == "A" and card_one in ["J", "Q", "K", "10"]:
        return True
    else:
        return False


def can_split_pairs(card_one, card_two):
    if value_of_card(card_one) == value_of_card(card_two):
        return True
    return False


def can_double_down(card_one, card_two):
    value = value_of_card(card_one) + value_of_card(card_two)
    if value in [9, 10, 11]:
        return True
    return False
