import string
alphabet_lowercase = list(string.ascii_lowercase)
alphabet_uppercase = list(string.ascii_uppercase)


def rotate(text: str, key: int) -> str:   
    resulting_list = []
    for letter in text:
        if letter.isupper():
            unicode_char = ord(letter)
            shifted_char = unicode_char + key
            char = chr(shifted_char)
            resulting_list.append(char)
        elif letter.islower():
            unicode_char = ord(letter)
            shifted_char = unicode_char + key
            char = chr(shifted_char)
            resulting_list.append(char)
        else:
            resulting_list.append(letter)

    result = ''.join(resulting_list)
    return result


print(rotate("HElLo, BRotHer!!1", 2))
