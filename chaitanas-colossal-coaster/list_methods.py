"""Functions to manage and organize queues at Chaitana's roller coaster."""


def add_me_to_the_queue(express_queue: list[str], normal_queue: list[str], ticket_type: int, person_name: str) -> list[str]:
    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    else:
        normal_queue.append(person_name)
        return normal_queue


def find_my_friend(queue: list[str], friend_name: str) -> int:
    return queue.index(friend_name)


def add_me_with_my_friends(queue: list[str], index: int, person_name: str) -> list[str]:
    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue: list[str], person_name: str) -> list[str]:
    queue.remove(person_name)
    return queue


def how_many_namefellows(queue: list[str], person_name: str) -> int:
    num = queue.count(person_name)
    return num


def remove_the_last_person(queue: list[str]) -> str:
    person = queue.pop(-1)
    return person


def sorted_names(queue: list[str]) -> list[str]:
    queue.sort()
    return queue
