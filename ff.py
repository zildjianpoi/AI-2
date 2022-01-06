# feed forward
import math
import sys
import os

def T(x):
    global num
    num = int(num)
    if num == 2 and x <= 0:
        return 0
    if num >= 3:
        x = (1 + math.exp(-1*x))**(-1)
    if num == 4:
        x = 2*x - 1
    return x


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    return False

def init():
    inputs = []
    for arg in sys.argv:
        if os.path.isfile(arg) and arg != sys.argv[0]:
            global WEIGHTS
            WEIGHTS = open(arg, 'r').read().splitlines()
            for i, c in enumerate(WEIGHTS):
                WEIGHTS[i] = WEIGHTS[i].split()
        elif arg[0].upper() == "T":
            global num
            num = int(arg[1])
        elif is_number(arg):
            inputs.append(float(arg))

    return inputs

def dot(inputs, wl):
    ninputs = []
    while wl:
        val = 0
        for i, ch in enumerate(inputs):
            w = float(wl.pop(0))
            val = val + ch * w
        ninputs.append(T(val))
    return ninputs
def main():
    inputs = init()
    for wl in WEIGHTS[:-1]:
        inputs = dot(inputs, wl)
    for i, c in enumerate(inputs):
        inputs[i] = c * float(WEIGHTS[-1][i])
    return inputs


#print(init(), WEIGHTS, num)
print(main())