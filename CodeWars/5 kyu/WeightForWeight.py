def digiSum(n):
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum

def order_weight(strng):
    bar = sorted(strng.split(' '))
    baz = sorted(bar, key=digiSum)
    return " ".join(baz)