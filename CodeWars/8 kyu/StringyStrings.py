def stringy(size):
    return ''.join(str(abs(i%2 - 1)) for i in range(size))