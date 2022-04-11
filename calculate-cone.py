import math

def pyth_theorem(a,b):
    c = math.sqrt(a*a + b*b)
    return c

def converse_of_pyth_theorem(c,a):
    b = math.sqrt((c * c) - (a * a))
    return b

def cone(r,h,d):
    if d == 1:
        volume = math.pi * r * r * h / 3
        return volume
    volume = r * r * h / 3
    return volume

def radius_in_cone(v,h,d):
    if d == 1:
        radius = v * 3 / math.pi / h
        return radius
    radius = v * 3 / h
    return radius

def height_in_cone(v,r,d):
    if d == 1:
        height = v * 3 / math.pi / r / r
        return height
    height = v * 3 / r / r
    return height

def slang_height(r,h):
    l = pyth_theorem(r,h)
    return l

def curved_surface_area_cone(r,h,d):
    if d == 1:
        l = slang_height(r,h)
        area = math.pi * r * l
        return area
    l = slang_height(r,h)
    area = r * l
    return area

def fix_missing_part_return(r,l,h,area,curved_surface_area,volume):
    a = 0
    if r != None:
        a += 1
    elif l != None and h != None:
        r = converse_of_pyth_theorem(l,h)
    elif area != None:
        r = math.sqrt((area / math.pi))
    elif curved_surface_area != None and l != None:
        r = curved_surface_area / math.pi / l
    elif volume != None and h != None:
        r = math.sqrt(volume * 3 / math.pi / h)
    if l != None: 
        a += 1
    if r != None and h != None:
        l = pyth_theorem(r,h)
    elif curved_surface_area != None and r != None:
        l = curved_surface_area / math.pi / r
    if h != None:
        a += 1
    elif l != None and r != None:
        h = converse_of_pyth_theorem(l,r)
    elif volume != None and r != None:
        h = volume * 3 / math.pi / r / r
    if area != None:
            a += 1
    elif r != None:
        area = math.pi * r * r
    if curved_surface_area != None:
        a += 1
    elif r != None and h != None:
        curved_surface_area = math.pi * r * pyth_theorem(r,h)
    if volume != None:
        a += 1
    elif r != None and h != None:
        volume = math.pi * r * r * h / 3
    list = [r,l,h,area,curved_surface_area,volume]
    return list
