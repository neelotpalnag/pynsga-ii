import random

# THE SIMULATED BINARY CROSSOVER for Real-Coded GA


def cross_sbx(num_obj, X_pool, cxi, pop_size, num_params, seed):
    # The method "cross_sbx" requires the following parameters:
    # X : The mating population pool from selection
    # cxi : The Crossover Index ~20
    # X_hi : Max. Values of Xi
    # X_lo : Min. Values of Xi
    # pop_size : Population Size

    # Step 1 : Randomly select two members from the Mating Pool
    X_daughters = []
    for i in range(0, int(pop_size/2), 1):
        # Choose 2 members randomly:
        random.seed(seed)
        rn = random.sample(range(0, pop_size-1), 2) # List of 2 random numbers
        random.seed(seed)
        rn_beta = random.random()
        beta = beta_calculator(rn_beta, cxi)

        xd1 = []
        xd2 = []
        for j in range(0, num_params, 1):
            xd1.append(0.5*((1-beta)*X_pool[rn[0]][j] + (1+beta)*X_pool[rn[1]][j]))
            xd2.append(0.5*((1+beta)*X_pool[rn[0]][j] + (1-beta)*X_pool[rn[1]][j]))

        X_daughters.append(xd1)
        X_daughters.append(xd2)

    return X_daughters


def beta_calculator(rn, cxi):
    if rn < 0.5:
        return pow(2*rn, (1/(cxi+1)))
    else:
        return 1/pow(2*(1-rn), (1/(cxi+1)))
