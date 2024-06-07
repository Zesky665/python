"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number) -> list:
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2) -> list:
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number) -> bool:
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds


def card_average(hand) -> float:
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand) -> bool:
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    average_of_first_and_last = (hand[0] + hand[-1]) / 2
    middle_card = hand[len(hand) // 2]
    real_card_average = card_average(hand)

    first_test = average_of_first_and_last == real_card_average
    second_test = middle_card == real_card_average

    return first_test or second_test


def average_even_is_average_odd(hand) -> bool:
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even_cards = hand[::2]
    odd_cards = hand[1::2]
    even_cards_average = sum(even_cards) / len(even_cards)
    odd_cards_average = sum(odd_cards) / len(odd_cards)

    return even_cards_average == odd_cards_average


def maybe_double_last(hand) -> list:
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] *= 2

    return hand
