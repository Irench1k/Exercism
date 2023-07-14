def get_rounds(number: int) -> list[int]:
    number2 = number + 1
    number3 = number + 2
    rounds = [number, number2, number3]
    return rounds


def concatenate_rounds(rounds_1: list[int], rounds_2: list[int]) -> list[int]:
    poker_rounds = rounds_1 + rounds_2
    return poker_rounds


def list_contains_round(rounds: list[int], number: int) -> bool:
    if number in rounds:
        return True
    return False


def card_average(hand: list[int]) -> float:
    average = sum(hand) / len(hand)
    return average


def approx_average_is_average(hand: list[int]) -> bool:
    first_and_last = (hand[0] + hand[-1]) / 2.0
    middle_card = hand[len(hand) // 2]

    if card_average(hand) == first_and_last or card_average(hand) == middle_card:
        return True
    return False


def average_even_is_average_odd(hand: list[int]) -> bool:
    even_average = card_average(hand[::2])
    odd_average = card_average(hand[::1])
    if even_average == odd_average:
        return True
    return False


def maybe_double_last(hand: list[int]) -> list[int]:
    if hand[-1] == 11:
        hand[-1] *= 2
    return hand