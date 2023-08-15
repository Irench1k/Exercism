def is_pangram(sentence: str):
    alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    lowercase_sentence = sentence.lower()
    result = set(lowercase_sentence)
    if alphabet <= result:
        return True
    return False


print(is_pangram("abcdefghijklmnopqrstuvwxyz"))
