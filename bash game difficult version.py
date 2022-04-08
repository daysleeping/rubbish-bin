import math
import random
from time import sleep

def User(x,m,list,list_1):
    z = input(f'There are {x} stones. You can take 1 to {m} stone(s) away. How many stone you would like to take away ')
    try:
        y = int(z)
    except:
        print("Invalid input")
        User(x,m,list,list_1)
    for i in list_1:
        if y == i:
            x = x - y
            list.append(x)
            if x == 0:
                print("Congragulation! You win.")
                Printout = input(f'Would you like to print out the process? Type "Yes" if you want. ')
                if Printout == "Yes":
                    print(list)
                    sleep(1)
                    return 0
                else:
                    sleep(1)
                    return 0
            else:
                Op(x,m,list,list_1)
                return 0
    print("Invalid input")
    User(x,m,list,list_1)


def Op(x,m,list,list_1):
    r = abs(int(math.remainder(x,m + 1)))
    if r == 0:
        x = x - random.randint(1,m)
    else:
        x = x - r
    list.append(x)
    if x == 0:
        print("Oh. You loss")
        Printout = input(f'Would you like to print out the process? Type "Yes" if you want. ')
        if Printout == "Yes":
            print(list)
            return None
    else:
        User(x,m,list,list_1)

def get_Original_stones_numbers():
    try:
        x = int(input(f'Original stones numbers : '))
        return x
    except:
        list = get_Original_stones_numbers()
        return list

def get_Original_stones_number():
    try:
        y = int(input(f'maximum number of stones take per turn : '))
        return y
    except:
        list = get_Original_stones_number()
        return list


x = get_Original_stones_numbers()
y = get_Original_stones_number()
list = []
list.append(x)
list_1 = []
q = y
while q != 0:
    list_1.append(q)
    q -=1
User(x,y,list,list_1)
