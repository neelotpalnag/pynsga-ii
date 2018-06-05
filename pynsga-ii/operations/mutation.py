import random
from operations.evaluate import evaluate

# POLYNOMIAL MUTATION for Real Coded GA


def mutate(num_objectives, X_pool, X_hi, X_lo, mui, pop_size):
    # The method "mutate" requires the following parameters:
    # X_pool : The population from the previous generation
    # X_hi : Max. Values of Xi
    # X_lo : Min. Values of Xi
    # pop_size : Population Size
    # seed_gen : For random number gen

    num_params = len(X_hi)
    X_mut = []
    for i in range(0, pop_size, 1):
        xm = []
        random.seed(i)
        rn = random.random()

        for j in range(0, num_params, 1):
            val = X_pool[i][j] + (X_hi[j] - X_lo[j])*delta_calculator(rn, mui)
            if val > X_hi[j]:
                val = X_hi[j]
            elif val < X_lo[j]:
                val = X_lo[j]
            xm.append(val)

        x_ev = xm
        for k in range(0, num_objectives, 1):
            xm.append(evaluate(k, x_ev))

        X_mut.append(xm)

    return X_mut


def delta_calculator(rn, mui):
    if rn < 0.5:
        return pow((2*rn), (1/(mui+1))) -1
    else:
        return 1- 1/pow((2 -2*rn), (1/(mui+1)))