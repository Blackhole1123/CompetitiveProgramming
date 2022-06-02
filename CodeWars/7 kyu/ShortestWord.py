def find_short(s):
    s = s.split(' ')
    shortlen = 0
    for i in range(len(s)):
        if i == 0:
            shortlen = len(s[i])
        elif (i != 0 and len(s[i]) < shortlen):
            shortlen = len(s[i])
    return shortlen