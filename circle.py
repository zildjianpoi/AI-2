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
            # expected values (arranged by index)
    inline = r'^x\*x\+y\*y(>=|<=|>|<)(\d+.?\d+)$'
    for arg in sys.argv:
        match = re.search(inline, arg, re.M)
        if match:
            ##Init Equation
            ##Init -> Bound ex: <= 1.21 <- bound
            global bound
            bound = float(match.group(2))
            global exp
            exp = match.group(0)
    global WEIGHTS
    global n
    n = 2
    WEIGHTS = [[random.random() * n - n/2 for i in range(30)], [random.random() * n - n/2 for i in range(100)], [random.random() * n - n/2 for i in range(20)], [random.random() * n - n/2 for i in range(2)], [random.random() * n - n/2]]
    #WEIGHTS = [[-1.48, 0.9, -1.11, 1.05, -0.64, -1.26, -1.54, -0.01], [1.77, -1.61], [0.32]]

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
def ff(inputs):
    inp = inputs
    #print('mainnnnn', WEIGHTS)
    allout = [inp]
    for wl in WEIGHTS[:-1]:
        inp = dot(inp, wl.copy())       #testNum = which case tested?
        allout.append(inp)
    for i, c in enumerate(inp):
        inp = [c * float(WEIGHTS[-1][i])]
        allout.append(inp)
    return allout
def randPoint(bound, exb, count):
    if count == 1:
        return [0,0,1]
    elif count == 2:
        return [bound, bound, 1]
    elif count == 3:
        return [bound, -bound, 1]
    elif count == 4:
        return [-bound, bound, 1]
    elif count == 5:
        return [-bound, -bound, 1]
    inputs = [random.random()*4 + bound-2, random.random()*4 + bound-2, 1]
    x = inputs[0]
    y = inputs[1]
    while eval(exp) != exb:
        inputs = [random.random() * 2 + bound - 1, random.random() * 2 + bound - 1, 1]
        x = inputs[0]
        y = inputs[1]
    return inputs


#print(init(), WEIGHTS, num)
#print(main())
          #nums go from 0 to 3(NOT 1-4)
def tot():
    """weights = []
    for col in WEIGHTS:
        weights = weights + col"""
    E = 1
    oldE = 0
    count = 1
    exb = True
    init()
    a = 3
    while count < 50000 or E > 0.001:
        if a < 0: a = -1*a
        #Set new input and ex -> new method
        inputs = randPoint(bound, exb, count)
        if E == 1: E = 0    #set first time error to 0
        ex = int(exb)
        #print('begin', E)
        NN = ff(inputs)
        error = ex - NN[-1][0]
        #print('wwwwwww', WEIGHTS)
        global WEIGHTS
        backProp(error, NN, a)
        #print("0--=--", WEIGHTS)
        NN = ff(inputs)
        #print('after', backProp(error, NN, a))
        #print(WEIGHTS)
        error = ex - NN[-1][0]
        #print('ex:', ex, error)``````````````````````````````````````````````````
        E = (E*(count-1) + (error ** 2) / 2)/count
        count += 1
        exb = not exb
        #print('---', E, NN[-1][0], ex[case])
        #print(ex, case)
        if error > 10000*E or error > 5:
            WEIGHTS = [[random.random() * n - n / 2 for i in range(60)],
                       [random.random() * n - n / 2 for i in range(200)],
                       [random.random() * n - n / 2 for i in range(20)],
                       [random.random() * n - n / 2 for i in range(2)], [random.random() * n - n / 2]]
            E = 10
            print('exit1')
            continue
        #print(E)
        #print(WEIGHTS)
        #if oldE - E > 0.1 or E - 0.01 < 0.01:
        #    a = a/2
        #print("comppppppppp", E, oldE, count)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if count%10000 == 0:
            print("Error: ", E)
            print('Layer cts:', [len(w) for w in NN])
            print("Weights: ")
            for w in WEIGHTS:
                print(w)
            if a < 0.1:
                a = a
            elif oldE > E:
                a = a/2
                oldE = E
            else:
                a = a - (E*100)
                if a<0:
                    a = 0.1
            if oldE - E < 0.000001 and E - 0.01 > 0.4 and E != 0:
                WEIGHTS = [[random.random() * n - n / 2 for i in range(30)],
                           [random.random() * n - n / 2 for i in range(20)],
                           [random.random() * n - n / 2 for i in range(2)], [random.random() * n - n / 2]]
                E = 0
                count = 1
                print('exit2')
    print("Error: ", E)
    print('Layer cts:', [len(w) for w in NN])
    print("Weights: ")
    for w in WEIGHTS:
        print(w)


def backProp(error, x, a):
    global WEIGHTS
    if a < 0: a = -1*a
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


