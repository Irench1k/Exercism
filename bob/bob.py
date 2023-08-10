def response(hey_bob: str) -> str:
    hey_bob = hey_bob.strip()
    if is_questioning(hey_bob) and is_shouting(hey_bob):
        return "Calm down, I know what I'm doing!"

    if is_questioning(hey_bob):
        return "Sure."
    
    if is_shouting(hey_bob):
        return "Whoa, chill out!"
    
    if is_silence(hey_bob):
        return "Fine. Be that way!"
    
    return "Whatever."


def is_shouting(hey_bob: str) -> bool:
    return hey_bob.isupper()


def is_questioning(hey_bob: str) -> bool:
    return hey_bob.endswith("?")
    

def is_silence(hey_bob: str) -> bool:
    return not hey_bob
