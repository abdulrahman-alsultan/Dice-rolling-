import random

def R():
    return random.randint(1,6)

def draw():
    number = R()
    if number ==1:
        print("[-----------]")
        print("[           ]")
        print("[     0     ]")
        print("[           ]")
        print("[-----------]")
    elif number==2:
        print("[-----------]")
        print("[           ]")
        print("[   0   0   ]")
        print("[           ]")
        print("[-----------]")
    elif number == 3:
        print("[-----------]")
        print("[     0     ]")
        print("[     0     ]")
        print("[     0     ]")
        print("[-----------]")
    elif number == 4:
        print("[-----------]")
        print("[   0   0   ]")
        print("[           ]")
        print("[   0   0   ]")
        print("[-----------]")
    elif number == 5:
        print("[-----------]")
        print("[   0   0   ]")
        print("[     0     ]")
        print("[   0   0   ]")
        print("[-----------]")
    else:
        print("[-----------]")
        print("[   0   0   ]")
        print("[   0   0   ]")
        print("[   0   0   ]")
        print("[-----------]")


x = input("Ready to roll ? ENTER = roll , Q = quit")
while x == "":
    draw()
    x = input("Ready to roll ? ENTER = roll , Q = quit")

print("thanks for playing")