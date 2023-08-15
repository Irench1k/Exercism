def is_isogram(word: str):
    word = word.lower()
    word = word.replace(" ", "").replace("-", "")
    letter_count = {}

    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    for value in letter_count.values():
        if value != 1:
            return False
    return True


print(is_isogram("mother"))
