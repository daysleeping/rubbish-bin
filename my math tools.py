import math

def IsOdd(a):
    x = abs(math.remainder(a,2))
    if x == 1:
        return True
    else:
        return False

def IsEven(a):
    x = abs(math.remainder(a,2))
    if x == 1:
        return False
    else:
        return True

def Is_prime(a):
    b = 2
    while b != a:
        r = math.remainder(a,b)
        if r == 0:
            return False
        b += 1
    return True

print(Is_prime(9))
