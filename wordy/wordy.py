def plus(a: int, b: int) -> int:
    return a + b


def minus(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: int, b: int) -> int:
    return a // b


operations = {
    'plus': plus,
    'minus': minus,
    'multiplied by': multiply,
    'divided by': divide
}


def answer(question: str):
    if not question.startswith('What is') or 'cubed' in question:
        raise ValueError("unknown operation")

    question = question.removeprefix("What is").removesuffix("?").strip()
    list_question = question.split()

    result = int(list_question[0])
    i = 1
    while i < len(list_question):
        number = result
        operator = list_question[i]
        next_number = int(list_question[i + 1])

        if operator in operations:
            result = operations[operator](number, next_number)
            print(f"The result is: {result}")
        else:
            raise ValueError("syntax error")
        i += 2
        
    return result


print(answer('What is 5 plus 5 plus -12?'))



def preprocess(input_string: str) -> tuple[int, str]:
    pass

initial_value, action_string = preprocess(input_string)

#initial_value = 5
#action_string = "multiple by 2 plus 6"

actions = action_list(action_string)

#actions = [("multiple by", 2), ("plus", 6)]
#actions = [(multiply, 2), (plus, 6)]


result = execute(initial_value, actions)


def execute(initial_value: int, actions: list[tuple]) -> int:
    result = inital_value
    for action_fn, value in actions:
        result = action(result, value)

    return result
