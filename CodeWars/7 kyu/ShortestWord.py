def find_short(s):
    s = s.split(' ')
    short = 0
    for i in range(len(s)):
        if i == 0:
            short = len(s[i])
        elif (i != 0 and len(s[i]) < short):
            short = len(s[i])
    return short