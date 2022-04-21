def rotate_string(s,offset):
    if offset == 0:
        return s
    if offset > len(s):
        offset = offset % len(s)
    return s[offset:] + s[:offset]


def str_str(source:str,target:str):
    m = 0
    i = 0
    c = 0
    b = 0
    a = -1
    while m != len(source) and a == -1:
        while i != len(target) and b == 0:
            print(f'i : {i}')
            print(f'm : {m}')
            print(f'source : {source[i + m]}')
            print(f'target : {target[i]}')
            print(f'formula : {i} + {m} = {i + m}')
            if i + m < len(source):
                if source[i + m] == target[i]:
                    c += 1
                else:
                    b = 1
                if c == len(target):
                    a = m
                print(f'C : {c}')
                print(f'A : {a}')
                i += 1
            else:
                print(f'{i} + {m} < {len(source) - 1}')
                return -1
        b = 0
        i = 0
        c = 0
        m += 1
    return a
  
  def product_exclude_itself(list):
    a = len(list) - 1
    b = len(list) - 1
    result = 1
    list1 = []
    while a != -1:
        while b != -1:
            if b != a:
                result = result * list[b]
            b -= 1
        list1.append(result)
        result = 1
        a -= 1
    return list1
  
  import math


def Is_prime(a):
    b = 2
    while b != a:
        r = math.remainder(a, b)
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
        r = abs(math.remainder(a, list[x]))
        if r == 0:
            list_2.append(list[x])
            a = a / list[x]
        else:
            x += 1
    return list_2
  
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

def reverse_array(list):
    a = 0
    b = len(list) // 2
    while a != b:
        c = list[a]
        list[a] = list[len(list) - 1 - a]
        list[len(list) - 1 - a] = c
        a += 1
    return list

def sumof_two_strings(a,b):
    a = a[::-1]
    b = b[::-1]
    pos = 0     # create pos variable
    if len(b) > len(a): # getting the largest variable
        pos1 = len(b)
    else:
        pos1 = len(a)
    print(len(a))
    print(len(b))
    ans = ''  # create a string variable
    while pos != pos1: # if two variables is not equal
        print(f'Current position : {pos}')
        result = 0
        if len(a) > pos and len(b) > pos:
            result = int(a[pos]) + int(b[pos])
            print(f'result = {a[pos]} + {b[pos]}')
            print(f'result : {result}')
        elif len(a) > pos:
            result = int(a[pos])
            print(f'result : {a[pos]}')
            print(f'result : {result}')
        else:
            result = int(b[pos])
            print(f'result : {b[pos]}')
            print(f'result : {result}')
        ans = ans + str(result)
        print(f'Ans : {ans}')
        pos += 1 
    return ans 
