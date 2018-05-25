from math import *

def evaluate(obj_index, x_input):
    # ZDT4 Problem
    X = x_input
    F = [0, 0]

    if obj_index==0:
        F[0] = X[0]
        return F[0]

    elif obj_index==1:
        F[1] = 91
        for i in range(1, 10, 1):
            F[1] = F[1] + pow(X[i], 2) - (10 * cos(4 * pi * X[i]))
        F[1] = F[1] * (1 - sqrt(X[0] / F[1]))

        return F[1]

    return F[obj_index]