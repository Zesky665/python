"""Functions to manage a users shopping cart items."""
from typing import Iterable, Union


def add_item(current_cart: dict[str, int], items_to_add: Iterable) -> dict[str, int]:
    """Add items to shopping cart.

    :param current_cart: dict[str, int] - the current shopping cart.
    :param items_to_add: Iterable - items to add to the cart.
    :return: dict[str, int] - the updated user cart dictionary.
    """
    for item in items_to_add:
        current_cart[item] = current_cart.setdefault(item, 0) + 1

    return current_cart


def read_notes(notes: Iterable) -> dict[str, int]:
    """Create user cart from an iterable notes entry.

    :param notes: Iterable of items to add to cart.
    :return: dict[str, int] - a user shopping cart dictionary.
    """
    return dict.fromkeys(notes, 1)


def update_recipes(ideas: dict[str, dict[str, int]], recipe_updates: dict[str, dict[str, int]]) -> dict[str, dict[str, int]]:
    """Update the recipe ideas dictionary.

    :param ideas: dict[str, dict[str, int]] - The "recipe ideas" dict.
    :param recipe_updates: dict[str, dict[str, int]] - dictionary with updates for the ideas section.
    :return: dict[str, dict[str, int]] - updated "recipe ideas" dict.
    """
    ideas.update(recipe_updates)

    return ideas


def sort_entries(cart: dict[str, int]) -> dict[str, int]:
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict[str, int] - a users shopping cart dictionary.
    :return: dict[str, int] - users shopping cart sorted in alphabetical order.
    """
    return dict(sorted(cart.items()))


def send_to_store(cart: dict[str, int], aisle_mapping: dict[str, dict[str, bool]]) -> dict[str, dict[int, str, bool]]:
    """Combine users order to aisle and refrigeration information.

    :param cart: dict[str, int] - users shopping cart dictionary.
    :param aisle_mapping: dict[str, dict[str, bool]] - aisle and refrigeration information dictionary.
    :return: dict[str, dict[int, str, bool]] - fulfillment dictionary ready to send to store.
    """
    new_cart: dict = {}

    for item, quantity in sorted(cart.items(), reverse=True):
        new_cart[item] = [quantity] + aisle_mapping.get(item, [])

    return new_cart

def update_store_inventory(fulfillment_cart: dict[str, dict[int, str, bool]], store_inventory: dict[str, dict[int, str, bool]]) ->  dict[str, dict[int | str, str, bool]]:
    """Update store inventory levels with user order.

    :param fulfillment cart: dict[str, dict[int, str, bool]] - fulfillment cart to send to store.
    :param store_inventory: dict[str, dict[int, str, bool]] - store available inventory
    :return: dict[str, dict[int | str, str, bool]] - store_inventory updated.
    """
    for item in fulfillment_cart:
        store_inventory[item][0] = store_inventory[item][0] - fulfillment_cart[item][0]
        if store_inventory[item][0] <= 0:
            store_inventory[item][0] = "Out of Stock"

    return store_inventory
