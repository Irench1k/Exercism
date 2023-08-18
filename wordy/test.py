def plus(a: int, b: int) -> int:
    return a + b


def minus(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: int, b: int) -> int:
    return a // b


def cheking(question: str):
    if not question.startswith('What is') or 'cubed' in question:
        raise ValueError("unknown operation")

    question = question.removeprefix("What is").removesuffix("?").strip()
    question = question.split()

    first_term = int(question[0])
    action_string = ' '.join(question[1:])

    return first_term, action_string

first_term, action_string = cheking(question)


def action_list(action_string: str) -> list[tuple(function, int)]:
    words = action_string.split()
    result = []
    i = 0

    while i < len(words):
        if words[i] == 'plus':
            action = plus
            value = int(words[i + 1])
            result.append((action, value))
            processed = 2
        elif words[i] == 'minus':
            action = minus
            value = int(words[i + 1])
            result.append((action, value))
            processed = 2
        elif words[i] == 'multiplied' and words[i + 1] == 'by':
            action = multiply
            value = int(words[i + 2])
            result.append((action, value))
            processed = 3
        elif words[i] == 'divided' and words[i + 1] == 'by':
            action = divide
            value = int(words[i + 2])
            result.append((action, value))
            processed = 3
        else:
            raise ValueError("syntax error")
        i += processed

    return result


def execute(result) -> int:
    answer = first_term
    for action, value in result:
        answer = action(answer, value)
    return answer


print(cheking("What is 5 plus 5 minus 10?"))
print(action_list('plus 5 minus 10 multiplied by 9'))
