"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name: str, dish_ingredients: list[str]) -> tuple:
    ingredients = set(dish_ingredients)
    return dish_name, ingredients

def check_drinks(drink_name: str, drink_ingredients: list[str]) -> str:
    if set(drink_ingredients).intersection(ALCOHOLS):
        return drink_name + " Cocktail"
    else:
        return drink_name + " Mocktail"


def categorize_dish(dish_name: str, dish_ingredients: list[str]) -> str:
    dish_category = {
    "VEGAN": VEGAN,
    "VEGETARIAN": VEGETARIAN,
    "PALEO": PALEO,
    "KETO": KETO,
    "OMNIVORE": OMNIVORE
    }
    for category in dish_category:
        if set(dish_ingredients).issubset(dish_category[category]):
            return dish_name + ": " + category


def tag_special_ingredients(dish: tuple[str, list[str]])  -> tuple[str, set[str]]:
    dish_ingredients = set(dish[1])
    return dish[0], dish_ingredients.intersection(SPECIAL_INGREDIENTS)
         


def compile_ingredients(dishes: list[str]) -> set[str]:
    return set().union(*dishes)


def separate_appetizers(dishes: list[str], appetizers: list[str]) -> list[str]:
    dishes_set = set(dishes)
    appetizers_set = set(appetizers)
    return list(dishes_set.difference(appetizers_set))


def singleton_ingredients(dishes: list[set[str]],
                          intersection: set[str]) -> set[str]:
    """Determine which `dishes` have a singleton ingredient (an ingredient that only appears once across dishes).

    :param dishes: list - of ingredient sets.
    :param intersection: constant - can be one of `<CATEGORY>_INTERSECTIONS` constants imported from `sets_categories_data.py`.
    :return: set - containing singleton ingredients.

    Each dish is represented by a `set` of its ingredients.

    Each `<CATEGORY>_INTERSECTIONS` is an `intersection` of all dishes in the category. `<CATEGORY>` can be any one of:
        (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).

    The function should return a `set` of ingredients that only appear in a single dish.
    """

    singletons: set[str] = set()

    empty_set: set[str] = set()
    dish_set: set[str] = empty_set.union(*dishes)

    dish: set[str] = dish_set.difference(intersection)
    singletons.update(dish)
    return singletons
