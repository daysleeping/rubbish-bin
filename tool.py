import math

def reverse_array(list):
    a = 0
    b = len(list) // 2
    while a != b:
        c = list[a]
        list[a] = list[len(list) - 1 - a]
        list[len(list) - 1 - a] = c
        a += 1
    return list

def move_zeroes(nums):
        a = 0
        b = 0
        if nums == [0]:
            return []
        if len(nums) == 1 and nums != [0]:
            return nums
        while a < len(nums) - 1:
            if nums[a] == 0:
                nums.pop(a)
                b += 1
                a -= 1
            a += 1
        
        while b != 0:
            nums.append(0)
            b -= 1
        return nums

def Is_prime(a):
    b = 2
    while b != a:
        r = math.remainder(a,b)
        if r == 0:
            return False
        b += 1
    return True

def get_prime(b):
    list = [2]
    while b != 2:
        if Is_prime(b):
            list.append(b)
        b -= 1
    list.sort()
    return list

def prime_factorization(a):
    if Is_prime(a):
        return [a]
    list = get_prime(a)
    list_2 = []
    x = 0
    while x != len(list) - 1:
        r = abs(math.remainder(a,list[x]))
        if r == 0:
            list_2.append(list[x])
            a = a / list[x]
        else:
            x += 1
    return list_2

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
