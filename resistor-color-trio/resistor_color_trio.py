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


def value(colors: list[str]) -> int:
    """Changes the first two colors into an integer."""
    result: list[int] = []
    for color in colors:
        if len(colors) == 4:
            result.append(color_values[color])
            if len(result) == 2:
                break
        else:
            result.append(color_values[color])
            if len(result) == 3:
                break
    return int(''.join(map(str, result)))


def get_ohms(colors: list[str]) -> int:
    """Calculates the third colour into a power of 10."""
    if len(colors) == 4:
        if colors[2] in color_values:
            zeros = color_values[colors[2]]
            return 10 ** zeros
        else:
            return 1
    else:
        if colors[3] in color_values:
            zeros = color_values[colors[2]]
            return 10 ** zeros
        else:
            return 1


def label(colors: list[str]) -> str:
    """Main function of the program"""
    ohms = get_ohms(colors)
    resistance_value = value(colors)
    last_chance = (resistance_value * ohms)
    if last_chance >= 1_000_000_000:
        prefix = "giga"
        last_chance //= 1_000_000_000
    elif last_chance >= 1_000_000:
        prefix = "mega"
        last_chance //= 1_000_000
    elif last_chance >= 1_000:
        prefix = "kilo"
        last_chance //= 1_000
    else:
        prefix = ""
    
    return f"{last_chance} {prefix}ohms"


print(label(["orange", "orange", "black", "red", "green"]))
