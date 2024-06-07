"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time: int):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time



def preparation_time_in_minutes(layers: int):
    """Calculate the preparation time.

    :param layers: int - number of layers of lasagna.
    :return: int - preparation time (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the number of layers you want to add to the lasagna as
    an argument and returns how many minutes you would spend making them.
    """

    return layers * PREPARATION_TIME


def elapsed_time_in_minutes(layers: int, elapsed_bake_time: int):
    """Calculate the elapsed time.

    :param layers: int - number of layers of lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - elapsed time (in minutes) derived from 'PREPARATION_TIME' and 'EXPECTED_BAKE_TIME'.

    Function that takes two arguments: the first is the number of layers you want to add to the
    lasagna, and the second is the number of minutes the lasagna has been in the oven.
    The function should return how many minutes in total you've worked on cooking the meal.
    """

    return preparation_time_in_minutes(layers) + elapsed_bake_time