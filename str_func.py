def upper_string(word):
    return word.upper()


def capital_words(string) -> str:
    """return all words from list for main letter"""
    return ' 'join(s.capitalize() for s in string.split())

