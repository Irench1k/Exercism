color_values = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}


color_tolerance = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10
}


def value(colors: list[str]) -> int:
    """Changes the first two colors into an integer."""
    result: list[int] = []
    if len(colors) == 4:
        for color in colors:
            result.append(color_values[color])
            if len(result) == 2:
                break
    else:
        for color in colors:
            result.append(color_values[color])
            if len(result) == 3:
                break
    return int(''.join(map(str, result)))


def get_ohms(colors: list[str]) -> int:
    """Calculates the third/fourth colour into a power of 10."""
    if colors[-2] in color_values:
        zeros = color_values[colors[-2]]
        return 10 ** zeros
    else:
        return 1


def get_tolerance(colors: list[str]) -> float:
    """Converts the last color into the tolerance value."""
    return color_tolerance[colors[-1]]


def get_prefix(resistance: int, divider: int) -> int | float:
    """Converts result into an integer if the result is 2.0 == 2."""
    if resistance % divider == 0:
        return int(resistance / divider)
    else:
        return resistance / divider


def resistor_label(colors: list[str]):
    """Main function of the program."""
    if len(colors) == 1:
        return "0 ohms"

    ohms = get_ohms(colors)
    resistance_value = value(colors)
    tolerance = get_tolerance(colors)
    last_chance = (resistance_value * ohms)
    if last_chance >= 1_000_000_000:
        prefix = "giga"
        last_chance = get_prefix(last_chance, 1_000_000_000)
    elif last_chance >= 1_000_000:
        prefix = "mega"
        last_chance = get_prefix(last_chance, 1_000_000)
    elif last_chance >= 1_000:
        prefix = "kilo"
        last_chance = get_prefix(last_chance, 1_000)
    else:
        prefix = ""
    
    return f"{last_chance} {prefix}ohms ± {tolerance}%"


print(resistor_label(["orange", "orange", "yellow", "black", "brown"]))
