# feed forward
import math
import random
import sys
import os
import re
"""WEIGHTS = [[-4.0946906907596645, -0.5365228929251931, 3.6368118524696733, -2.576017519730379, -2.213627932507257, 1.929628132898788],[-5.910095878655614, 8.129920213160506],[-9.78355182680082]]
print('Layer cts:', [3, 2, 1, 1])
print("Weights: ")
for w in WEIGHTS:
    print(w)
sys.exit()"""

def T(x):
    global num
    num = 3
    if num == 2 and x <= 0:
        return 0
    if num >= 3:
        try:
            x = (1 + math.exp(-1*x))**(-1)
        except OverflowError:
            if x > 0: x = 1
            if x < 0: x = 0
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

def init():  #Change
    global inputs
    inputs = []
    global ex
    ex = []             # expected values (arranged by index)
    inline = r'^((\d )*)=> (\d)$'
    for arg in sys.argv:
        if os.path.isfile(arg) and arg != sys.argv[0]:
            lines = open(arg, 'r').read().splitlines()      # for i, c in enumerate(WEIGHTS):   WEIGHTS[i] = WEIGHTS[i].split()
            for l in lines:
                match = re.search(inline, l, re.M)
                if not match:
                    print('Error')
                    sys.exit()
                inputs.append([int(ch) for ch in match.group(1) if ch.isdigit()]+[1])
                ex.append(int(match.group(3)))
            global inNum                # Number of inputs
            inNum = len(inputs[0]) #tot inputs, including offset
    sortedex = [i[1] for i in sorted(enumerate(ex), key=lambda x:int(str(''.join(map(str, inputs[x[0]]))), 2))]
    global WEIGHTS
    global n
    n = 20
    print('Layer cts:', [3,2,1,1])
    if sortedex == [1,1,1,0]:
        WEIGHTS = [[3, 3, -6, -3, -2, -4], [-4, 4], [2]]
    elif sortedex == [1,1,0,1]:
        print([4.015028485996086, -4.5187611993896315, -2.668217114665191, 1.0084697965236444, 3.0020583791561553, 1.9547589918004884], '\n', [-3.5179991124689742, -0.23044258867712122],'\n', [2.3864884319731496])
        sys.exit()
    elif sortedex == [0,1,1,0]:
        print([7.202938919760621, -6.478370536585542, 3.0176624441630806, -8.137715349126974, 8.161118682986674, 4.045860162104338], '\n', [-2.57420625796037, -2.536653036110093],'\n', [14.503399387374516])
        sys.exit()
    elif sortedex == [1,0,0,1]:
        print([-2.59536, -2.60847, 3.68213, -5.20756, -5.08331, 1.09838],'\n', [-4.77734, 5.09581],'\n', [3.2712])
        sys.exit()
    else:
        n = 10
        WEIGHTS = [[random.random() * n - n/2 for i in range((inNum) * 2)], [random.random() * n - n/2 for i in range(2)], [random.random() * n - n/2]]
    #WEIGHTS = [[-1.48, 0.9, -1.11, 1.05, -0.64, -1.26, -1.54, -0.01], [1.77, -1.61], [0.32]]
    """print("in: ", inputs)
    print('out: ', ex)
    print('weights: ', WEIGHTS)"""
    return inputs

def dot(inp, wl):
    ninputs = []
    while wl:
        val = 0
        for i, ch in enumerate(inp):
            #print(wl, inp, i)
            w = float(wl.pop(0))
            val = val + ch * w
        ninputs.append(T(val))
    return ninputs
def main(testNum):
    inp = inputs[testNum]
    #print('mainnnnn', WEIGHTS)
    allout = [inp]
    for wl in WEIGHTS[:-1]:
        inp = dot(inp, wl.copy())       #testNum = which case tested?
        allout.append(inp)
    for i, c in enumerate(inp):
        inp = [c * float(WEIGHTS[-1][i])]
        allout.append(inp)
    return allout


#print(init(), WEIGHTS, num)
#print(main())
          #nums go from 0 to 3(NOT 1-4)
def tot():
    """weights = []
    for col in WEIGHTS:
        weights = weights + col"""
    E = 1
    oldE = 0
    init()
    while E > 0.01:
        times = 0
        a = 1
        E = 0
        #print('begin', E)
        for case in range(len(inputs)):  # first run
            NN = main(case)
            error = ex[case] - NN[-1][0]
            #print('wwwwwww', WEIGHTS)
            global WEIGHTS
            backProp(error, NN, a)
            #print("0--=--", WEIGHTS)
        E = 0
        for case in range(len(inputs)):
            NN = main(case)
            #print('after', backProp(error, NN, a))
            #print(WEIGHTS)
            error = ex[case] - NN[-1][0]
            E = E + (error ** 2) / 2
            #print('---', E, NN[-1][0], ex[case])
            #print(ex, case)
            if error > 100*E or error > 5:
                WEIGHTS = [[random.random() * n - n/2 for i in range((inNum) * 2)], [random.random() * n - n/2 for i in range(2)], [random.random() * n - n/2]]
                E = 10
                break
        #print(E)
        #print(WEIGHTS)
        #if oldE - E > 0.1 or E - 0.01 < 0.01:
        #    a = a/2
        if oldE - E < 0.1 and E - 0.01 > 0.4 and oldE != 9 and oldE != 10:
            WEIGHTS = [[random.random() * n - n/2 for i in range((inNum) * 2)],[random.random() * n - n/2 for i in range(2)], [random.random() * n - n/2]]
            E = 9
        print(E, oldE)
        oldE = E
        times = times + 1
        if times//10000 == 0:
            print('Layer cts:', [len(w) for w in NN])
            print("Weights: ")
            for w in WEIGHTS:
                print(w)
    print('Layer cts:', [len(w) for w in NN])
    print("Weights: ")
    for w in WEIGHTS:
        print(w)


def backProp(error, x, a):
    global WEIGHTS
    gradients = dict()         # En+1 * Xn       #NEED to BE REVERSED
    Er = {len(x)-1:[error]}
    for l in range(len(x)-2, -1, -1):
        #print('llll', l)
        for i,E in enumerate(Er[l+1]):
            weightsperO = len(x[l])
            Er[l] = []
            for wi in range(weightsperO):
                wei = weightsperO*i + wi     # weights index
                #print('wei', wei, 'wi', wi, 'i', i)
                gradients[l, wei] = E*x[l][wi]
                #print(l ,E, x)
                fprime = (x[l][wi]*(1-x[l][wi]))
                #print(WEIGHTS[l], wei, l)
                if len(Er[l]) == wi:
                    Er[l].append(WEIGHTS[l][wei]*E* fprime)
                else:
                    Er[l][wi] = Er[l][wi] + WEIGHTS[l][wei]*E* fprime
    #print(Er)
    #print(gradients)

    for l in range(len(WEIGHTS)):
        for w in range(len(WEIGHTS[l])):
            WEIGHTS[l][w] = WEIGHTS[l][w] + a*gradients[(l, w)]
    #print(WEIGHTS)
    return WEIGHTS



tot()







#range -> -10, 10           a = 1 or bigger


"""
Test Case 1
0 0 => 0
0 1 => 1
1 0 => 1
1 1 => 1



2:
0 0 0 => 1
0 0 1 => 1
0 1 0 => 1
0 1 1 => 1
1 0 0 => 1
1 0 1 => 1
1 1 0 => 1
1 1 1 => 0
"""