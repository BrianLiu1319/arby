from fuzzywuzzy import fuzz


def lev_ratio(str1, str2):
    """
    return levenshtein distance between two strings

    input: str, str
    output: int
    """
    ratio = fuzz.ratio(str1.lower(), str2.lower())
    return ratio


def partial_ratio(str1, str2):
    """
    return partial ratio between two strings

    input: str, str
    output: int
    """
    ratio = fuzz.partial_ratio(str1.lower(), str2.lower())
    return ratio


def token_set_ratio(str1, str2):
    """
    return ratios of each individual tokens between two strings

    input: str, str
    output: int
    """
    ratio = fuzz.token_set_ratio(str1, str2)
    return ratio

def avg_ratio(str1, str2):
    """
    return avg ratio of token_set, partial, and lev

    input: str, str
    output: int
    """
    ratio = token_set_ratio(str1,str2) + partial_ratio(str1, str2) + lev_ratio(str1, str2)
    ratio /= 3
    
    return ratio
