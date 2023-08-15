from string import ascii_lowercase


def is_pangram(sentence: str):
    alphabet = set(ascii_lowercase)
    lowercase_sentence = sentence.lower()
    result = set(lowercase_sentence)
    if alphabet <= result:
        return True
    return False


print(is_pangram("abcdefghijklmnopqrstuvwxyz"))
