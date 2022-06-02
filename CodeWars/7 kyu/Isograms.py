def is_isogram(string):
    s = string.lower().strip()
    return len(s) == len(set(s))