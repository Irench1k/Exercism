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
    result = []
    for color in colors:
        if color in color_values:
            number = color_values[color]
            result.append(number)
            if len(result) == 2:
                break
    if result:    
        final = int(''.join(map(str, result)))
        return final
    else:
        return 0
