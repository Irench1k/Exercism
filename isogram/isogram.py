def is_isogram(word: str):
    word = word.lower()
    word = word.replace(" ", "").replace("-", "")
    letter_count = set()

    for letter in word:
        if letter in letter_count:
            return False
            
        else:
            letter_count.add(letter)
    return True


print(is_isogram("mother"))
