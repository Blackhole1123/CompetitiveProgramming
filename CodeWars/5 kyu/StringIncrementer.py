def increment_string(strng):
    h = strng.rstrip('0123456789')
    t = strng[len(h):]
    if t == "": return strng+"1"
    return h + str(int(t) + 1).zfill(len(t))