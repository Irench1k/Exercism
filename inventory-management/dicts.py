"""Functions to keep track and alter inventory."""


def create_inventory(items: list[str]) -> dict[str, int]:
    item_counts = {}
    for item in items:
        number = items.count(item)
        item_counts[item] = number
    return item_counts


def add_items(inventory: dict[str, int], items: list[str]) -> dict[str, int]:
    result = inventory.copy()
    new_inventory = create_inventory(items)

    for key, value in new_inventory.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result


def decrement_items(inventory: dict[str, int], items: list[str]) -> dict[str, int]:
    result = inventory.copy()
    new_inventory = create_inventory(items)

    for key, value in new_inventory.items():
        if key in result:
            result[key] -= value
            if result[key] < 0:
                result[key] = 0
    return result


def remove_item(inventory: dict[str, int], item: str) -> dict[str, int]:
    if item in inventory:
        inventory.pop(item)
    return inventory


def list_inventory(inventory: dict[str, int]) -> list[str]:
    items = []
    for item, count in inventory.items():
        if inventory[item] > 0:
            items.append((item, count))
    return items
