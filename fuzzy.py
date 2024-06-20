from fuzzywuzzy import fuzz



def lev_ratio (str1, str2):
    """
    return levenshtein distance between two strings
    
    input: str, str
    output: int 
    """
    ratio = fuzz.ratio(str1.lower(), str2.lower())
    return ratio
    
print(lev_ratio('SUn', "saturn"))