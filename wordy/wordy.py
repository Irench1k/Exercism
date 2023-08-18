from typing import Callable
ListOfOperations = list[tuple[Callable[[int, int], int], int]]


def plus(a: int, b: int) -> int:
    return a + b


def minus(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: int, b: int) -> int:
    return a // b


def answer(question: str) -> int:
    '''Main function which is called by Exercism test suite.'''
    first_term, action_string = checking(question)
    try:
        operators_and_numbers = action_list(action_string)
    except:
        raise ValueError("syntax error")
    
    result = execute(first_term, operators_and_numbers)
    return result


def checking(question: str) -> tuple[int, str]:
    """Checks the question and convert it into a tuple of the first int and rest as a string"""
    if not question.startswith('What is') or 'cubed' in question:
        raise ValueError("unknown operation")

    question = question.removeprefix("What is").removesuffix("?").strip()
    list_question = question.split()

    try:
        first_term = int(list_question[0])
    except:
        raise ValueError("syntax error")

    action_string = ' '.join(list_question[1:])

    return first_term, action_string


def action_list(action_string: str) -> ListOfOperations:
    """('plus 5 minus 10') -> [(plus, 5), (minus, 10)]"""
    words = action_string.split()
    result: ListOfOperations = []
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


def execute(first_term: int, operators_and_numbers: ListOfOperations) -> int:
    """Calculates the final answer"""
    answer = first_term
    for action, value in operators_and_numbers:
        answer = action(answer, value)
    return answer


print(answer("What is plus 5 10?"))
