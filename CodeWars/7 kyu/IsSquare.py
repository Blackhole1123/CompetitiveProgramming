def is_square(n):  
    num = n  
    if num < 0:
        return False
    if num == 0:
        return True
    else:
        return int(num**0.5)**2 == num