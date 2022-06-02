import string

def is_pangram(s):
    s = s.lower().strip()
    if len(s) < 26:
        return False
    for i in string.ascii_lowercase:
        if i not in s:
            return False
    return True