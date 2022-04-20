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
        r = math.remainder(a, b)
        if r == 0:
            return False
        b += 1
    return True


def get_prime(b):
    if b < 2:
        return []
    list = [2]
    while b > 2:
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


def IsOdd(a):
    x = abs(math.remainder(a, 2))
    if x == 1:
        return True
    else:
        return False


def IsEven(a):
    x = abs(math.remainder(a, 2))
    if x == 1:
        return False
    else:
        return True


def reverse_3_digits_integer(number):
    return number % 10 * 100 + int(number / 10) % 10 * 10 + int(number / 100)


def calculate_mean(list):
    b = 0
    sum = 0
    print(len(list))
    while b != len(list):
        sum += list[b]
        b += 1
    print(sum)
    return sum / len(list)


def calculate_medium(list):
    if IsOdd(len(list)):
        return list[int(len(list) / 2)]
    else:
        return (list[int(len(list) / 2)] + list[int(len(list) / 2) + 1]) / 2


def get_input(list):
    b = float(input('What ? '))
    a = int(input('how many ? '))
    while a != 0:
        list.append(b)
        a -= 1
    d = input('Keep ? ')
    try:
        c = int(d)
    except:
        return list
    c = int(d)
    if c == 1:
        return get_input(list)
    return list


def area_of_pyramid(area, height):
    a = (area * height) / 3
    return a


def get_the_area_of_triangle(side, side1):
    c = (side * side1) / 2
    return c


def area_Trapezoid(a, b, h):
    area = (a + b / 2) * h
    return area


def pyth_theorem(a, b):
    c = math.sqrt(a * a + b * b)
    return c


def converse_of_pyth_theorem(c, a):
    b = math.sqrt((c * c) - (a * a))
    return b


def fix_missing_part_return(r, l, h, area, curved_surface_area, volume):
    a = 0
    if r != None:
        a += 1
    elif l != None and h != None:
        r = converse_of_pyth_theorem(l, h)
    elif area != None:
        r = math.sqrt((area / math.pi))
    elif curved_surface_area != None and l != None:
        r = curved_surface_area / math.pi / l
    elif volume != None and h != None:
        r = math.sqrt(volume * 3 / math.pi / h)
    if l != None:
        a += 1
    if r != None and h != None:
        l = pyth_theorem(r, h)
    elif curved_surface_area != None and r != None:
        l = curved_surface_area / math.pi / r
    if h != None:
        a += 1
    elif l != None and r != None:
        h = converse_of_pyth_theorem(l, r)
    elif volume != None and r != None:
        h = volume * 3 / math.pi / r / r
    if area != None:
        a += 1
    elif r != None:
        area = math.pi * r * r
    if curved_surface_area != None:
        a += 1
    elif r != None and h != None:
        curved_surface_area = math.pi * r * pyth_theorem(r, h)
    if volume != None:
        a += 1
    elif r != None and h != None:
        volume = math.pi * r * r * h / 3
    list = [r, l, h, area, curved_surface_area, volume]
    return list


def reverse_words(s):  
    a = s[::-1]
    return a


def reverse_words(s) :
    s_list = s.split()
    s_list.reverse()
    s_reverse = " ".join(s_list)
    return s_reverse


def reverse_array(list):
    a = 0
    b = len(list) // 2
    while a != b:
        c = list[a]
        list[a] = list[len(list) - 1 - a]
        list[len(list) - 1 - a] = c
        a += 1
    return list
