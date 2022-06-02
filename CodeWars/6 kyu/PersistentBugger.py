def splitint(n):
    return [int(i) for i in str(n)]

def multiply(n):
    c = 1
    for i in n:
        c *= i
    return c

def persistence(n):
    if len(str(n)) == 1:
        return 0
    else:
        count = 0
        while len(str(n)) != 1:
            n = multiply(splitint(n))
            count += 1
        return count