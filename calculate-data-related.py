import tools

def calculate_mean(list):
    b = 0
    sum = 0
    print(len(list))
    while b != len(list):
        sum += list[b]
        b += 1
    print(sum)
    return sum/len(list)

def calculate_medium(list):
    if Math_tools.IsOdd(len(list)):
        return list[int(len(list)/2)]
    else:
        return(list[int(len(list)/2)] + list[int(len(list)/2) + 1]) / 2

def get_input(list):
    a = int(input('how many ? '))
    b = int(input('What ? '))
    while a != 0:
        list.append(b)
        a -= 1
    d = input('Keep? ')
    try:
        c = int(d)
    except:
        print(list)
        return list
    c = int(d)
    if c == 1:
        print(list)
        return get_input(list)
